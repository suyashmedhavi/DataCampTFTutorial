# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:14:37 2018

@author: suyash
"""

import tensorflow as tf
import os
import skimage.data

ROOT_PATH = 'C:/Users/suyas/Documents/GitHub/DataCampTFTutorial/Data'
train_data_directory = os.path.join(ROOT_PATH,'Training')
test_data_directory = os.path.join(ROOT_PATH,'Testing')

def load_data(data_directory):
    directories = [ d for d in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory,d)) ]
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory,d)
        file_names = [os.path.join(label_directory,f) for f in os.listdir(label_directory) if f.endswith('.ppm')]
        for f in file_names:
            labels.append(int(d))
            images.append(skimage.data.imread(f))
    return labels,images
    
labels,images = load_data(test_data_directory)