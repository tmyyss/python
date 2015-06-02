#!/usr/bin/python
#!-*-encoding:utf-8-*-

import scrapy
from job.items import JobItem

class JobSpider(scrapy.Spider):
	name='zhaopin'
	allowed_domains=['zhaopin.com']
	start_urls=[
		'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E5%B7%9E&kw=python&sm=0&p=1',
	]
	def parse(self,response):
		for sel in response.xpath("//table[@class='newlist']"):
			for title in sel.xpath("./tr/td[@class='zwmc']/div/a/text()[1]").extract():
				print "****************************************************************************"
				print "职位:",title
			for wg in sel.xpath("./tr/td[@class='zwyx']/text()").extract():
				print "薪资:",wg
			for wz in sel.xpath("./tr/td[@class='gzdd']/text()").extract():
				print "工作地点:",wz
			for detail in sel.xpath("./tr[@class='newlist_tr_detail']/td/div/div/ul/li/text()").extract():
				print "工作描述:",detail
	
