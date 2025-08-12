const path       = require('path')
const dotenv     = require('dotenv')
const request    = require('request');
dotenv.config({ path: path.join(__dirname, '../.env') })




const DATETODAY = new Date().toLocaleDateString('en-GB');
var d = new Date(); 
var x = 5;
const dates    = d.setDate(d.getDate() + x);
var FIVEDAYS = new Date(dates).toLocaleDateString("en-GB")


const month = DATETODAY.split('/')[1];
const year  = DATETODAY.split('/')[2];


const day01 = "01/" + month + "/" + year
const day15 = "15/" + month + "/" + year
const day10 = "10/" + month + "/" + year
const day08 = "08/" + month + "/" + year
const day05 = "05/" + month + "/" + year
const day18 = "18/" + month + "/" + year
const day20 = "20/" + month + "/" + year
const day22 = "22/" + month + "/" + year
const day27 = "27/" + month + "/" + year
const day28 = "28/" + month + "/" + year
const day29 = "29/" + month + "/" + year
const day30 = "30/" + month + "/" + year
const day31 = "31/" + month + "/" + year



module.exports.METOD1 = async function (associado, KEY){
    return new Promise((resolve, reject) => {
            
            if(DATETODAY == day28 || DATETODAY == day29 || DATETODAY == day30 || DATETODAY == day31){
                const MSG       = 'None'    
                return resolve(MSG);

            }else if(DATETODAY >= day01 && DATETODAY <= day27 ){
                    
                    const jar       = request.jar();
                    jar.setCookie(request.cookie(process.env.COOKIE), process.env.ASSOCIADOS);
                
                    const options = {
                    method: 'POST',
                    url: process.env.ASSOCIADOS,
                    headers: {
                        'User-Agent': process.env.USERAGENT,
                        Authorization: `Bearer ${KEY}`
                    },
                    
                    body: {
                        codigo_associado: associado.toString(),
                        codigo_situacao_boleto: '1',
                        data_vencimento_inicial: day01,
                        data_vencimento_final: day27
                    },
                    json: true,
                    jar: 'JAR'
                    };

                    request(options, function (error, response, body) {
                    if (error) throw new Error(error);

                    return resolve(body);
                });
            }
 
  });

}



module.exports.METOD2 = async function (associado, KEY){
    return new Promise((resolve, reject) => {
        
        if(DATETODAY == day28 || DATETODAY == day29 || DATETODAY == day30 || DATETODAY == day31){
            const MSG       = 'None' 
            return resolve(MSG);

        }else  if(DATETODAY >= day01 && DATETODAY <= day27 ){
                
                const jar       = request.jar();
                jar.setCookie(request.cookie(process.env.COOKIE), process.env.ASSOCIADOS);
            
                const options = {
                method: 'POST',
                url: process.env.ASSOCIADOS,
                headers: {
                    'User-Agent': process.env.USERAGENT,
                    'Content-Type': process.env.HEADERS,
                    Authorization: `Bearer ${KEY}`
                },
                body: {
                    codigo_associado: associado.toString(),
                    codigo_situacao_boleto: '2',
                    data_vencimento_inicial: day01,
                    data_vencimento_final: day27

                },
                json: true,
                jar: 'JAR'
                };

                request(options, function (error, response, body) {
                if (error) throw new Error(error);
                return resolve(body);
            });

        }
  });

}





module.exports.METOD3 = async function (associado, KEY){
    return new Promise((resolve, reject) => {
        
        if(DATETODAY == day28 || DATETODAY == day29 || DATETODAY == day30 || DATETODAY == day31){
            const MSG       = 'None' 
            return resolve(MSG);

        }else  if(DATETODAY >= day01 && DATETODAY <= day27 ){
                
                const jar       = request.jar();
                jar.setCookie(request.cookie(process.env.COOKIE), process.env.ASSOCIADOS);
            
                const options = {
                method: 'POST',
                url: process.env.ASSOCIADOS,
                headers: {
                    'User-Agent': process.env.USERAGENT,
                    Authorization: `Bearer ${KEY}`
                },
                body: {
                    codigo_associado: associado.toString(),
                    codigo_situacao_boleto: '3',
                    data_vencimento_inicial: day01,
                    data_vencimento_final: day27
                },
                json: true,
                jar: 'JAR'
                };

                request(options, function (error, response, body) {
                if (error) throw new Error(error);

                return resolve(body);
            });
        }
  });

}




module.exports.METOD4 = async function (associado, KEY){
    return new Promise((resolve, reject) => {

        if(DATETODAY == day28 || DATETODAY == day29 || DATETODAY == day30 || DATETODAY == day31){
            const MSG       = 'None' 
            return resolve(MSG);

        }else  if(DATETODAY >= day01 && DATETODAY <= day27 ){
                
                const jar       = request.jar();
                jar.setCookie(request.cookie(process.env.COOKIE), process.env.ASSOCIADOS);
            
                const options = {
                method: 'POST',
                url: process.env.ASSOCIADOS,
                headers: {
                    'User-Agent': process.env.USERAGENT,
                    Authorization: `Bearer ${KEY}`
                },
                body: {
                    codigo_associado: associado.toString(),
                    codigo_situacao_boleto: '4',
                    data_vencimento_inicial: day01,
                    data_vencimento_final: day27
                },
                json: true,
                jar: 'JAR'
                };

                request(options, function (error, response, body) {
                if (error) throw new Error(error);

                return resolve(body);
            });
        }
  });

}



module.exports.METOD5 = async function (associado, KEY){
    return new Promise((resolve, reject) => {

        if(DATETODAY == day28 || DATETODAY == day29 || DATETODAY == day30 || DATETODAY == day31){
            const MSG       = 'None'  
            return resolve(MSG);

        }else if(DATETODAY >= day01 && DATETODAY <= day27 ){
                
                const jar       = request.jar();
                jar.setCookie(request.cookie(process.env.COOKIE), process.env.ASSOCIADOS);
            
                const options = {
                method: 'POST',
                url: process.env.ASSOCIADOS,
                headers: {
                    'User-Agent': process.env.USERAGENT,
                    Authorization: `Bearer ${KEY}`
                },
                body: {
                    codigo_associado: associado.toString(),
                    codigo_situacao_boleto: '999',
                    data_vencimento_inicial: day01,
                    data_vencimento_final: day27
                },
                json: true,
                jar: 'JAR'
                };

                request(options, function (error, response, body) {
                if (error) throw new Error(error);

                return resolve(body);
            });
        }
  });

}




module.exports.PAGAMENTOUPDATE = async function (nosso_numero, KEY){


    const jar = request.jar();
    jar.setCookie(request.cookie(process.env.COOKIE), process.env.BOLETO + nosso_numero);

    const options = {
    method: 'GET',
    url: process.env.BOLETO + nosso_numero,
    headers: {
        'User-Agent': process.env.USERAGENT,
        Authorization: `Bearer ${KEY}`
    },
    jar: 'JAR'
    };


    request(options, function (error, response, body) {
       if (error) throw new Error(error);
       const data           = JSON.parse(body)
       const DATEPAYORIGEM  = new Date(data.data_vencimento_original).toLocaleDateString('en-GB');



       return new Promise((resolve, reject) => {
        
        if(DATEPAYORIGEM >= day05 && DATEPAYORIGEM <= day15){

            if(DATETODAY >= day05 && DATETODAY <= day15){

                const jar       = request.jar();
                jar.setCookie(request.cookie(process.env.COOKIE), process.env.VENCIMENTO);
            
                const options = {
                method: 'POST',
                url: process.env.VENCIMENTO,
                headers: {
                    'User-Agent': process.env.USERAGENT,
                    Authorization: `Bearer ${KEY}`
                },
                body: {
                    nosso_numero: nosso_numero.toString(),
                    nova_data_vencimento: DATETODAY
                },
                    json: true,
                    jar: 'JAR'
                };

                request(options, function (error, response, body) {
                if (error) throw new Error(error);

                return resolve(body);
            });
            }else{
                return resolve("None");
            }

        }else if(DATEPAYORIGEM >= day20 && DATEPAYORIGEM <= day27){


            if(DATETODAY >= day20 && DATETODAY <= day27){
                const jar       = request.jar();
                jar.setCookie(request.cookie(process.env.COOKIE), process.env.VENCIMENTO);
            
                const options = {
                method: 'POST',
                url: process.env.VENCIMENTO,
                headers: {
                    'User-Agent': process.env.USERAGENT,
                    Authorization: `Bearer ${KEY}`
                },
                body: {
                    nosso_numero: nosso_numero.toString(),
                    nova_data_vencimento: DATETODAY
                },
                    json: true,
                    jar: 'JAR'
                };

                request(options, function (error, response, body) {
                if (error) throw new Error(error);

                return resolve(body);
            });
        }else{
                return resolve("None");
        }}});});

 
}




module.exports.PAGAMENTO = async function (nosso_numero, KEY){
    return new Promise((resolve, reject) => {
        

        const jar = request.jar();
        jar.setCookie(request.cookie(process.env.COOKIE), process.env.BOLETO + nosso_numero);

        const options = {
        method: 'GET',
        url: process.env.BOLETO + nosso_numero,
        headers: {
            'User-Agent': process.env.USERAGENT,
            Authorization: `Bearer ${KEY}`
        },
        jar: 'JAR'
        };

        request(options, function (error, response, body) {
           if (error) throw new Error(error);
        
           const data = JSON.parse(body)
        return resolve(data);
        });

  });

}
