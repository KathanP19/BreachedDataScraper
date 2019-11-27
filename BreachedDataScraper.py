import os
import sys
import requests
from googlesearch import search


R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m' # white

version = '1.0a'

def banner():
	os.system('clear')
	banner = ""
	print(G + banner + W + '\n')
	print(G + '[+] ' + R + 'Author          ' + G + 'Hacker Destination')
	print(G + '[+] ' + R + 'Update          ' + G + 'Haroon Awan')
	print(G + '[+] ' + R + 'Script          ' + G + 'Search illegal, stolen, breached data in private nodes, darkweb, internet, end-to-end channels')
	print(G + '[+] ' + R + 'Start Engine    ' + G + 'OK')
	print(G + '[+] ' + R + 'Ver             ' + G + version)
    
   	


def cardpwn():
	urls = []
	qlist = []
	total_url = []
	paste_sites = ['pastespot.com/search?q=', 'pastespot.com', 'cl1p.net', 'dpaste', 'slexy', 'slexy.org', 'dumpz.org', 'hastebin', 'ideone', 'pastebin', 'pw.fabian-fingerle.de','gist.github.com','https://www.heypasteit.com/','ivpaste.com','mysticpaste.com','paste.org.ru','paste2.org','sebsauvage.net/paste/','slexy.org','squadedit.com','wklej.se','textsnip.com']
	card = input(G + '[+] ' + R +'Enter Search    ' + W)
	try:
		val = card
		if len((val)) >= 1 and len((val)) <= 30:
			for site in paste_sites:
				query = '{} {}'.format(site, card)
				qlist.append(query)
			for entry in qlist:
				for url in search(entry, pause=2.0, stop=20, user_agent='Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'):
					urls.append(url)

			print('\n' + G + '[>]' + R + ' Getting Dumps...' + W + '\n')
			for item in urls:
				for site in paste_sites:
					if '{}'.format(site) in item:
						print(G + '[+] ' + C + item + W)
						total_url.append(item)

		else:
			print('\n' + R + '[!] ' + G + 'Invalid Search ' + W + '\n')
			return cardpwn()
		total = len(total_url)
		if total == 0:
			print (R + '[-] No Data Leaks' + W + '\n')
		else:
			print('\n' + G + '[+]' + R + ' Total Dumps Found : ' + W + str(total) + '\n')

	except ValueError:
		print('\n' + R + '[!] Invaild Search' + W + '\n')


def network():
	try:
		requests.get('https://github.com/', timeout = 5)
		print ('' + G + '[!]' + R + ' Script Status  ' + W, end = '')
		print (G + ' Online ' + W + '\n')
	except requests.ConnectionError:
		print (R + '[!]' + R + ' Offline' + W)
		sys.exit()

try:
	banner()
	network()
	cardpwn()
except KeyboardInterrupt:
	print ('\n' + R + '[!]' + R + ' Keyboard Interrupt Called' + W)
	exit()
