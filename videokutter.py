"""
 *
 * @Author: abdelino17
 * @Date: 2019-03-15 03:49:38 
 *
"""
from moviepy.editor import VideoFileClip
import pathlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str)
parser.add_argument('--prefix', type=str, default="")
parser.add_argument('--duration', type=int, default=120)
parser.add_argument('--start', type=int, default=0)
parser.add_argument('--output', type=str, default="output")
args = parser.parse_args()

PATH = args.file
PREFIX = args.prefix
SUBCLIP_DURATION = args.duration
START = args.start
OUTPUT_DIR = args.output

video = VideoFileClip(PATH)
total_duration = video.duration
number_parts = int(total_duration / SUBCLIP_DURATION)

if number_parts > 0:
    if not PREFIX:
        PREFIX = video.filename.split(".")[0]
    pathlib.Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True) 
    output_path = OUTPUT_DIR + "/" + PREFIX.title() + " Part "
    for i in range(1, number_parts+1):
        subclip = video.subclip(START, START + SUBCLIP_DURATION)
        START += SUBCLIP_DURATION
        subclip.write_videofile(output_path + str(i) + ".mp4")

    subclip = video.subclip(START)
    subclip.write_videofile(output_path + str(number_parts+1) + ".mp4")          
else:
    print("Operation aborted...the duration is lower than the subclip duration.")
