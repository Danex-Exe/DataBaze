import shutil
import logging
import os
import json
from datetime import datetime

class DataFile:
    """
        DataFile(name, type, encode, path, logs, logger)

        name - Название файла
        type - Расширение файла (default - json)
        encode - Кодировка файла (default - utf-8)
        path - Путь до файла (default - .)
        logs - Показывать/Скрывать логи (default - False)
        logger - Логер (default - None)

        .create() - создает файл и, при необходимости, создает папку
        .read() - чтение файла (если файл - json, то автоматическое переобразование в словарь)
        .write(data) - запись данных в файл (если файл - json, то автоматическое переобразование в строчку)
        .delete() - удаление файла
        .rename(new_name) - переименование файла
        .info() - возвращает информацию о файле (родительская папка, путь, размер, название, дата последнего изменения)
    """

    def __init__(self, name: str, type: str = "json", encode: str = "utf-8", path: str = ".", logs: bool = False, logger: logging.Logger = None):
        """
            name - Название файла
            type - Расширение файла (default - json)
            encode - Кодировка файла (default - utf-8)
            path - Путь до файла (default - .)
            logs - Показывать/Скрывать логи (default - False)
            logger - Логер (default - None)
        """

        self._name = name
        self._type = type
        self._encode = encode
        self._path = path
        self._logs = logs
        self._logger = logger


    def _log(self, level, message):
        if self._logs and self._logger:
            if level == 'INFO':
                self._logger.info(message)


            elif level == 'ERROR':
                self._logger.error(message)


    def create(self, data=""):
        """
            .create(data) - создает файл и, при необходимости, создает папку
            data (default - '') - Данные
        """


        file_path = os.path.join(self.path, f'{self.name}.{self.type}')


        if not os.path.exists(self.path):
            os.makedirs(self.path)


            self._log('INFO', f'[DataFile - Create] Создана папка: {self.path}')


        if not os.path.exists(file_path):
            try:
                with open(file_path, "w", encoding=self.encode) as f:
                    if self.type == "json":
                        f.write(json.dumps(data, ensure_ascii=False, indent=4))
                        self._log('INFO', f'[DataFile - Write] Данные успешно записаны в файл {file_path}')


                    else:
                        f.write(str(data))
                        self._log('INFO', f'[DataFile - Write] Данные успешно записаны в файл {file_path}')


                self._log('INFO', f'[DataFile - Create] Файл {file_path} успешно создан.')


                return 'success'
            

            except Exception as e:
                self._log('ERROR', f'[DataFile - Create] Ошибка при создании файла {file_path}: {e}')


                return 'error'
            

        else:
            self._log('INFO', f'[DataFile - Create] Файл уже существует: {file_path}')


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
                            self._log('INFO', f'[DataFile - Read] Файл {file_path} успешно прочтен.')


                            return json.loads(content)
                        

                        else:
                            self._log('INFO', f'[DataFile - Read] Файл {file_path} пустой, возвращен пустой словарь.')


                            return {}
                        

                    else:
                        self._log('INFO', f'[DataFile - Read] Файл {file_path} успешно прочтен.')


                        return f.read()
                    

            except json.JSONDecodeError as e:
                self._log('ERROR', f'[DataFile - Read] Ошибка при чтении JSON из файла {file_path}: {e}')


                return None
            

            except Exception as e:
                self._log('ERROR', f'[DataFile - Read] Неизвестная ошибка при чтении файла {file_path}: {e}')


                return None
            

        else:
            self._log('INFO', f'[DataFile - Read] Файл {file_path} не найден.')


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
                mode = "w" if rewrite else "a"


                with open(file_path, mode, encoding=self.encode) as f:
                    if self.type == "json":
                        f.write(json.dumps(data, ensure_ascii=False, indent=4))


                        self._log('INFO', f'[DataFile - Write] Данные успешно записаны в файл {file_path}')


                    else:
                        f.write(str(data))


                        self._log('INFO', f'[DataFile - Write] Данные успешно записаны в файл {file_path}')


            except TypeError as e:
                self._log('ERROR', f'[DataFile - Write] Ошибка типа при записи в файл {file_path}: {e}')


            except Exception as e:
                self._log('ERROR', f'[DataFile - Write] Неизвестная ошибка при записи в файл {file_path}: {e}')


        else:
            self._log('INFO', f'[DataFile - Write] Файл {file_path} не найден.')


    def delete(self):
        """
            .delete() - удаление файла
        """


        file_path = os.path.join(self.path, f'{self.name}.{self.type}') if self.type != "" else ""


        if os.path.exists(file_path):
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)


                    self._log('INFO', f"[DataFile - Delete] Файл {file_path} успешно удален.")


            except Exception as e:
                self._log('ERROR', f"[DataFile - Delete] Ошибка при удалении файла {file_path}: {e}")


        else:
            self._log('INFO', f'[DataFile - Delete] Файл {file_path} не найден.')



    def rename(self, new_name: str):
        """
            .rename(new_name) - переименование файла
        """


        old_file_path = os.path.join(self.path, f'{self.name}.{self.type}')
        new_file_path = os.path.join(self.path, f'{new_name}.{self.type}')


        if os.path.exists(old_file_path):
            try:
                os.rename(old_file_path, new_file_path)


                self._log('INFO', f"[DataFile - Rename] Файл {self.name} успешно переименнован в {new_name}")
                self._name = new_name


            except Exception as e:
                self._log('ERROR', f"[DataFile - Rename] Ошибка при переименовании файла {old_file_path} в {new_file_path}: {e}")


        else:
            self._log('INFO', f'[DataFile - Rename] Файл {old_file_path} не найден.')


    def info(self):
        """
            .info() - возвращает информацию о файле (родительская папка, путь, размер, название, дата последнего изменения)
        """


        file_path = os.path.join(self.path, f'{self.name}.{self.type}')


        if os.path.exists(file_path):
            try:
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


                self._log('INFO', f"[DataFile - Info] Информация о файле {file_path} успешно получена.")


                return info
            

            except Exception as e:
                self._log('ERROR', f"[DataFile - Info] Ошибка при получении информации о файле {file_path}: {e}")


                return None
            

        else:
            self._log('INFO', f'[DataFile - Info] Файл {file_path} не найден.')


            return None

    
    @property
    def name(self):
        return self._name
    

    @property
    def type(self):
        return self._type
    

    @property
    def encode(self):
        return self._encode
    

    @property
    def path(self):
        return self._path
    

    @property
    def logs(self):
        return self._logs
    

    @property
    def logger(self):
        return self._logger


class DataBaze:
    """
        DataBaze(path, logs, logger)

        path - путь до папки
        logs - Показывать/Скрывать логи (default - False)
        logger - Логер (default - None)

        .file(name, type, encode) - обьявляет файл
        .delete() - удаляет все файлы в базе данных
    """


    def __init__(self, path: str = "data/", logs: bool = False, logger: logging.Logger = None):
        """
            path - путь до папки
            logs - Показывать/Скрывать логи (default - False)
            logger - Логер (default - None)
        """


        self.path = path
        self.logs = logs
        self.logger = logger


    def _log(self, level, message):
        if self.logs and self.logger:
            if level == 'INFO':
                self.logger.info(message)


            elif level == 'ERROR':
                self.logger.error(message)


    def file(self, name: str, type: str = "json", encode: str = "utf-8") -> DataFile:
        """
            .file(name, type, encode) - обьявляет файл
            Returns an instance of DataFile.
        """


        return DataFile(name, type, encode, self.path, self.logs, self.logger)
    

    def delete(self):
        """
            .delete() - удаляет папку и все ее содержимое
        """

        if os.path.exists(self.path):
            try:
                shutil.rmtree(self.path)


                self._log('INFO', f"[DataBaze - Delete] Папка {self.path} успешно удалена.")


            except Exception as e:
                self._log('ERROR', f"[DataBaze - Delete] Ошибка при удалении папки {self.path}: {e}")

                
        else:
            self._log('INFO', f'[DataBaze - Delete] Папка {self.path} не найдена.')
