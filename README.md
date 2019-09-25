# VideoKutter

Simple kutter of Video Clips.

# How it works ?

VideoKutter is a python script which allows you to easily split a video into serveral parts.

# Options

- --file = Input video
- --prefix = The prefix used for the output files (By default, it's the input file's name)
- --duration = The time (in seconds) of an output file (By default, it's 120 seconds)
- --start = The second from which the process has to start (By default, it's 0)
- --output = Directory used to store the output files (By default, it's "output")

# Example

To split a video into several parts of 2 minutes, we can use the following command :  
`python videocutter --file=my_video.mp4 --duration=120`  
The result will be several files like :

- my_video Part 1.mp4
- my_video Part 2.mp4
- my_video Part 3.mp4

# Update v1

Now, you can pass an input directory instead of a single file.
