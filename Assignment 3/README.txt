Name: Cameron Padua
Class: CSS390
Assignment 3: Log Analysis
Description: This program will read in two logs converting them into 4 different dictionaries. The first two will have the Segements as the keys and the cookies as the value. The last two are the Cookies as the keys and the segments as the values. It will then compare the two like dictionaries and find keys that have missing or added values. In addition to this, it will print a header summary and all the keys that are added/missing values

To run:
python ./report-generator.py file1.log file2.log

Notes:
This script was compiled and tested in Python 2.7.12

By default, the program will print to Standard Ouput, however you can redirect it to a file.
ex: python ./report-generator.py evaluator-integration.log evaluator-integration-baseline.log > report2.txt

The script will (and needs to) take two file names from commandline arguements

The total amount of cookies includes cookies that does not any segments

This script takes ~6 mins when using evaluator-intergration.log and baseline.

sources:
https://stackoverflow.com/questions/287684/regular-expression-to-validate-hex-string
https://stackoverflow.com/questions/3462143/get-difference-between-two-lists
https://stackoverflow.com/questions/4730993/python-key-in-dict-keys-performance-for-large-dictionaries
https://stackoverflow.com/questions/6307394/removing-dictonary-entries-with-no-values-python
https://docs.python.org/2/library/re.html
http://www.pythonforbeginners.com/system/python-sys-argv
https://stackoverflow.com/questions/2907637/pythons-equivalent-of-public-static-void-main
