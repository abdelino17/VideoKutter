"""
 *
 * @Author: abdelino17
 * @Date: 2019-03-15 03:49:38
 * @LastUpdate: 2019-09-25 10:51:10
 *
"""
from moviepy.editor import VideoFileClip
import pathlib
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default="input")
parser.add_argument('--prefix', type=str, default="")
parser.add_argument('--duration', type=int, default=120)
parser.add_argument('--start', type=int, default=0)
parser.add_argument('--output', type=str, default="output")
args = parser.parse_args()

DIR = args.dir

args_prefix = args.prefix
args_duration = args.duration
args_start = args.start
args_output = args.output

def create_file(input_path):
    PREFIX = args_prefix
    START = args_start
    SUBCLIP_DURATION = args_duration
    OUTPUT_DIR = args_output

    video = VideoFileClip(input_path)
    total_duration = video.duration
    number_parts = int(total_duration / SUBCLIP_DURATION)

    if number_parts > 0:
        if not PREFIX:
            PREFIX = video.filename.split(os.sep)[-1].split(".")[0]
        pathlib.Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True) 
        output_path = OUTPUT_DIR + os.sep + PREFIX.title() + " Part "
        for i in range(1, number_parts+1):
            subclip = video.subclip(START, START + SUBCLIP_DURATION)
            START += SUBCLIP_DURATION
            subclip.write_videofile(output_path + str(i) + ".mp4")

        subclip = video.subclip(START)
        subclip.write_videofile(output_path + str(number_parts+1) + ".mp4")          
    else:
        print("Operation aborted...the duration is lower than the subclip duration.")

files = os.listdir(DIR)
for file in files:
    create_file(os.path.join(DIR, file))
    print("The file was correctly kut")
    print("-----------------------------------------------------------------")