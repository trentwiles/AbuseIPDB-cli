cd
git clone https://github.com/RiversideRocks/AbuseIPDB-cli
cd ~/AbuseIPDB-cli
echo "[Config]" > tokens.ini
echo "key=$1"
pip3 install -r requirements.txt
alias abuseipdb="python3 ~/AbuseIPDB/python.py"
