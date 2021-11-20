#!/usr/bin/env python3

import sys 


prs_city = None
prs_state = None

prs_city_cnt = 0
prs_state_cnt= 0

for inputs in sys.stdin:
	data = inputs.strip()
	data=data.split(",")
	
	if prs_state != data[0]:
		if prs_state != None:
			print(prs_city, prs_city_cnt)
			print(prs_state, prs_state_cnt + prs_city_cnt)
			prs_state_cnt = 0
			prs_city = None
		prs_state = data[0]
		print(prs_state)
		
	if prs_city == None:
		prs_city_cnt = 0
		prs_city = data[1]
		
		
	if prs_city == data[1]:
		prs_city_cnt = prs_city_cnt + int(data[2])
	
	else:
		print(prs_city,prs_city_cnt)
		prs_state_cnt = prs_state_cnt + prs_city_cnt
		prs_city = data[1]
		prs_city_cnt = int(data[2])

print(prs_city,prs_city_cnt)

print(prs_state,prs_state_cnt + prs_city_cnt)
		


	
	
