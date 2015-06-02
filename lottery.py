#!/usr/bin/python

import urllib2
import re
from bs4 import BeautifulSoup

red=re.compile('red_ball')
blue=re.compile('blue_ball')
url="http://trend.lecai.com/ssq/redBaseTrend.action?recentPhase=100#chartTableWrapper"
f=urllib2.urlopen(url)
htmlsource=f.read()

soup=BeautifulSoup(htmlsource)
trs=soup('tr')
for tr in trs:
	try:
		term=tr(class_="chart_table_td",width=100)[0]
		print "The Term is:%s"%term.string
	except IndexError:
		continue
	red_balls=tr(class_=red)
	print "The red ball is:"
	for red_ball in red_balls:
		print red_ball.string,
	blue_ball=tr(class_=blue)[0]
	print "\nThe Blue ball is:%s"%blue_ball.string

		
