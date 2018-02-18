#!/bin/bash

#Author: Cameron Padua
#Class: CSS390
#Professor: Morris Bernstein
#Assignment #1: File Management Part 2
#Date: 10/22/17

#current directory of this script
loc="$(pwd)"

#location of the temporary folder to be created
filecreationLoc="$loc"/TestLocation
#make temporary folder
mkdir "$filecreationLoc"

#create 50 to 1000 files (increasing by 50 each time) 
#and run the time command each time on the dupdetec script
for((file = 50; file <= 1000; file = file + 50))
do	
	#creating the files at the specified location
	"$loc"/filecreate.sh $file "$filecreationLoc"
	
	#time how long it takes for dupdetec to run and save the results in time.tsv
	/usr/bin/time -f "$file\t%E" -o time.tsv -a "$loc"/dupdetec.sh "$filecreationLoc"
done

#delete temporary files directory
rm -r "$filecreationLoc"
