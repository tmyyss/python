#!/usr/bin/python

import cookielib,urllib,urllib2

login='ismellbacon123@yahoo.com'
password='login'

cookiejar=cookielib.CookieJar()
urlOpener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))

values={'login':login,'password':password}
data=urllib.urlencode(values)
request=urllib2.Request("http://www.imdb.com/register/login", data)
url=urlOpener.open(request)
page=url.read(500000)
print cookiejar
if not 'id' in [cookie.name for cookie in cookiejar]:
	raise ValueError,"Login failed with login=%s,password=%s"%(login,password)

print "we are logged in !"

url=urlOpen.open("http://imdb.com/find?s=all&q=grave")
page=url.read(200000)
