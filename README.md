# image-object-filter
image/video object-filtering scripts built on ffmpeg and ImageAI.

### Use Case: Find Particular Objects in a Timelapse Video
1. Use `vid_frames_to_png.sh` to break a video into individual `.png` files, one per frame
2. Grab a RetinaNet model file, like [this one](https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5/)
3. Run `filter.py --objects person sports_ball --dir MY_TIMELAPSE_PNGS_DIR` (see `-h` for help)
   - This will produce JSON files that contain the filenames of the images with your object(s)
