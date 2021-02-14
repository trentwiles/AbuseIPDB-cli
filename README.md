# AbuseIPDB-cli
Improved + fixed CLI for AbuseIPDB. Inspired by [this project](https://github.com/dnhckt/abuseipdb-cli).

## Screenshot + Demo
https://flag.riverside.rocks/watch/1707832457

![](https://cdn.riverside.rocks/a/begonia-aerosteon-girdle.png)

## Setup

Create an AbuseIPDB account and make an API key on the "API" tab. Copy the key to your clipboard. Run the following code in a Linux terminal with Python 3 and Pip 3 installed:

```
curl -s https://github.com/RiversideRocks/AbuseIPDB-cli/blob/main/setup.sh > setup.sh
bash setup.sh YOUR_API_KEY_HERE
```

(replace YOUR_API_KEY_HERE with your API key)

Run the script with `abuseipdb IP`.
