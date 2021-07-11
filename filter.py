"""Reads a collection of images and places those with an object in a directory."""

from imageai.Detection import ObjectDetection
import os
import argparse
import json


# Get Inputs
parser = argparse.ArgumentParser()
parser.add_argument(
    "--objects", help="the object(s) to look for", nargs="+", required=True
)
parser.add_argument("--dir", help="the dir of images to parse", required=True)
parser.add_argument(
    "--model", help="the model path", default="resnet50_coco_best_v2.1.0.h5"
)
args = parser.parse_args()
print(args)


# Setup
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(args.model)
detector.loadModel()
custom = detector.CustomObjects(
    **{obj: True for obj in args.objects}  # Ex: person=True, sports_ball=True, ...
)
print(custom)
print()

# Look at each image
file_results = {}
for image in os.listdir(args.dir):
    if not any(image.endswith(ext) for ext in [".png", ".jpeg", ".jpg"]):
        continue
    print()
    print(image)

    detected_image_array, detections = detector.detectObjectsFromImage(
        custom_objects=custom,
        output_type="array",
        input_image=os.path.join(args.dir, image),
    )

    file_results[image] = detections
    print(detections)
print()
print(file_results)
json.dump(file_results, open("files.results.json", "w"))
print()

# Filter
for obj in args.objects:
    print(obj + ":")
    files_with_object = {}
    for fname, results in file_results.items():
        for res in results:
            if res["name"] == obj:
                files_with_object[fname] = res["percentage_probability"]
                break
    print(files_with_object)
    json.dump(files_with_object, open(f"files.{obj}.object.json", "w"))

# Empty Images
files_with_nothing = []
print("files with nothing:")
for fname, results in file_results.items():
    if not results:
        files_with_nothing.append(fname)
print(files_with_nothing)
json.dump(files_with_nothing, open(f"files.no.object.json", "w"))
