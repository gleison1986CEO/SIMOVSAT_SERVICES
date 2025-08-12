var mysql        = require('mysql');
const path       = require('path')
const dotenv     = require('dotenv')

dotenv.config({ path: path.join(__dirname, '../.env') })


module.exports.ConnGPWROX = function (){

  var connection = mysql.createConnection({
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0,
    host     : process.env.HOST,
    user     : process.env.USERSDATA,
    password : process.env.PASS,
    database : process.env.DATABASE

  });
  connection.connect();
  return connection;
}


module.exports.ConnTRACCAR = function (){

  var connection = mysql.createConnection({
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0,
    host     : process.env.HOST,
    user     : process.env.USERSDATA,
    password : process.env.PASS,
    database : process.env.DATABASETRACCAR
    
  });
  connection.connect();
  return connection;
}
