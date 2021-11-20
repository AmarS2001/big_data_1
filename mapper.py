#!/usr/bin/env python3

import sys
import datetime
import requests 
import json


start_lat= float(sys.argv[1])
start_lng=float(sys.argv[2])
D=float( sys.argv[3])

for line in sys.stdin:
	data=json.loads(line.strip().replace("nan","NaN"))
	try:
		c_lat= float(data['Start_Lat'])
		c_lng= float(data['Start_Lng'])
		d= ( (c_lat - start_lat)**2 +   (c_lng-start_lng)**2  )**(1/2)
		if D>d and c_lat != None and c_lng != None:
			ans=requests.post('http://20.185.44.219:5000/',json = {'latitude':  c_lat , 'longitude': c_lng } )
			city= json.loads(ans.text)
			print('%s,%s,%s' %(city['state'],city['city'],1))
	
	except Exception as error:
		pass






