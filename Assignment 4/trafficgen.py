"""
Name: Cameron Padua
Class: CSS390
Assignment 4: Website Monitoring
Description: Traffic Generator. This script is meant to generate traffic to
a server at a port of the users choosing. It is mean to simulate traffic to
a website. In this simulation, it can generate 200s, 500s, and 404 errors.
At the very least, this program can generate 500 requests per second.

"""

import urllib2
import random
import time
import argparse


#Command line arguement parser for URL, RPS, and Jitter
parser = argparse.ArgumentParser()
parser.add_argument("--url", "-u", type=str, default="http://localhost:8080",
                    help="The URL that you want to hit. Default = http://localhost:8080")
rps = parser.add_argument("--rps", "-r", type=int, default=500,
                          help="The rate you want to hit the URL. Default = 500")
parser.add_argument("--jitter", "-j", type=float, default=.02,
                    help="Floating-point number in the range of [0..1]  "
                         "representing the shakiness of the rate. Default = .02")
options = parser.parse_args()

url = options.url
rps = options.rps
jitter = options.jitter
#Range of RPS rate
requestRateLow = int(float(rps) * (1 - jitter))
requestRateHigh = int(float(rps) * (1 + jitter))

#Traffic Generation
while True:
    rate = random.randint(requestRateLow, requestRateHigh)
    ServerError = random.randint(0, 500)
    start = time.time()
    for x in xrange(rate):
        if ServerError % 205 == 1:
            try:
                urllib2.urlopen(urllib2.Request(url + "/fail"))
            except urllib2.HTTPError:
                pass
        elif x % 71 == 1:
            try:
                urllib2.urlopen(urllib2.Request(url + "/404"))
            except urllib2.HTTPError:
                pass
        else:
            urllib2.urlopen(urllib2.Request(url))

    end = time.time()

    #If generating output did not take a second, wait 1/100th of a second
    # and recheck.
    while True:
        if end - start >= 1:
            break
        time.sleep(.01)
        end = time.time()
