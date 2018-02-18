#!/bin/sh

#Author: Cameron Padua
#Class: CSS390
#Professor: Morris Bernstein
#Assignment #1: File Management Part 1
#Date: 10/10/17

#Go to directory of provided Music folder location
cd "$1" ; 
#Find the total tracks
echo -n 'Total Tracks: ' ; find -name "*.ogg" -type f | wc -l ; 
#Find the Total Artists
echo -n '\r\nTotal Artists: ' ; find -maxdepth 2 -mindepth 2 -printf "%f\r\n" | sort | uniq | wc -l ;
#Find all the muliti-genre artists,
echo "\r\nMulti-Genre Artists:\r" ; find -maxdepth 2 -mindepth 2 -printf "%f\r\n" | sort | uniq -d ;
#Find all the albums that have more than one disk
echo "\r\nMulti-Disk Albums:\r" ; find -maxdepth 4 -mindepth 4 -print | grep disk[[:digit:]] | cut -d/ -f4 | uniq | sort 




