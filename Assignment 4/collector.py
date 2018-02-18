"""
Name: Cameron Padua
Class: CSS390
Assignment 4: Website Monitoring
Description: Collector. This script to used to scrape the server for the
current count of 200s, 500s, and 404 errors. After pulling this data it will
store these values in a TSV file call collected. The user has the option to
change the interval at which data is collected, the URL to collect from,
and the number of times to repeat the interval.
"""

import urllib2
import time
import argparse
#Command line arguement parser to get the URL, interval, and repeat values
parser = argparse.ArgumentParser()
parser.add_argument("--url", "-u", type=str, default="http://localhost:8080",
                    help="The URL that you want to collect from. Default = "
                         "http://localhost:8080")
parser.add_argument("--interval", "-i", type=int, default=10,
                    help="The interval you want to collect data at in "
                         "seconds. Default = 10 seconds")
parser.add_argument("--repeat", "-r", type=int, default=-1,
                    help="The number of times you want to repeat the "
                         "interval. Default = -1 (forever)")
options = parser.parse_args()

url = options.url
interval = options.interval
repeat = options.repeat

outputData = open('collected.tsv', 'w')
count = 1

#The first While loop will repeat until count is equal to the repeat value.
# Otherwise this program will loop forever.
if repeat > 0:
    while True:
        response = urllib2.urlopen(url + "/stats")
        html = response.read()
        values = html.split("\n")
        del values[-1]
        for var in values:
            value = var.split(":")
            outputData.write(value[1].strip() + "\t")
        outputData.write("\n")
        if repeat == count:
            break
        else:
            count+=1
            time.sleep(interval)
else:
    while True:
        response = urllib2.urlopen(url + "/stats")
        html = response.read()
        values = html.split("\n")
        del values[-1]
        for var in values:
            value = var.split(":")
            outputData.write(value[1].strip() + "\t")
        outputData.write("\n")
        time.sleep(interval)
outputData.close()
