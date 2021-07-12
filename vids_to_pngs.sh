#!/bin/bash

merged_file='merged.mp4'
temp_file='temp-files.txt'
png_dir='./png_frames'


# Check arg(s)
if [ "$#" -ne 1 ]; then
	echo "Missing/Extra Arguments: vids_to_png.sh src_dir"
	exit 1
fi


# Find what video encoding to use as input (.mov, .mp4, ...)
extensions=`find "$1" -type f | awk -F. '!a[$NF]++{print $NF}'`
if [ `echo $extensions | wc -w` -ne 1 ]; then
	echo "Not all files have the same extension type:"
	echo $extensions
	exit 1
else
	ext=`echo $extensions | head -n1`
	ext=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
	echo Detected input video type: $ext
fi


# Get filepaths into temp_file
find "$1" -maxdepth 1 -type f | sort > $temp_file
sed -i -e 's/^/file /' $temp_file


# Merge to single .mp4 file
echo
echo MERGING TO ONE MP4 FILE...
if [ $ext -eq "mp4" ]; then
    # mp4 is easy 
	ffmpeg -f concat -i $temp_file -c copy $merged_file
else
	ffmpeg -safe 0 -f concat -i $temp_file -vcodec copy -acodec aac -strict -2 -b:a 384k $merged_file
fi
rm $temp_file


# Convert merged .mp4 file into directory of .png file, one per frame
echo
echo CONVERTING TO PNG FILES...
if [ -d "$png_dir" ]; then
	read -p "Directory '$png_dir' already exists. Overwrite? [y/N] " -n 1 -r
	echo    # (optional) move to a new line
	if [[ $REPLY =~ ^[Yy]$ ]]; then
		rm -r $png_dir
    else
    	exit 1
    fi
fi
mkdir -p $png_dir
ffmpeg -i $merged_file ./$png_dir/frame-%05d.png

# and done
echo
echo DONE.
echo CREATED `ls $png_dir | wc -l` PNG FILES @ $png_dir



