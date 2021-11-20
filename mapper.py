#!/usr/bin/env python3

import sys
import datetime
import json



desc_rule = ["lane blocked", "shoulder blocked", "overturned vehicle"]
weather_rule = ["Heavy Snow", "Thunderstorm","Heavy Rain", "Heavy Rain Showers", "Blowing Dust"]

format = ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M:%S.%f")



def weat_match(string, weather_rule):
    for sub in weather_rule:
        if string == sub:
            return True
    return False


def desc_match(string, desc_rule):
    string = string.lower()
    for i in desc_rule:
        if i in string:
            return True
    return False




def main():
    for line in sys.stdin:
        line = json.loads(line)
        start = line["Start_Time"][0:23]
        for fmt in format:
            try:
                time = datetime.datetime.strptime(start, fmt)
                break
            except ValueError:
                continue

        try:
            if ((line["Severity"] >= 2.0) and (line["Sunrise_Sunset"] == "Night") and (line["Visibility(mi)"] <= 10.0)
                and (line["Precipitation(in)"] >= 0.2) and (desc_match(line["Description"], desc_rule))
                    and (weat_match(line["Weather_Condition"], weather_rule))):
                value = 1
                #print('%s	%s'%(time.hour,value))
                if len(str(time.hour))==1:
                	print('0%s	%s'%(time.hour,value))
                else:
                	print('%s	%s'%(time.hour,value))
                
                

        except Exception as e:
            continue

main()

