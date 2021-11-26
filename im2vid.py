# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 11:24:49 2021

@author: z004ac7x
"""
import argparse
import os
import moviepy.video.io.ImageSequenceClip

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help="path to images")
    parser.add_argument("--name",default="test.mp4", type=str, help="name of the video file")
    parser.add_argument("--format", default = '.jpg', help= "format of image, default is .jpg")
    parser.add_argument("--fps", default =30, type=int, help="frames per second")
    args = parser.parse_args()

def im2vid(image_path, name, image_format, fps):
    image_folder=image_path
    fps=30
    
    image_files = [os.path.join(image_folder,img)
                   for img in os.listdir(image_folder)
                   if img.endswith(image_format)]
    image_files = sorted(image_files)
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(name, codec="libx264")

im2vid(args.path, args.name, args.format, args.fps)