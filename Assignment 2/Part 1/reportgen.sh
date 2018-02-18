#!/bin/bash

#Author: Cameron Padua
#Class: CSS390
#Professor: Morris Bernstein
#Assignment #1: File Management Part 2
#Date: 10/22/17

#change directory to arguement
cd "$1"

#get an array of all artists in the Directory, assumes the Assigment 1 directory paths
mapfile -t allArtist < <(find -maxdepth 2 -mindepth 2 -print |
 cut -d/ -f3 |
 sort |
 uniq);

 #creates headings of HTML file and sends to standard out
echo -e "<html>\r\n<body>\r\n<table border=\"1\">\r\n"
echo -e "\t<tr>\r\n" 
echo -e "\t\t<th>Artist</th>\r\n" 
echo -e "\t\t<th>Album</th>\r\n"
echo -e "\t</tr>\r\n" 

for artist in "${allArtist[@]}"
do
	#get an array of all albums by an artist
	mapfile -t albums < <(find -type d |
		 grep [/]"$artist" |
		 cut -d/ -f4 |
		 sort |
		 uniq) 
	
	for((album = 1; album < ${#albums[@]}; album++))
	do
		#add intial <tr> with tabs and newlines
		echo -e "\t<tr>\r\n" 
		
		#if it is the first row of an artist
		if [ $album -eq 1 ] ; then
			#create the number of rows (for each album) and add the artist, 
			#ie add <td rowspan="#">artist</td> with tabs and newlines
			printf "\t\t<td rowspan=\"%s\">%s</td>\r\n" $(expr ${#albums[@]} - 1) "$artist" 
		fi
		
		#else
		#add the album to the current row, ie add the <td>album</td> with tabs and newlines
		printf "\t\t<td>%s</td>\r\n" "${albums[$album]}" 		
		
		#add the ending table HTML tags
		#ie </tr> with tabs and newlines
		echo -e "\t</tr>\r\n"
	done
done

#add end of body HTML tags
#ie </table>
#	</body> with tabs and newlines
echo -e "</table>\r\n</body>"
