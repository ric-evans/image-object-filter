# image-object-filter
Image/video object-filtering scripts built on ffmpeg and ImageAI.

### Use Case: Find Particular Objects in a Timelapse Video
1. Use `vids_to_pngs.sh` to collectively break video files into individual `.png` files, one per frame, at `png_frames/`
   - This will also intermittently create a single `.mp4` file of the merged videos
2. Grab a RetinaNet model file, like [this one](https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5/)
3. Run `filter.py --objects person sports_ball --dir ./png_frames` (see `-h` for help)
   - This will produce JSON files that contain the filenames of the images with your object(s)
