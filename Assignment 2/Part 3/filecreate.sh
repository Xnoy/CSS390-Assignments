#!/bin/bash

#Author: Cameron Padua
#Class: CSS390
#Professor: Morris Bernstein
#Assignment #1: File Management Part 2
#Date: 10/22/17

#change directory to second passed in variable
cd "$2";

#the number of duplicate files to be created
same=$(($1/20))

#create X amount of files (minus the same variable) of 1MB based on passed in variable
for((file = 1; file <= ($1 - same); file++))
do
	name=$(printf "%04d.file" "$file")
	dd if=/dev/urandom of=$name bs=1024 count=1024 status=none
done

#creates same amount of duplicate files by copying the files already created and call them copyXXXX.file
for((num = 1; num <= same; num++))
do	
	name=$(printf "%04d.file" "$num")
	dup=$(printf "copy%04d.file" "$num")
	cp $name $dup
done
