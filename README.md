# deauth_attack
Tested in Kali Linux 2022.4  

## Installation
```sh
pip3 install scapy
```

## Usage
python3 deauth_attack.py <interface> <ap mac> [<station mac> [-auth]]  
ex) python3 deauth_attack.py wlan0 11:22:33:44:55:66 aa:bb:cc:dd:ee:ff
