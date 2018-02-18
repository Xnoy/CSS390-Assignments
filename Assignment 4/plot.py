"""
Name: Cameron Padua
Class: CSS390
Assignment 4: Website Monitoring
Description: Plot. This script is used to create a graph of the collected
data. This program will only create a graph for 1 minute intervals

"""
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, default="collected.tsv",
                    help="The file to read the data from. Default = collected.tsv")
options= parser.parse_args()

fileName = options.file

f = open(fileName, 'r')
f2 = open('graph.tsv', 'w')

#store fence post value
previousLine = str()

line = f.readline()
dataPast = line.split("\t")
count = 1

#store values to add to graph in new file
while line:
    currentData = line.split("\t")
    if int(currentData[0]) - int(dataPast[0]) >= 60:
        f2.write(str(count)+"\t")
        count += 1
        for x in range(4):
            f2.write(str((int(currentData[x])-int(dataPast[x]))/60)+"\t")
        f2.write("\n")
        dataPast = line.split("\t")
    previousLine = line
    line = f.readline()
    currentData = line.split("\t")

currentData = previousLine.split("\t")
#adding fencepost if it exists
if currentData != dataPast:
    f2.write(str(count) + "\t")
    divideVal = int(currentData[0]) - int(dataPast[0])
    for x in range(4):
        f2.write(
            str((int(currentData[x]) - int(dataPast[x])) / divideVal) + "\t")
f.close()
f2.close()

#using GNUplot
bashCommand = "gnuplot plot.plt"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

f = open("graph.png", 'w')

#creation of the graph.png
for line in output:
    f.write(line)
f.close()

#remove temporary file
bashCommand = "rm graph.tsv"
process = subprocess.Popen(bashCommand.split(), stdout=None)
output, error = process.communicate()
