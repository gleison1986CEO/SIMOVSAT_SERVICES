const { Client, LocalAuth} = require('whatsapp-web.js');
const EMAIL                = require("./email");
const QRCODE               = require('qrcode')
const LOGS                 = require("../log/logs");


module.exports.CLIENTE = function (){
    const wwebVersion = '2.2412.54';
    const client = new Client({ 
        webVersionCache: {
            type: 'remote',
            remotePath: `https://raw.githubusercontent.com/wppconnect-team/wa-version/main/html/${wwebVersion}.html`,
        },
        puppeteer: { 
            headless: true,
            args: ['--no-sandbox', '--disable-setuid-sandbox']}, 
            authStrategy: new LocalAuth() })
    return client;
}


module.exports.QR = async function(client){
        


        client.on('qr', (qr) => {
            if(qr){

                QRCODE.toString( qr , 
                    {type:'terminal', width: 50,height: 50, scale: 2}, 
                    function (err, url) {
                    LOGS.LOGS(qr);
                    console.log("#########");
                    console.log(qr);
                    console.log("#########");
                })
        
            }else{
                const msg = "SEU WHATSAPP JÁ ESTÁ ESCANEADO, E ESTÁ FUNCIONANDO CORRETAMENTE! \nFIQUE ATENTO AS ATUALIZAÇÕES DO WHATSAPP OBRIGADO!😀"
                LOGS.LOGS(msg);
                console.log("#########");
                console.log(qr);
                console.log("#########");                
                //EMAIL.EMAIL(msg);
            }
     
    })
       
 

    

}




module.exports.READY = function (client){
    client.on('ready', () => {
        const mess = "SEU WHATSAPP JÁ ESTÁ ESCANEADO, E ESTÁ FUNCIONANDO CORRETAMENTE! \nFIQUE ATENTO AS ATUALIZAÇÕES DO WHATSAPP OBRIGADO!😀"
        LOGS.LOGS("TESTE! CONECTADO WHATSAPP!");
        EMAIL.EMAIL(mess);
        return mess;
    });
}


