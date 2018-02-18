"""
Name: Cameron Padua
Class: CSS390
Assignment 3: Log Analysis
Description: This program will read in two logs converting them into 4 different dictionaries. The first two
                will have the Segements as the keys and the cookies as the value. The last two are the Cookies
                as the keys and the segments as the values. It will then compare the two like dictionaries and
                find keys that have missing or added values. In addition to this, it will print a header summary
                and all the keys that are added/missing values
"""

import re
import sys
"""
SegmentsToCookies: This method is used for creating a dictionary containing segments as the keys and cookies as the
                    values. To increase the performance, we go through the files twice to reduce the amount of actions
                    have to be done each time. The first time through will create add all the segments to the dictionary
                    with an empty list as the value. The second time through, it will add the cookies to the lists of
                    each segment key. Then we return the dictionary.
"""
def SegmentsToCookies(fileName):
    segments = dict()
    segmentRegEx = re.compile('.[0-9]+_[0-9]+')
    cookieRegEx = re.compile(':\s([A-Fa-f0-9]+)\s')

    with open(fileName, "r") as f:
        for line in f:
            if (re.search(cookieRegEx, line)):
                segmentsList = re.findall(segmentRegEx, line)
                for segment in segmentsList:
                    segments[segment] = []
        f.close()

    with open(fileName, "r") as f:
        for line in f:
            if (re.search(cookieRegEx, line)):
                cookie = re.findall(cookieRegEx, line)[0]
                segmentsList = re.findall(segmentRegEx, line)
                for segment in segmentsList:
                    segments[segment].append(cookie)
        f.close()

    return segments
"""
CookiestoSegments: This method is used for creating a dictionary containing cookies as the keys and segments as the
                    values. To increase the performance, we go through the files twice to reduce the amount of actions
                    have to be done each time. The first time through will create add all the cookies to the dictionary
                    with an empty list as the value. The second time through, it will add the segments to the lists of
                    each segment key. Then we return the dictionary.
"""
def CookiestoSegments(fileName):
    cookies = dict()
    segmentRegEx = re.compile('.[0-9]+_[0-9]+')
    cookieRegEx = re.compile(':\s([A-Fa-f0-9]+)\s')

    with open(fileName, "r") as f:
        for line in f:
            if (re.search(cookieRegEx, line)):
                cookie = re.findall(cookieRegEx, line)[0]
                cookies[cookie] = []
        f.close()

    with open(fileName, "r") as f:
        for line in f:
            if (re.search(cookieRegEx, line)):
                cookie = re.findall(cookieRegEx, line)[0]
                segmentsList = re.findall(segmentRegEx, line)
                for segment in segmentsList:
                    cookies[cookie].append(segment)
        f.close()

    return cookies
"""
addedValuesReport: This method is responsible for finding any extra values in each list when comparing two dictionaries.
                    To do this, it will convert each list into a set and subtract the test from the baseline. Then we 
                    convert the subtracted sets into a list and loop though it removing empty lists. Finally we return
                    the dictionary of extra values
"""
def addedValuesReport(testrun, baseline):
    extraValues = dict()

    for key in testrun:
        if(key in baseline):
            extraValues[key] = list(set(testrun[key]) - set(baseline[key]))
        else:
            extraValues[key] = testrun[key]

    for x in extraValues.keys():
        if extraValues[x] == []:
            del extraValues[x]

    return extraValues
"""
missingValuesReport: This method is responsible for finding any missing values in each list when comparing two 
                        dictionaries. To do this, it will convert each list into a set and subtract the baseline from 
                        the test. Then we convert the subtracted sets into a list and loop though it removing empty 
                        lists. Finally we return the dictionary of extra values
"""
def missingValuesReport(testrun, baseline):
    missingValues = dict()

    for key in baseline:
        if(key not in testrun):
            missingValues[key] = baseline[key]
        else:
            missingValues[key] = list(set(baseline[key]) - set(testrun[key]))

    for x in missingValues.keys():
        if missingValues[x] == []:
            del missingValues[x]

    return missingValues
"""
printReportSegments: This method is responsible for printing dictionaries in the following format:

                    line#   key     dictionary_Length   [dictionary values]\n

                    It will sort the keys to be in order and then iterate through the list printing the format above
"""
def printReportSegments(dict):
    line = 0
    sortedKeys = sorted(dict.keys())

    for key in sortedKeys:
        print str(line) + "\t" + key + "\t" + str(len(dict[key])) + "\t",
        print sorted(dict[key])
        line += 1

def main(args):
    testLogSC = SegmentsToCookies(sys.argv[1])
    baseLogSC = SegmentsToCookies(sys.argv[2])
    numberOfSegments = len(baseLogSC.keys())

    ec = addedValuesReport(testLogSC, baseLogSC)
    print "Segments with added cookies: " + str(len(ec.keys())) + " / " + str(numberOfSegments)
    printReportSegments(ec)
    print ""

    mc = missingValuesReport(testLogSC, baseLogSC)
    print "Segments with missing cookies: " + str(len(mc.keys())) + " / " + str(numberOfSegments)
    printReportSegments(mc)
    print ""

    testLogCS = CookiestoSegments(sys.argv[1])
    baseLogCS = CookiestoSegments(sys.argv[2])
    numberOfCookies = len(testLogCS.keys())

    aseg = addedValuesReport(testLogCS, baseLogCS)
    print "Cookies in extra segments: " + str(len(aseg.keys())) + " / " + str(numberOfCookies)
    printReportSegments(aseg)
    print ""
    mseg = missingValuesReport(testLogCS, baseLogCS)
    print "Cookies omitted from segments: " + str(len(mseg.keys())) + " / " + str(numberOfCookies)
    printReportSegments(mseg)
    print ""

if __name__ == '__main__':
    main(sys.argv)
