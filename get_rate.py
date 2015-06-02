#!/usr/bin/python

from bs4 import BeautifulSoup
from  opener import getRandomOpener

map_dict={"yuebao":["https://financeprod.alipay.com/fund/index.htm","sevenRate"],
	"baifa":["http://8.baidu.com/",".channel-item"],
	"baitiao":["http://jr.jd.com/xjk/index.htm",'.half-box'],}

for name,item in map_dict.items():
	print name,item
	f=getRandomOpener().open(item[0])
	htmlsource=f.read()
	soup=BeautifulSoup(htmlsource)
	if item[1].startswith('.'):
		content=soup.select(item[1])[0]
	else:
		content=soup.find_all(id=item[1])[0]
	print name
	print content.text


