var nodemailer = require('nodemailer');
const LOGS     = require("../log/logs");

module.exports.EMAIL = function (QRCODE){

    var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
        user: 'devgleisonsilveira@gmail.com',
        pass: 'vttc aida yzft xopm'
        }
    });
    
    var mailOptions = {
        from: 'devgleisonsilveira@gmail.com',
        to: 'devgleisonsilveira@gmail.com',
        subject: 'WHATSAPP FINANCEIRO::SOMATTO',
        text: 'CONFIRA O WHASTAPP::SOMATTO',
        html: '<p><h1><strong>' + QRCODE.toString() +'</strong></h1></p><p>😀</p>'
    };
    
    transporter.sendMail(mailOptions, function(error, info){
        if (error) {
            LOGS.LOGS(error)
            console.log(error);
        } else {
        LOGS.LOGS('EMAIL ENVIADO: ' + QRCODE.toString())
        }
    }); 
    return cpf.isNumber();
}
// EMAIL



module.exports.CONSULTA = function (msg, ass_email){

    var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
        user: 'devgleisonsilveira@gmail.com',
        pass: 'dugm jjhq wvbb jxmo'
        }
    });
    
    var mailOptions = {
        from: 'devgleisonsilveira@gmail.com',
        to: 'devgleisonsilveira@gmail.com,' + ass_email.toString() + '',
        subject: 'SOLICITAÇÃO DE BOLETO',
        text: msg.toString(),
    };
    
    transporter.sendMail(mailOptions, function(error, info){
        if (error) {
            LOGS.LOGS(error)
            console.log(error);
        } else {
            LOGS.LOGS('EMAIL ENVIADO: ' + msg.toString())
        }
    }); 
    return cpf.isNumber();
}
// EMAIL




module.exports.CONSULTASEMBOLETO = function (msg){

    var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
        user: 'devgleisonsilveira@gmail.com',
        pass: 'dugm jjhq wvbb jxmo'
        }
    });
    
    var mailOptions = {
        from: 'devgleisonsilveira@gmail.com',
        to: 'devgleisonsilveira@gmail.com',
        subject: 'PROBLEMAS AO SOLICITAR O BOLETO SOMATTO',
        text: msg.toString(),
    };
    
    transporter.sendMail(mailOptions, function(error, info){
        if (error) {
            LOGS.LOGS(error)
            console.log(error);
        } else {
            LOGS.LOGS('EMAIL ENVIADO: ' + msg.toString())
        }
    }); 
    return cpf.isNumber();
}
// EMAIL



module.exports.TOKEN = function (token){

    var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
        user: 'devgleisonsilveira@gmail.com',
        pass: 'dugm jjhq wvbb jxmo'
        }
    });
    
    var mailOptions = {
        from: 'devgleisonsilveira@gmail.com',
        to: 'devgleisonsilveira@gmail.com',
        subject: 'SOLICITAÇÃO DE TOKEN SOMATTO',
        text: 'Uma nova solicitação de token foi realizada.\n' + token.toString(),
    };
    
    transporter.sendMail(mailOptions, function(error, info){
        if (error) {
            LOGS.LOGS(error)
            console.log(error);
        } else {
            LOGS.LOGS('EMAIL ENVIADO: ' + token.toString())
        }
    }); 
    return cpf.isNumber();
}
// EMAIL
