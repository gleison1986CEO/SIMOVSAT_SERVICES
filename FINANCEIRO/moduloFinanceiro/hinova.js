const request    = require('request');
const path       = require('path')
const dotenv     = require('dotenv')
const LOGS       = require("../log/logs");
const jar        = request.jar();
dotenv.config({ path: path.join(__dirname, '../.env') })

module.exports.HINOVA = async function (){

  return new Promise((resolve, reject) => {
      jar.setCookie(request.cookie(process.env.COOKIE), process.env.AUTH);

      const options = {
        method: 'POST',
        url: process.env.AUTH,
        headers: {
          'Content-Type': process.env.HEADERS,
          'User-Agent': process.env.USERAGENT,
          Authorization: `Bearer ${process.env.BEARTOKENS}`
        },
        body: {usuario: process.env.LOGIN, senha: process.env.SENHA},
        json: true,
        jar: 'JAR'
      };

      request(options, function (error, response, body) {
        if (error) throw new Error(error);
          const token = body["token_usuario"]
          LOGS.LOGS(token);
          return resolve(token);

        
      });});
}
