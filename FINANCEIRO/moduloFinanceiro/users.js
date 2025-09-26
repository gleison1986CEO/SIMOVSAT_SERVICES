const path       = require('path')
const dotenv     = require('dotenv')
const request    = require('request');
const LOGS       = require("../log/logs");

dotenv.config({ path: path.join(__dirname, '../.env') })

module.exports.DATA = async function (cpf, KEY){
    
    return new Promise((resolve, reject) => {
        
        
        const jar     = request.jar();


        jar.setCookie(request.cookie(process.env.COOKIE), `${process.env.USERS}${cpf}`);

        const options = {
        method: 'GET',
        url: `${process.env.USERS}${cpf}`,
        headers: {
            'User-Agent': process.env.USERAGENT,
            Authorization: `Bearer ${KEY}`
        },
        jar: 'JAR'
        };

        request(options, function (error, response, body) {
        if (error) throw new Error(error);
        LOGS.LOGS(body)
        return resolve(body);
    });});

}
