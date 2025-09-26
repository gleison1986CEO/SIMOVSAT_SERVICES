
## SIMOVSAT & ATISE  WEBAPI

- SERVIDOR LINUX UBUNTU 22
- 167.172.144.33
---

## ENDPOINTS EXTERNO HINOVA

- https://kepler.hinova.com.br/api/sga/v2/doc/
- https://tudomaispormenos.com.br/docs/api#/
- https://sistemas.infornet.com.br/webassist/atise/ws/rest/api_v1/
- https://kepler.hinova.com.br/api/sga/v2/doc/#api-Boleto-Listar_Boleto
---

## DEPEDÊNCIAS

- sudo apt-get -y update
- sudo apt-get -y upgrade
- sudo apt-get install unzip
- wget or git clone project # donwload project
- sudo apt install python3.11
- sudo apt install python3-pip
- sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
- sudo apt-get -y install net-tools   # for IP
- ERROR? apt-get remove  python3-apt && apt-get install python3-apt
- sudo apt-get install redis-server
- redis-cli                           # commnad for see ip and port REDIS
- sudo systemctl start redis-server
 
 ---


## PM2
- sudo apt install nodejs
- sudo apt install npm
- npm install pm2@latest -g  # for server project
- pip3 install requirements.txt
- pm2 start "flask run" --exp-backoff-restart-delay=100
- pm2 start "python3 microBoleto.py" --exp-backoff-restart-delay=100
- pm2 start "python3 microBloqueio.py" --exp-backoff-restart-delay=100
- pm2 start "python3 microInfornet.py" --exp-backoff-restart-delay=100
- pm2 start "python3 microMaps.py" --exp-backoff-restart-delay=100
- pm2 start "node financeiro.js" --exp-backoff-restart-delay=100
- pm2 list, pm2 start, pm2 stop
--- 

## ENDPOINTS
- IP:5000/swagger
---

# RESPONSABILIDADES

## WHATSAPP BOT

- endpoint /boletos (onde e recebido os boletos do serviço pagamentos em classes py)
- metodo client.on recebe mensagem do usuario que necessita de um boleto onde sera consultado por cpf
---

## SERVIÇO

- classe conexa configura um endpoint que recebe dados de um formulario
- classe conexa possuyi um microserviço conectado ao infornet onde afaz a leitura de todos os usuários e envia caso nao exista para a conexa
- extraclasse boleto      -> tras os boletos da hinova 
- extraclasse cooperativa -> tras todas as cooperativas da hinova
- extraclasse infornet    -> tras todos os usuarios da infornet
- extraclasse pacientes   -> publica os pacientes que nao existem na conexa
- extraclasse produto     -> tras todos os produtos relacionados aos usuarios
- extraclasse regionais   -> tras todasas regionais
- extraclasse situação    -> tras todas as situações
- extraclasse usuarios    -> tras todos os usuarios hinova
- extraclasse veiculos    -> tras todos os veiculos hinova
- extraclasse voluntarios -> tras todos os voluntarios hinova
- classejobs data -> faz um select no banco de dados simovsat compara com hinova para gerar dados de mapas locais dos veiculos
- classe conexa   -> recebe so dados da conexa
- classe conn     -> conecta os bancos de dados como sqlserver e mysql(simovsat)
- classe data     -> send data to mysql se usuario ou veiculo9s nao existirem
- classe hinova   -> trata os dados da hinova entre usuarios veiculos e outros
- classe infornet -> insere dados pacientes conexa e clube de vantagens
- classe key      -> gerar uma chave hinova
- classe locationMovida -> gerar link para mapa pela movida
- classe logs     -> cria logs de cada funcionalidade existente
- classe movida   -> insere link do mapa para simovsat no banco de dados sharing
- classe pagamentos -> verificar e envia boletos hinova  para clientes somatto e simovsat
- classe redis    -> redis salva  historico
- classe save     -> save, update, mysql
- classe sendmessagem -> envia mensagem para whatsapp
- classe time         -> pega data e hora atual para reduzir e adcionar dias e horas.
- classe tratamento   -> trata todos os dados mediante aos dados da hinova, simovsat, conexa e outros
- classe verification -> verificar cpf e verifica cnpj e verifica telefones
- repository Insert   -> insere tudo na base de dados sqlserver para (futuro painel admin)
---

## API

- "status": True,
- "/spec"                         : "swagger version api",
- "/movida_generate_link/<placa>" : "GENERATE LINK WITH MAP",
- "/movida_cerca"                 : "CERCA",
- "/movida_result/<placa>"        : "GET LOCATION USER BY PLATE",
- "/usuarios_importadas"          : "GET USERS IMPORTED",
- "/veiculos_importados"          : "GET VEHICLES IMPORTED",
- "/veiculos_cooperativa/ativos/<codigo_cooperativa>"         : "GET VEHICLES /ATIVOS BY COOPERATIVA ID",
- "/veiculos_regional/ativos/<codigo_regional>"               : "GET VEHICLES /ATIVOS BY REGIONAL ID",
- "/veiculos_situacao/ativos/<codigo_situaca>"                : "GET VEHICLES /ATIVOS BY SITUACAO ID",
- "/veiculos_cooperativa/inadimplentes/<codigo_cooperativa>"  : "GET VEHICLES /INADIMPLENTES BY COOPERATIVA ID",
- "/veiculos_regional/inadimplentes/<codigo_regional>"        : "GET VEHICLES /INADIMPLENTES BY REGIONAL ID",
- "/veiculos_situacao/inadimplentes/<codigo_situaca>"         : "GET VEHICLES /INADIMPLENTES BY SITUACAO ID",
- "/veiculos_cooperativa/inativos/<codigo_cooperativa>"       : "GET VEHICLES /INATIVOS BY COOPERATIVA ID",
- "/veiculos_regional/inativos/<codigo_regional>"             : "GET VEHICLES /INATIVOS BY REGIONAL ID",
- "/veiculos_situacao/inativos/<codigo_situaca>"              : "GET VEHICLES /INATIVOS BY SITUACAO ID",
- "/regionais_todas"              : "GET REGIONAIS",
- "/cooperativas_todas"           : "GET COOPERATIVAS",
- "/voluntarios_todas"            : "GET VOLUNTARIOS",
- "/produtos_todas"               : "GET PRODUTOS",
- "/situacao_todas"               : "GET SITUAÇÕES",
- "/placas_inativos/<placa>"      : "GET PLATES INATIVOS SIMOVSAT",
- "/placas_inativos_hinova/<placa>" :  "GET PLATES INATIVOS HINOVA",
- "/placas_inadimplentes/<placa>" :    "GET PLATES INA. SIMOVSAT",
- "/placas_inadimplentes_hinova/<placa>" : "GET PLATES INA. HINOVA",
- "/placas_ativas/<placa>"        : "GET ACTIVE PLATES SIMOVSAT",
- "/placas_ativas_hinova/<placa>" : "GET ACTIVE PLATES HINOVA",
- "/hinova_result/<uid>"          : "GET RESULTS HINOVA",
- "/usuarios"                     : "POST USERS TO IMPORT",
- "/veiculos_filter"              : "POST VEHICLES WITH FILTER",
- "/veiculos_filter_import"       : "POST VEHICLES TO IMPORT WITH FILTER",
- "/situacao"                     : "POST TO GENERATE SITUATIONS",
- "/produto"                      : "POST TO GENERATE PRODUTOS",
- "/voluntarios"                  : "POST TO GENERATE VOLUNTARIOS",
- "/cooperativa"                  : "POST TO GENERATE COOPERATIVAS",
- "/regionais"                    : "POST TO GENERATE REGIONAIS",
- "/pacientes"                    : "POST TO CONEXAAPP",
- "/boletos"                      : "POST TO BOLETOS",
- "profile":"JESUS É FIEL",
- "developer":"GLEISON SILVEIRA DE FREITAS"
---

## WHASTAPP JS SOLUTION
- whatsapp js 1.24.0
- npm install github:pedroslopez/whatsapp-web.js#webpack-exodus
- const wwebVersion = '2.2412.54';
- https://raw.githubusercontent.com/wppconnect-team/wa-version/main/html/${wwebVersion}.html