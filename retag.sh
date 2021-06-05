#!/bin/fish
set FILES "/mnt/c/Users/akaza/Music/LINUX/songs/*.mp3"
cd /mnt/c/Users/akaza/Music/LINUX/songs/
for file in (ls /mnt/c/Users/akaza/Music/LINUX/songs/);
	echo $file
	echo "Input artist"
	read artist
	echo "input title"
	read title
	set lastpath (basename $file)
	eyeD3 -a $artist -t $title "$lastpath";
end
