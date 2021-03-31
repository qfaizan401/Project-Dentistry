# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 13:50:43 2021

@author: rehan.qureshi
"""
from skimage import io, measure, img_as_ubyte
from skimage.filters import threshold_multiotsu
from skimage.color import label2rgb, rgb2gray
from skimage.segmentation import clear_border
import numpy as np
import matplotlib.pyplot as plt

class Dental ():
    def __init__(self, input_data):
        self.input_data = input_data
        
    def image_input(self):
        img = io.imread(self.input_data, as_gray=True)
        
    def image_preprocessing(self):
        