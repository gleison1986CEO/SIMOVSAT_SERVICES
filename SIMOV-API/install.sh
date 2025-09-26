##BASH CODE INSTALL API

##### MICROSOFT TOOLS 18
if ! [[ "18.04 20.04 22.04 23.04" == *"$(lsb_release -rs)"* ]];
then
    echo "Ubuntu $(lsb_release -rs) is not currently supported.";
    exit;
fi

curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc

curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
##### MICROSOFT TOOLS 18

sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
sleep 2
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18
echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
source ~/.bashrc
sudo apt-get install -y unixodbc-dev
sleep 5
sudo apt install python3.11
sleep 2
sudo apt install python3-pip
sleep 2
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
sleep 2
sudo apt-get -y install net-tools
sleep 2
sudo apt-get install redis-server
redis-cli
sudo systemctl start redis-server
sleep 3
sudo apt install nodejs
sleep 3
sudo apt install npm
sleep 2
npm install pm2@latest -g
pip3 install -r requirements.txt
sleep 2
pm2 start "flask run" --exp-backoff-restart-delay=100
pm2 start "python3 microBoleto.py" --exp-backoff-restart-delay=100
pm2 start "python3 microBloqueio.py" --exp-backoff-restart-delay=100
pm2 start "python3 microInfornet.py" --exp-backoff-restart-delay=100
pm2 start "python3 microMaps.py" --exp-backoff-restart-delay=100
pm2 start "node financeiro.js" --exp-backoff-restart-delay=100