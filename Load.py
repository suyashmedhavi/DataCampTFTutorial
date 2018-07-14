# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:14:37 2018

@author: suyash
"""

import os
import skimage.data
import matplotlib.pyplot as plt

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
    
labels,images = load_data(train_data_directory)

plt.hist(labels,62)
plt.show()

plt.close()

traffic_signs = [300, 600, 900, 1200]

for i in range(len(traffic_signs)):
    plt.subplot(1, 4, i+1)
    plt.axis('off')
    plt.imshow(images[traffic_signs[i]])
    plt.subplots_adjust(wspace=0.5)
    plt.show()
    print("shape: {0}, min: {1}, max: {2}".format(images[traffic_signs[i]].shape, 
                                                  images[traffic_signs[i]].min(), 
                                                  images[traffic_signs[i]].max()))
    
unique_labels = set(labels)
plt.figure(figsize=(15, 15))

i = 1

for label in unique_labels:
    image = images[labels.index(label)]
    plt.subplot(8, 8, i)
    plt.axis('off')
    plt.title("Label {0} ({1})".format(label, labels.count(label)))
    i += 1
    plt.imshow(image)