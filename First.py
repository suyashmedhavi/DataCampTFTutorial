# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:21:32 2018

@author: suyash
"""

import tensorflow as tf

x1=tf.constant([1,2,3])
x2=tf.constant([4,5,6])

result=tf.multiply(x1,x2)

sess=tf.Session()
print(sess.run(result))
sess.close()    

with tf.Session() as sess:
    print(sess.run(result))