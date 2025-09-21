# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 22:12:45 2025

@author: Fabian Mink
"""

import numpy as np
import pyaudio
import time

f = 440.0        # sine frequency, Hz, may be float    
duration = 1   # in seconds, may be float
fs = 8000       # sampling rate, Hz, must be integer
t = 0;

def callback(in_data, frame_count, time_info, status):
    global cnt
    global t
    print(str(frame_count) + ": " + str(t))
    
    thist = np.arange(frame_count)*1/fs + t
    
    samples = (np.sin(2*np.pi*f*thist)).astype(np.float32)
    #print(samples)
    
    t = t + frame_count/fs
    
    if(t > duration):
        return (samples, pyaudio.paComplete)
    
    return (samples, pyaudio.paContinue)



# Instantiate PyAudio and initialize PortAudio system resources (2)
p = pyaudio.PyAudio()

# Open stream using callback (3)
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True,
                stream_callback=callback)

# Wait for stream to finish (4)
while stream.is_active():
    time.sleep(0.1)

# Close the stream (5)
stream.close()

# Release PortAudio system resources (6)
p.terminate()