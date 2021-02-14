cd
git clone https://github.com/RiversideRocks/AbuseIPDB-cli
cd ~/AbuseIPDB-cli
touch tokens.ini
echo "[Config]" >> tokens.ini
echo "key=$1" >> tokens.ini
pip3 install -r requirements.txt
cd
echo 'alias abuseipdb="python3 ~/AbuseIPDB-cli/python.py"' >> .bashrc
bash
clear
echo "Setup done."
