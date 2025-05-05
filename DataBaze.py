import os, json, shutil
from datetime import datetime
from fastapi import FastAPI, HTTPException, Request
from typing import Any, Optional
import os
import json

class DataAPIServer:
    def __init__(self, db, file_name: str = 'config'):
        self.db = db
        self.file_name = file_name
        self.app = FastAPI()
        self.data_file = self.db.file(self.file_name, type='json', encode='utf-8')
        self._setup_routes()

    def _get_full_path(self):
        return os.path.join(self.db.path, f"{self.file_name}.json")

    def _ensure_file_exists(self):
        if not os.path.exists(self._get_full_path()):
            raise HTTPException(status_code=404, detail="File not found")

    def _setup_routes(self):
        @self.app.get("/{path:path}")
        async def read_data(path: str):
            self._ensure_file_exists()
            data = self.data_file.read()
            if not isinstance(data, dict):
                raise HTTPException(status_code=500, detail="Invalid JSON data")
            
            path_parts = path.split('/') if path else []
            current = data
            for part in path_parts:
                if isinstance(current, dict) and part in current:
                    current = current[part]
                else:
                    raise HTTPException(status_code=404, detail=f"Key '{part}' not found")
            return current

        @self.app.post("/{path:path}")
        async def update_data(path: str, request: Request):
            self._ensure_file_exists()
            data = self.data_file.read()
            if not isinstance(data, dict):
                raise HTTPException(status_code=500, detail="Invalid JSON data")
            
            path_parts = path.split('/') if path else []
            if not path_parts:
                raise HTTPException(status_code=400, detail="Cannot update root")
            
            key = path_parts[-1]
            query_params = dict(request.query_params)
            if key not in query_params:
                raise HTTPException(status_code=400, detail=f"Missing parameter '{key}'")
            value = query_params[key]
            
            current = data
            for part in path_parts[:-1]:
                if isinstance(current, dict) and part in current:
                    current = current[part]
                else:
                    raise HTTPException(status_code=404, detail=f"Path part '{part}' not found")
            
            if not isinstance(current, dict):
                raise HTTPException(status_code=400, detail="Parent is not a dictionary")
            
            current[key] = value
            self.data_file.write(data)
            return {"status": "success", "message": "Data updated"}

        @self.app.delete("/{path:path}")
        async def delete_data(path: str):
            self._ensure_file_exists()
            data = self.data_file.read()
            if not isinstance(data, dict):
                raise HTTPException(status_code=500, detail="Invalid JSON data")
            
            path_parts = path.split('/') if path else []
            if not path_parts:
                raise HTTPException(status_code=400, detail="Cannot delete root")
            
            key = path_parts[-1]
            parent_parts = path_parts[:-1]
            
            current = data
            for part in parent_parts:
                if isinstance(current, dict) and part in current:
                    current = current[part]
                else:
                    raise HTTPException(status_code=404, detail=f"Path part '{part}' not found")
            
            if not isinstance(current, dict) or key not in current:
                raise HTTPException(status_code=404, detail=f"Key '{key}' not found")
            
            del current[key]
            self.data_file.write(data)
            return {"status": "success", "message": "Key deleted"}

        @self.app.get("/")
        async def read_root():
            self._ensure_file_exists()
            return self.data_file.read()
        
class DataFile:

    """
        DataFile(name, type, encode, path, logs)

        name - Название файла
        type - Расширение файла (default - json)
        encode - Кодировка файла (default - utf-8)
        path - Путь до файла (default - .)
        logs - Показывать/Скрывать логи (default - False)

        .create() - создает файл и, при необходимости, создает папку
        .read() - чтение файла (если файл - json, то автоматическое переобразование в словарь)
        .write(data) - запись данных в файл (если файл - json, то автоматическое переобразование в строчку)
        .delete() - удаление файла
        .rename(new_name) - переименование файла
        .info() - возвращает информацию о файле (родительская папка, путь, размер, название, дата последнего изменения)
    """

    def __init__(self, name: str, type: str = "json", encode: str = "utf-8", path: str = ".", logs: bool = False):

        """
            name - Название файла
            type - Расширение файла (default - json)
            encode - Кодировка файла (default - utf-8)
            path - Путь до файла (default - .)
            logs - Показывать/Скрывать логи (default - False)
        """

        self.name = name
        self.type = type
        self.encode = encode
        self.path = path
        self.logs = logs

    def create(self, data = ""):

        """
            .create(data) - создает файл и, при необходимости, создает папку
            data - Данные
        """

        file_path = os.path.join(self.path, f'{self.name}.{self.type}')
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        if not os.path.exists(file_path):
            try:
                with open(file_path, 'w', encoding=self.encode) as f:
                    f.write(data)
                if self.logs: print(f'[DataFile - Create] {file_path} успешно создан.')
                return 'success'
            except Exception as e:
                if self.logs: print(f'[DataFile - Create] Ошибка при создании файла {file_path}: {e}')
                return 'error'
        else:
            if self.logs: print(f'[DataFile - Create] Файл уже существует: {file_path}')
            return 'file_exists'

    def read(self):

        """
            .read() - чтение файла (если файл - json, то автоматическое преобразование в словарь)
        """

        file_path = os.path.join(self.path, f'{self.name}.{self.type}')
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding=self.encode) as f:
                    if self.type == "json":
                        content = f.read()
                        if content.strip():
                            return json.loads(content)
                        else:
                            return {}
                    else:
                        return f.read()
                if self.logs: print(f'[DataFile - Read] Файл {file_path} успешно прочтен.')
            except json.JSONDecodeError as e:
                if self.logs: print(f'[DataFile - Read] Ошибка при чтении файла {file_path}: {e}')
            except Exception as e:
                if self.logs: print(f'[DataFile - Read] Неизвестная ошибка при чтении файла {file_path}: {e}')
        else:
            if self.logs: print(f'[DataFile - Read] Файл {file_path} не найден.')
            return None


    def write(self, data, rewrite: bool = True):

        """
            .write(data, type) - запись данных в файл (если файл - json, то автоматическое переобразование в строчку)
            data - Данные
            rewrite - Перезаписывать (True/False)
        """

        file_path = os.path.join(self.path, f'{self.name}.{self.type}')
        if os.path.exists(file_path):
            try:
                if not rewrite:
                    with open(file_path, "a", encoding=self.encode) as f:
                        if self.type == "json":
                            f.write(json.dumps(data, ensure_ascii=False, indent=4))
                            if self.logs: print(f'[DataFile - Write] Данные успешно записаны в файл {file_path}')
                        else:
                            f.write(str(data))
                            if self.logs: print(f'[DataFile - Write] Данные успешно записаны в файл {file_path}')
                else:
                    with open(file_path, "w", encoding=self.encode) as f:
                        if self.type == "json":
                            f.write(json.dumps(data, ensure_ascii=False, indent=4))
                            if self.logs: print(f'[DataFile - Write] Данные успешно записаны в файл {file_path}')
                        else:
                            f.write(str(data))
                            if self.logs: print(f'[DataFile - Write] Данные успешно записаны в файл {file_path}')
            except TypeError as e:
                if self.logs: print(f'[DataFile - Write] Ошибка при записи в файл {file_path}: {e}')
            except Exception as e:
                if self.logs: print(f'[DataFile - Write] Неизвестная ошибка при записи в файл {file_path}: {e}')
        else:
            if self.logs: print(f'[DataFile - Write] Файл {file_path} не найден.')

    def delete(self):

        """
            .delete() - удаление файла
        """
        
        file_path = os.path.join(self.path, f'{self.name}.{self.type}') if self.type != "" else ""
        if os.path.exists(file_path):
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    if self.logs: print(f"[DataFile - Delete] Файл {file_path} успешно удален.")
            except Exception as e:
                if self.logs: print(f"[DataFile - Delete] Ошибка при удалении файла {file_path}: {e}")
        else:
            if self.logs: print(f'[DataFile - Delete] Файл {file_path} не найден.')

    def rename(self, new_name: str):

        """
            .rename(new_name) - переименование файла
        """

        old_file_path = os.path.join(self.path, f'{self.name}.{self.type}')
        new_file_path = os.path.join(self.path, f'{new_name}.{self.type}')
        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
            if self.logs: print(f"[DataFile - Rename] Файл {self.name} успешно переименнован в {new_name}")
            self.name = new_name
        else:
            if self.logs: print(f'[DataFile - Rename] Файл {old_file_path} не найден.')

    def info(self):

        """
            .info() - возвращает информацию о файле (родительская папка, путь, размер, название, дата последнего изменения)
        """

        file_path = os.path.join(self.path, f'{self.name}.{self.type}')
        if os.path.exists(file_path):
            file_info = os.stat(file_path)
            parent_folder = os.path.dirname(file_path)
            file_size = file_info.st_size
            last_modified = file_info.st_mtime
            last_modified_formatted = datetime.fromtimestamp(last_modified).strftime('%d.%m.%Y %H:%M:%S')
            info = {
                "name": f'{self.name}.{self.type}',
                "path": file_path,
                "father": parent_folder,
                "size": file_size,
                "modified": last_modified_formatted,
            }
            if self.logs: print(f"[DataFile - Info] Информация о файле {file_path} успешно получена.")
            return info
        else:
            if self.logs: print(f'[DataFile - Info] Файл {file_path} не найден.')
            return None


class DataBaze:

    """
        DataBaze(path, logs)

        path - путь до папки
        logs - Показывать/Скрывать логи (default - False)

        .file(name, type, encode) - обьявляет файл
        .delete() - удаляет все файлы в базе данных
    """
        
    def __init__(self, path: str = "data/", logs: bool = False):

        """
            path - путь до папки
            logs - Показывать/Скрывать логи (default - False)
        """
        
        self.path = path
        self.logs = logs

    def file(self, name: str, type: str = "json", encode: str = "utf-8"):

        """
            .file(name, type, encode) - обьявляет файл
        """

        return DataFile(name, type, encode, self.path, self.logs)

    def delete(self):

        """
            .delete() - удаляет все файлы в папке
        """
        
        if os.path.exists(self.path):
            try:
                shutil.rmtree(self.path)
                if self.logs:
                    print(f"[DataFile - Delete] Папка {self.path} успешно удалена.")
            except Exception as e:
                if self.logs:
                    print(f"[DataFile - Delete] Ошибка при удалении папки {self.path}: {e}")
        else:
            if self.logs:
                print(f'[DataFile - Delete] Папка {self.path} не найдена.')
