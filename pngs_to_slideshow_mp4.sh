#!/bin/bash

# Check arg(s)
if [ "$#" -ne 2 ]; then
	echo "Missing/Extra Arguments: pngs_to_slideshow_mp4.sh rate out_file"
	exit 1
fi

# Create
ffmpeg -r "$1" -pattern_type glob -i '*.png' -c:v libx264 -vf fps=25 -pix_fmt yuv420p "$2"