#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:06:20 2017
@author: wenyan bi
"""

# subfolders should be named like "vid_1", "vid_2", "vid_3", ...
# output video will be stored in the same folder as the frame images.

import cv2
import os
import glob
print(cv2.__version__)

# Changeble parameters:
start_vid_index = 1
end_vid_index = 66


curDir = os.getcwd()

for i in range(start_vid_index, end_vid_index):
    # subfolder prefix
    prefix = 'vid_' + str(i)
 
    os.chdir(prefix)
    tmpdir = os.getcwd()
    

    # get ".png" files
    frames = []
    for f in os.listdir(tmpdir):
        if f.endswith('png'):
            frames.append(f)
            
    frames.sort(key=lambda f1: int(filter(str.isdigit, f1)))
    
    
    # get width and shape
    frame_path = os.path.join(tmpdir, frames[0])
    frame = cv2.imread(frame_path)
    height, width, channels = frame.shape
    
    
    output = prefix + '.mov'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))
    
    for f in frames:
        frame_path = os.path.join(tmpdir, f)
        frame = cv2.imread(frame_path)
        out.write(frame)
    
    out.release()
    #cv2.destroyAllWindows()    
    os.chdir(curDir)
		