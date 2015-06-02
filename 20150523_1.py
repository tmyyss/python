#!/usr/bin/python
#http://www.oschina.net/code/snippet_1186210_48252

import requests
from bs4 import BeautifulSoup
BASE_URL='http://hkbici.com/'
LOGIN_URL='http://hkbici.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
FORM_DATA={'fastloginfield':'username','username':'studytest','password':'1qaz0plm','quickforward':'yes','handlekey':'1s'}
TEST_URL='http://hkbici.com/forum-217-1.html'
try:
	r=requests.get(LOGIN_URL,params=FORM_DATA)
	if 'alert_error' in r.content:
		print "Username or password incorrect!"
	else:
		print "Login success!"
		print r.cookies['Ovo6_2132_auth']
except requests.exceptions.ConnectionError,e:
	print "requests.exceptions.ConnectionError:%s"%e

r=requests.get(TEST_URL)
soup=BeautifulSoup(r.content)
for div in soup.find_all('div',class_='c cl'):
	pageurl=BASE_URL+div.find('a')['href']
