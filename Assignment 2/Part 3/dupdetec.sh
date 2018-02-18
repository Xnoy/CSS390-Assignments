#!/bin/bash

#Author: Cameron Padua
#Class: CSS390
#Professor: Morris Bernstein
#Assignment #1: File Management Part 2
#Date: 10/22/17

#change to directory that was passed in
cd "$1";

#an array of Files in the current Directory
mapfile -t Files < <(find -type f)

#Number of files in directory, also when to stop the loops
end=${#Files[@]}

#O(n^2) loop starting at the first and comparing through all of them besides the ones before it
for((file = 0; file < end; file++))
	do
	for((next = $(expr $file + 1); next < end; next++))
		do
		#if the files are different
		if ( cmp -s "${Files[$file]}" "${Files[$next]}" ); then
			#shows matched output and mathcing files without path names
			echo "matched" $(basename "${Files[$file]}") $(basename "${Files[$next]}")
		else
			true
		fi	
	done
done
