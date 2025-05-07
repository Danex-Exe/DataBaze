const fs = require('fs').promises;
const path = require('path');

class DataFile {
    constructor(name, type = 'json', encode = 'utf-8', dirPath = '.', logs = false, logger = null) {
        this._name = name;
        this._type = type;
        this._encode = encode;
        this._path = dirPath;
        this._logs = logs;
        this._logger = logger;
    }

    _log(level, message) {
        if (this._logs) {
            const msg = `[DataFile] ${message}`;
            if (this._logger) {
                level === 'INFO' ? this._logger.info(msg) : this._logger.error(msg);
            } else {
                level === 'INFO' ? console.log(msg) : console.error(msg);
            }
        }
    }

    async create(data = "") {
        const filePath = path.join(this._path, `${this._name}.${this._type}`);
        try {
            await fs.mkdir(this._path, { recursive: true });
            try {
                await fs.access(filePath);
                this._log('INFO', `File exists: ${filePath}`);
                return 'file_exists';
            } catch {
                const content = this._type === 'json' 
                    ? JSON.stringify(data, null, 2) 
                    : String(data);
                await fs.writeFile(filePath, content, this._encode);
                this._log('INFO', `File created: ${filePath}`);
                return 'success';
            }
        } catch (err) {
            this._log('ERROR', `Create error: ${err.message}`);
            return 'error';
        }
    }

    async read() {
        const filePath = path.join(this._path, `${this._name}.${this._type}`);
        try {
            const data = await fs.readFile(filePath, this._encode);
            if (this._type === 'json') {
                return data.trim() ? JSON.parse(data) : {};
            }
            return data;
        } catch (err) {
            if (err.code === 'ENOENT') {
                this._log('INFO', `File not found: ${filePath}`);
            } else {
                this._log('ERROR', `Read error: ${err.message}`);
            }
            return null;
        }
    }

    async write(data, rewrite = true) {
        const filePath = path.join(this._path, `${this._name}.${this._type}`);
        try {
            await fs.access(filePath);
            const content = this._type === 'json' 
                ? JSON.stringify(data, null, 2) 
                : String(data);
            await fs.writeFile(filePath, content, { 
                encoding: this._encode, 
                flag: rewrite ? 'w' : 'a' 
            });
            this._log('INFO', `Data written to: ${filePath}`);
        } catch (err) {
            this._log('ERROR', `Write error: ${err.message}`);
        }
    }

    async delete() {
        const filePath = path.join(this._path, `${this._name}.${this._type}`);
        try {
            await fs.unlink(filePath);
            this._log('INFO', `File deleted: ${filePath}`);
        } catch (err) {
            if (err.code === 'ENOENT') {
                this._log('INFO', `File not found: ${filePath}`);
            } else {
                this._log('ERROR', `Delete error: ${err.message}`);
            }
        }
    }

    async rename(newName) {
        const oldPath = path.join(this._path, `${this._name}.${this._type}`);
        const newPath = path.join(this._path, `${newName}.${this._type}`);
        try {
            await fs.rename(oldPath, newPath);
            this._name = newName;
            this._log('INFO', `File renamed to: ${newName}`);
        } catch (err) {
            this._log('ERROR', `Rename error: ${err.message}`);
        }
    }

    async info() {
        const filePath = path.join(this._path, `${this._name}.${this._type}`);
        try {
            const stats = await fs.stat(filePath);
            return {
                name: `${this._name}.${this._type}`,
                path: filePath,
                father: path.dirname(filePath),
                size: stats.size,
                modified: stats.mtime.toLocaleString('ru-RU')
            };
        } catch (err) {
            this._log('ERROR', `Info error: ${err.message}`);
            return null;
        }
    }

    get name() { return this._name; }
    get type() { return this._type; }
    get encode() { return this._encode; }
    get path() { return this._path; }
    get logs() { return this._logs; }
    get logger() { return this._logger; }
}

class DataBaze {
    constructor(dirPath = 'data/', logs = false, logger = null) {
        this._path = dirPath;
        this._logs = logs;
        this._logger = logger;
    }

    _log(level, message) {
        if (this._logs) {
            const msg = `[DataBaze] ${message}`;
            if (this._logger) {
                level === 'INFO' ? this._logger.info(msg) : this._logger.error(msg);
            } else {
                level === 'INFO' ? console.log(msg) : console.error(msg);
            }
        }
    }

    file(name, type = 'json', encode = 'utf-8') {
        return new DataFile(name, type, encode, this._path, this._logs, this._logger);
    }

    async delete() {
        try {
            await fs.rm(this._path, { recursive: true, force: true });
            this._log('INFO', `Directory deleted: ${this._path}`);
        } catch (err) {
            if (err.code === 'ENOENT') {
                this._log('INFO', `Directory not found: ${this._path}`);
            } else {
                this._log('ERROR', `Delete error: ${err.message}`);
            }
        }
    }

    get path() { return this._path; }
    get logs() { return this._logs; }
    get logger() { return this._logger; }
}

module.exports = { DataFile, DataBaze };
