# Usage

## DataFile(name, type, encode, path, logs, logger)

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

 ## DataBaze(path, logs, logger)

        path - путь до папки (default - .)
        logs - Показывать/Скрывать логи (default - False)
        logger - Логер (default - None)

        .file(name, type, encode) - обьявляет файл
        .delete() - удаляет все файлы в базе данных


# Application

```python
from DataBaze import DataBaze


DATABAZE = DataBaze()
CONFIG_FILE = DATABAZE.file('config')
CONFIG_FILE.create() # if not created


data = {
        "users": ["User1", "User2"],
        "admins": ["User1"]
}


data_file.write(data)
print(data_file.read()['admins']) # ["User1"]
```


```js
const { DataBaze } = require('./DataBaze');

async function main() {
    const db = new DataBaze('my-data');
    const file = db.file('config');
    
    // Создание файла
    await file.create({ version: 1.0 });
    
    // Чтение файла
    const data = await file.read();
    console.log(data);
    
    // Обновление данных
    await file.write({ ...data, updated: new Date() });
    
    // Получение информации о файле
    const info = await file.info();
    console.log(info);
    
    // Удаление базы данных
    await db.delete();
}

main();
```
