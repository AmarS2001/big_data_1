#!/usr/bin/env python3

from operator import itemgetter
import sys

curr_key = None
curr_count = 0
key = None


for line in sys.stdin:
	line = line.strip()
	key, count = line.split('\t', 1)
	try:
		count = int(count)
	except ValueError:
		continue
	
	
	if curr_key == key:
		curr_count += count
	else:
		if curr_key:
			print('%s %s' % (int(curr_key), curr_count))
			
		curr_count = count
		curr_key = key

if curr_key == key:
	print('%s %s' % (int(curr_key), curr_count))



