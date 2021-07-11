#!/bin/bash
# convert a video to a set of png files, one per frame
ffmpeg -i "%1" ./frames/frame-%04d.png
