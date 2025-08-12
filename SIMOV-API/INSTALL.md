# INSTALL API AND SERVICES ATISE
## API ATISE ASSIST 
---
## ATUALIZAÇÃO SERVIDOR
- apt-get update
- apt-get upgrade
---
---
## SQLSERVER
- wget https://packages.microsoft.com/keys/microsoft.asc -O /etc/apt/keyrings/mssql2022.key 
- wget https://packages.microsoft.com/config/ubuntu/22.04/mssql-server-2022.list -O /etc/apt/sources.list.d/mssql-server-2022.list 
- nano /etc/apt/sources.list.d/mssql-server-2022.list 
---

## ADD LINES
- deb [signed-by=/etc/apt/keyrings/mssql2022.key arch=amd64,armhf,arm64] https://packages.microsoft.com/ubuntu/22.04/mssql-server-2022 jammy main
- nano /etc/apt/sources.list.d/msprod.list 
- deb [signed-by=/etc/apt/keyrings/mssql2022.key arch=amd64,armhf,arm64] https://packages.microsoft.com/ubuntu/22.04/prod jammy main
---

## CONTINUE INSTALATION
-  apt update 
-  apt -y install mssql-server mssql-tools unixodbc-dev 

## CONFIGURE SQLSERVER
- /opt/mssql/bin/mssql-conf setup
- 3) Express (free) 
---

## VERIFY SQLSERVER RUNNING
- systemctl status mssql-server 
---

## CONFIGURE TOOLS
- echo 'export PATH=$PATH:/opt/mssql-tools/bin' > /etc/profile.d/mssql.sh 
- source /etc/profile.d/mssql.sh 
---