#!/bin/bash

# Check arg(s)
if [ "$#" -ne 1 ]; then
	echo "Missing/Extra Arguments: pngs_to_jpgs.sh src_dir"
	exit 1
fi

# Convert
for i in `find "$1" -name "*.png" -type f -maxdepth 1`; do
	echo ""
    echo "$i -> ${i%.png}.jpg"
    ffmpeg -i "$i" -preset veryslow ${i%.png}.jpg  # veryslow => less loss
done