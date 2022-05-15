const mysql = require('mysql');

const Connection = mysql.createConnection({
    host: '127.0.0.1',
    user: 'root',
    password: '',
    database: 'movies-control'
})

module.exports = Connection;
