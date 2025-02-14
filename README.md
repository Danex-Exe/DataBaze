# Usage

# DataFile(name, type, encode, path, logs)

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

 # DataBaze(path, logs)

        path - путь до папки (default - .)
        logs - Показывать/Скрывать логи (default - False)

        .file(name, type, encode) - обьявляет файл
        .delete() - удаляет все файлы в базе данных


# Application

```python
from DataBaze import *

db = DataBaze(path = 'data', logs = True)
data_file = db.file(name = 'data', type = "json", encode = "utf-8")
data_file.create() # if not created
data = {
        "users": ["User1", "User2"],
        "admins": ["User1"]
}
data_file.write(data)
print(data_file.read()['admins'])
```
