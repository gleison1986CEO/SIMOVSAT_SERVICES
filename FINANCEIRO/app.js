const HINOVACONN           = require("./moduloFinanceiro/hinova");
const CONNECTION           = require("./moduloFinanceiro/whats");
const CPFVERIFY            = require("./moduloFinanceiro/cpf");
const CONN                 = require("./moduloFinanceiro/conn");
const USERS                = require("./moduloFinanceiro/users");
const BOLETO               = require("./moduloFinanceiro/boleto");
const TIMER                = require("./moduloFinanceiro/timer");
const EMAIL                = require("./moduloFinanceiro/email");
const LOGS                 = require("./log/logs");
var express                = require('express');
var request                = require('request');
var bodyParser             = require('body-parser');
var api                    = express();
const fs                   = require('node:fs');
const cors                 = require('cors');



api.use(cors());
api.use(bodyParser.json());



///CLIENTES CONNECTION
///CLIENTES CONNECTION     
  
var client            = CONNECTION.CLIENTE();
CONNECTION.QR(client); 
CONNECTION.READY(client);


const DATETODAY = new Date().toLocaleDateString('en-GB');
var d = new Date(); 
var x = 5;
const dates    = d.setDate(d.getDate() + x);
var FIVEDAYS = new Date(dates).toLocaleDateString("en-GB")

const month = DATETODAY.split('/')[1];
const year  = DATETODAY.split('/')[2];


// DATAS
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



client.on('message', async (msg) => {
        
        LOGS.LOGS(msg.body);
        if (

            // VERIFICANDO MENSAGEM
            msg.body == 'boleto'  || 
            msg.body == 'fatura'  ||
            msg.body == 'fazer pagamento'  ||
            msg.body == 'Fazer pagamento'  ||
            msg.body == 'Segunda via'  ||
            msg.body == 'segunda via'  ||
            msg.body == 'Segunda Via'  ||
            msg.body == 'boletos' ||
            msg.body == 'Não consigo' ||
            msg.body == 'não consigo' ||
            msg.body == 'financeiros' ||
            msg.body == 'Financeiros' ||
            msg.body == 'BOLETO' || 
            msg.body == 'Boleto' || 
            msg.body == 'Boletos' ||
            msg.body == 'Quero boleto'   || 
            msg.body == 'Quero Boleto'   || 
            msg.body == 'quero boleto'   || 
            msg.body == 'meu boleto'     ||
            msg.body == 'boletos'        ||
            msg.body == 'boa tarde'      ||
            msg.body == 'Boa Tarde'      ||
            msg.body == 'Boa Noite'      ||
            msg.body == 'Bom Dia'        ||
            msg.body == 'boa noite'      ||
            msg.body == 'bom dia'        ||
            msg.body == 'io'             ||
            msg.body == 'Oi'  ||
            msg.body == 'OI'  ||
            msg.body == 'oi'  ||
            msg.body == 'Ola' ||
            msg.body == 'ola' ||
            msg.body == 'suporte' ||
            msg.body == 'Suporte' ||
            msg.body == 'Financeiro' ||
            msg.body == 'financeiro' ||
            msg.body == 'Olá!' ||
            msg.body == 'Olá' ||

            // INCLUDES STRING

            msg.body.includes('boleto')  || 
            msg.body.includes('Boleto')  || 
            msg.body.includes('fatura')  || 
            msg.body.includes('Fatura')  || 
            msg.body.includes('fazer pagamento')  ||
            msg.body.includes('Fazer pagamento') ||
            msg.body .includes( 'Segunda via')  ||
            msg.body.includes('segunda via')  ||
            msg.body.includes('Segunda Via')  ||
            msg.body.includes('2º Via')  ||
            msg.body.includes('boletos') ||
            msg.body.includes('Não consigo') ||
            msg.body.includes('não consigo') ||
            msg.body.includes('financeiros') ||
            msg.body.includes('Financeiros') ||
            msg.body.includes('BOLETO') || 
            msg.body.includes('Boleto') || 
            msg.body.includes('Boletos') ||
            msg.body.includes('Quero boleto')   || 
            msg.body.includes('Quero Boleto')   || 
            msg.body.includes('quero boleto')   || 
            msg.body.includes('meu boleto')     ||
            msg.body.includes('boletos')        ||
            msg.body.includes('boa tarde')      ||
            msg.body.includes('Boa Tarde')      ||
            msg.body.includes('Boa Noite')      ||
            msg.body.includes('Bom Dia')        ||
            msg.body.includes('boa noite')      ||
            msg.body.includes('bom dia')        ||
            msg.body.includes('io')             ||
            msg.body.includes('Oi')  ||
            msg.body.includes('OI')  ||
            msg.body.includes('oi')  ||
            msg.body.includes('Ola') ||
            msg.body.includes('ola') ||
            msg.body.includes('suporte') ||
            msg.body.includes('Suporte') ||
            msg.body.includes('Financeiro') ||
            msg.body.includes('financeiro') ||
            msg.body.includes('financeiros') ||
            msg.body.includes('pagar') ||
            msg.body.includes('Pagar') ||
            msg.body.includes('Olá!') ||
            msg.body.includes('Olá')) {
            await msg.reply("Olá! Tudo bem? Nós somos a Somatto Proteção Veicular\n\nPara verificarmos o financeiro\n\n*Porfavor digite o seu *cpf/cnpj**\n*OBS:sem hífen, espaço ou pontos* \n")
        
        }
         
        else if(isNaN(msg.body) == false && msg.body.length > 10 && msg.body.length < 15){ 

            const KEY       = await HINOVACONN.HINOVA()
            const users     = await USERS.DATA(msg.body, KEY)
            const usersData = JSON.parse(users)

            if(users.length > 1200){
                try{

                    await msg.reply(`Olá! estamos analisando as informações do *cpf/cnpj*.\nCarregando... aguarde.`)
                    await TIMER.TIMER();
                    const mgs = await Users(msg.body, KEY);
                    await msg.reply(`${mgs}`)
                    
                }catch(e){
                    await TIMER.TIMER();
                    await msg.reply("Erro ao consultar, tente novamente\nEstamos à disposição para ajudar!\nhttps://somatto.org.br/")
                }
            }else if(users.length < 1200){
                await msg.reply("Olá! Tudo bem? Nós somos a Somatto Proteção Veicular.\nNão encontramos o seu *boleto* neste *cpf/cnpj* em nosso sistema\nPor favor, entre em contato conosco por telefone para resolvermos essa questão\nEstamos à disposição para ajudar!\nhttps://somatto.org.br/")
            }
        }else if(isNaN(msg.body) == false && msg.body.length > 10 && msg.body.length < 15){ 
            await msg.reply("Digite apenas números do seu *cpf/cnpj*\nobs:sem hífen,espaço ou pontos")
        }
            

        
    }

    
);



async function getSecondPart(str) {
    const after   = await str.split('"codigo_associado":')[1];
    const before  = await after.split(',"telefone_fixo":')[0];
    return before;
}

async function getArrayNumber(arr){
    const count = arr.length;
    return count;
}



async function sendMessage(str) {

    // REQUESTE: CAMPOS PARA ANALISE

    // {
    //     codigo_associado: 7798,
    //     nome_associado: 'YURI TADEU PIMENTEL RODRIGUES',
    //     cpf_associado: '144.649.397-08',
    //     email: 'tadeuyuri83@gmil.com',
    //     codigo_situacao_associado: '1',
    //     descricao_situacao_associado: 'ATIVO',
    //     codigo_regional_associado: '9',
    //     nome_regional_associado: 'SOMATTO RESENDE',
    //     codigo_boleto: '183577',
    //     nosso_numero: 166175,
    //     codigo_situacao_boleto: '2',
    //     descricao_situacao_boleto: 'ABERTO',
    //     codigo_regional_boleto: '9',
    //     nome_regional_boleto: 'SOMATTO RESENDE',
    //     mes_referente: '06/2024',
    //     data_emissao: '2024-07-08',
    //     data_vencimento_original: '2024-07-22',
    //     data_vencimento: '2024-07-15',
    //     valor_boleto: '204.95',
    //     data_pagamento: null,
    //     valor_pagamento: '0.00',
    //     data_credito_banco: null,
    //     descricao_forma_pagamento: 'NAO INFORMADO',
    //     descricao_tipo_baixa_boleto: null,
    //     parcela_paga: 0,
    //     qtde_parcela_carne: 0,
    //     descricao_tipo_cobranca_recorrente: 'BOLETO / CARNÊ',
    //     codigo_tipo_boleto: 5,
    //     descricao_tipo_boleto: 'FECHAMENTO',
    //     codigo_conta: '6',
    //     codigo_banco: '2000',
    //     nome_banco: 'HINOVA PAY',
    //     agencia_bancaria: '0',
    //     conta_bancaria: '0',
    //     linha_digitavel: '34191.09206 40658.420936 75008.900005 1 97780000020495',
    //     link_boleto: 'https://short.hinova.com.br/v2/VXrwq58v.pdf',
    //     short_link: 'https://short.hinova.com.br/v2/VXrwq58v.pdf',
    //     pix: { qrcode: null, copia_cola: null },
    //     veiculos: [
    //       {
    //         codigo_veiculo: 9217,
    //         placa: 'KWO7D65',
    //         chassi: '9BHBG41DAFP328197',
    //         valor_fixo: '0.00',
    //         codigo_situacao_veiculo: 1,
    //         descricao_situacao_veicul: 'ATIVO',
    //         codigo_tipo_veiculo: '2',
    //         descricao_tipo_veiculo: 'AUTOMOVEL',
    //         codigo_modelo: '6339',
    //         descricao_modelo: 'HB20S C.PLUS/C.STYLE1.0 FLEX 12V MEC. 4P',
    //         valor_fipe: '49957.00',
    //         codigo_vencimento_veiculo: '15',
    //         dia_vencimento_veiculo: '22',
    //         codigo_tipo_envio_boleto: 3,
    //         descricao_tipo_envio_boleto: 'ENVIO POR E-MAIL',
    //         codigo_cooperativa_veiculo: '47',
    //         nome_cooperativa_veiculo: 'QUIVIA FEITOSA'
    //       }
    //     ]
    //   }



    

    // INSTÂNCIAS

    const DATEPAY        = new Date(str.data_vencimento).toLocaleDateString('en-GB');
    const DATEPAYORIGEM  = new Date(str.data_vencimento_original).toLocaleDateString('en-GB');
    const data_vencimento= str.data_vencimento;
    const ass_email      = str.email;
    const nome_associado = str.nome_associado;
    const cpf_associado  = str.cpf_associado;
    const descricao_situacao_boleto = str.descricao_situacao_boleto;
    const valor_pagamento= str.valor_boleto;
    const linha_digitavel= str.linha_digitavel;
    const link_boleto    = str.link_boleto;
    const short_link     = str.short_link;
    const placa          = str.placa;

    const DATAORIGINAL   = new Date(str.data_vencimento_original);
    var x = 5;
    const dates_new      = DATAORIGINAL.setDate(DATAORIGINAL.getDate() + x);
    const FIVEDAYS_OUT   = new Date(dates_new).toLocaleDateString("en-GB")
    
    if(DATETODAY > FIVEDAYS_OUT){

        const msg                = `Olá! ${nome_associado}\nNão conseguimos gerar o seu boleto no momento, porfavor tente novamente!.\nOu entre em contato conosco pelo telefone (21) 3024-1647 ou pelo WhatsApp (21) 99566-1473.`
        LOGS.LOGS(msg);
        return msg;
    
    }else{

        try{
    
            const msg            = `Olá! ${nome_associado}\n\nInformamos os dados do seu boleto para pagamento:\n\n -*linha digitável:* ${linha_digitavel} \n -*link de pagamento:* ${link_boleto} \n -*valor:* ${valor_pagamento} \n -**cpf/cnpj*:* ${cpf_associado}\n\nLembre-se: boletos em aberto após o vencimento deixarão o veículo descoberto.\n\n*Caso ja tenha pago,desconsidere essa mensagem*\n\nEstamos à disposição para ajudar!\n\nAcesse nosso site: [somatto.org.br](https://somatto.org.br/)`
            LOGS.LOGS(msg);
            return msg;
        
        }catch(ex){
            
            const msg           = `Olá! ${nome_associado}\nNão conseguimos gerar o seu boleto no momento, porfavor tente novamente!.\nOu entre em contato conosco pelo telefone (21) 3024-1647 ou pelo WhatsApp (21) 99566-1473.`
            LOGS.LOGS(msg);
            return msg;
        }        

    }

}



// {
//     "codigo_situacaoboleto": "1",
//     "descricao": "BAIXADO",
//     "pago": "SIM"
// },
// {
//     "codigo_situacaoboleto": "2",
//     "descricao": "ABERTO",
//     "pago": "NÃO"
// },
// {
//     "codigo_situacaoboleto": "3",
//     "descricao": "CANCELADO",
//     "pago": "NÃO"
// },
// {
//     "codigo_situacaoboleto": "4",
//     "descricao": "BAIXADO C\/ PENDÊNCIA",
//     "pago": "SIM"
// },
// {
//     "codigo_situacaoboleto": "999",
//     "descricao": "EXCLUIDO",
//     "pago": "NÃO"
// }


async function Users(cpf,KEY){
    const users     = await USERS.DATA(cpf, KEY)
        
        try{    
             
                const associado = await getSecondPart(users)
                const getBoleto = await BOLETO.METOD2(associado, KEY)


                if(getBoleto   == 'None'){

                    const sendMSG   = await sendMessage(getBoleto)
                    return sendMSG

                }else{

                    const getArray  = await getArrayNumber(getBoleto)
                    const getNossoNumero  = getBoleto[getArray - 1]["nosso_numero"]
                    await BOLETO.PAGAMENTOUPDATE(getNossoNumero, KEY)
                    const getPagamento    = await BOLETO.PAGAMENTO(getNossoNumero, KEY)
    
                    const sendMSG   = await sendMessage(getPagamento)
                    return sendMSG
                }
     
            
            }catch(e){

                try{
       
                    const associado = await getSecondPart(users);
                    const getBoleto = await BOLETO.METOD3(associado, KEY)


                    if(getBoleto   == 'None'){

                        const sendMSG   = await sendMessage(getBoleto)
                        return sendMSG

                    }else{

                        const getArray  = await getArrayNumber(getBoleto)
                        const getNossoNumero = getBoleto[getArray - 1]["nosso_numero"]
                        await BOLETO.PAGAMENTOUPDATE(getNossoNumero, KEY)
                        const getPagamento   = await BOLETO.PAGAMENTO(getNossoNumero, KEY)
                    
                        const sendMSG   = await sendMessage(getPagamento)
                        const date      = new Date();
                        return sendMSG
                    }
                    
                  

                }catch(e){

                    try{
                        const associado = await getSecondPart(users);
                        const getBoleto = await BOLETO.METOD1(associado, KEY)


                        if(getBoleto   == 'None'){

                            const sendMSG   = await sendMessage(getBoleto)
                            return sendMSG
    
                        }else{
                            const getArray       = await getArrayNumber(getBoleto)
                            const getNossoNumero = getBoleto[getArray - 1]["nosso_numero"]
                            await BOLETO.PAGAMENTOUPDATE(getNossoNumero, KEY)
                            const getPagamento   = await BOLETO.PAGAMENTO(getNossoNumero, KEY)
                        
                            const sendMSG   = await sendMessage(getPagamento)
                            const date      = new Date();
                            return sendMSG
                        }


                    } catch(e){

                        try{
                            const associado = await getSecondPart(users);
                            const getBoleto = await BOLETO.METOD4(associado, KEY)


                            if(getBoleto   == 'None'){

                                const sendMSG   = await sendMessage(getBoleto)
                                return sendMSG
        
                            }else{
                                const getArray  = await getArrayNumber(getBoleto)
                                const getNossoNumero = getBoleto[getArray - 1]["nosso_numero"]
                                await BOLETO.PAGAMENTOUPDATE(getNossoNumero, KEY)
                                const getPagamento   = await BOLETO.PAGAMENTO(getNossoNumero, KEY)
                            
                                const sendMSG   = await sendMessage(getPagamento)
                                const date      = new Date();
                                return sendMSG
                            }

                        }catch(e){
                            try{
                                
                                const associado = await getSecondPart(users);
                                const getBoleto = await BOLETO.METOD5(associado, KEY)


                                if(getBoleto   == 'None'){

                                    const sendMSG   = await sendMessage(getBoleto)
                                    return sendMSG
            
                                }else{
                                    const getArray  = await getArrayNumber(getBoleto)
                                    const getNossoNumero = getBoleto[getArray - 1]["nosso_numero"]
                                    await BOLETO.PAGAMENTOUPDATE(getNossoNumero, KEY)
                                    const getPagamento   = await BOLETO.PAGAMENTO(getNossoNumero, KEY)
                    
                                    const sendMSG   = await sendMessage(getPagamento)
                                    const date      = new Date();
                                    return sendMSG
                                }

                            }catch(e){
                                const msg = `Não encontramos o seu *boleto* neste *cpf/cnpj* em nosso sistema\nPor favor, entre em contato conosco por telefone para resolvermos essa questão\nEstamos à disposição para ajudar!\nhttps://somatto.org.br/`
                                LOGS.LOGS(msg);
                                return msg
                            }
                       
                    }
                }

            }
}}

// SCANNER QRCODE
process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 0;
api.get('/qrcode', (req, res) => {

    fs.readFile('datalog/qr.json', 'utf8', (err, data) => {
    if (err) {
        console.error('none', err);
        return;
    }

        var jsonObject  = JSON.parse(data);
        var Qr          = jsonObject[0]["qrcode"].toString();

        if(Qr.includes('2@')){
           res.json(jsonObject);
        }else{
           
            fs.readFile('datalog/none.json', 'utf8', (err, data) => {   
            var jsonObject  = JSON.parse(data);                 
            res.json(jsonObject);
           })
        }
        
        
    });
    
});

// BOLETOS REGRAS PYTHON

api.post('/boletos', async (req, res)  => {
        
        await TIMER.TIMER();
        const data = await req.body;

        if(data != null){
            console.log(data)
            // const number = "+5521965408033";
            const number = data.whatsapp;

            if(data.descricao == "VISTORIA"){        // APENAS ENVIADO QUANDO BOLETO PASSOU DA DATA
                    
                const text   =`Olá! ${data.nome_associado}\n\nNós somos a Somatto Proteção Veicular\n\n -*Você precisa passar pela vistoria* \n\ndados do usuario: \n\n*cpf/cnpj*: ${data.cpf_associado}\ntelefone: ${data.whatsapp}\n\n*Caso ja tenha pago,desconsidere essa mensagem*\n\nEstamos à disposição para ajudar!\n\nAcesse nosso site: [somatto.org.br](https://somatto.org.br/) `;
                const chatId = number.substring(1) + "@c.us";
                client.sendMessage(chatId, text);

            }else if(data.descricao == "BOLETO"){   // APENAS ENVIADO QUANDO BOLETO ESTA PENDENTE NA DATA
                
                const text   =`Olá! ${data.nome_associado}\nInformamos os dados do seu boleto para pagamento:\n\n-*linha digitável*: ${data.linha_digitavel}\n-*link de pagamento*: ${data.link_boleto}\n-*valor*: ${data.valor_boleto}\n-*vencimento*: ${data.vencimento}\n-**cpf/cnpj**: ${data.cpf_associado}\n\nLembre-se: boletos em aberto após o vencimento deixarão o veículo descoberto.\n\n*Caso ja tenha pago,desconsidere essa mensagem*\n\nEstamos à disposição para ajudar!\n\nAcesse nosso site: [somatto.org.br](https://somatto.org.br/) `;
                const chatId = number.substring(1) + "@c.us";
                client.sendMessage(chatId, text);

            }else if(data.descricao == "ERROR"){  // APENAS ENVIADO QUANDO CLIENTE QUESTIONA O BOLETO POR MENSAGEM NO WHATSAPP FLAG: MARKETING

                const text   =`Olá! Tudo bem? Nós somos a Somatto Proteção Veicular\n\nNão encontramos o seu BOLETO neste *cpf/cnpj* em nosso sistema\nPor favor, entre em contato conosco por telefone para resolvermos essa questão\nEstamos à disposição para ajudar!\n\nAcesse nosso site: [somatto.org.br](https://somatto.org.br/) `
                const chatId = number.substring(1) + "@c.us";
                client.sendMessage(chatId, text);

            }
        }
        res.send({
            message: data,
        });
        return  data;

        });




// ROTATIVIDADE DO MICROSERVIÇO PYTHON PORTANDO NESSE ENPOINT A CADA 24 HORAS
// ROTATIVIDADE DO MICROSERVIÇO PYTHON PORTANDO NESSE ENPOINT A CADA 24 HORAS    

client.initialize();
api.listen(80,function() {console.log('SERVIDOR ATISE ASSIST INICIALIZANDO NA PORTA :: 8000.');});


