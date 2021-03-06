"""Move each image listed in a JSON file to a new directory."""

import os
import shutil
import argparse
import json


# Get Inputs
parser = argparse.ArgumentParser()
parser.add_argument("--json", help="the json file of images", required=True)
parser.add_argument("--src", help="the source directory", required=True)
parser.add_argument("--dest", help="the destination directory", required=True)
parser.add_argument(
    "--copy", help="copy image files instead of moving", action="store_true"
)
args = parser.parse_args()
print(args)


# Get Files
file = []
data = json.load(open(args.json, "r"))
if isinstance(data, list):
    files = data
elif isinstance(data, dict):
    files = list(data.keys())
else:
    raise Exception(f"File has unsupported data (list or dict only) {args.json}")
print(files)


# Move Files
os.mkdir(args.dest)
for file in files:
    src = os.path.abspath(os.path.join(args.src, file))
    print(file)
    dest = os.path.abspath(os.path.join(args.dest, file))
    try:
        if args.copy:
            shutil.copy(src, dest)
        else:
            shutil.move(src, dest)
    except FileNotFoundError:
        continue
