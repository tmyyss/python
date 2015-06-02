#!/usr/bin/python
import time

birthday=(2014,8,18,18,0,0,0,0,0)
birthday=time.mktime(birthday)
now=time.time()
delta=now-birthday
days=int(delta/(24*60*60))
print("darling is %s days"%days)
