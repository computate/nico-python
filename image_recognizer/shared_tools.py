import rembg
from PIL import Image, ImageChops, ImageOps
import cv2
import os
import numpy
from matplotlib import pyplot
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow
import json
import argparse
import shutil

def trim(input_image):
    bg = Image.new(input_image.mode, input_image.size, input_image.getpixel((0,0)))
    diff = ImageChops.difference(input_image, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return input_image.crop(bbox)
    else:
        return input_image

def process_image(original_image_path):
    print("    Removing Backround...")
    output_image = rembg.remove(Image.open(original_image_path))
    print("    Trimming image...")
    output_image = trim(output_image)
    print("    Making the image B&W, Scaling the image, and adding padding...")
    output_image = numpy.array(ImageOps.pad(output_image, (28, 28), color=(0,0,0,255)))
    output_image = cv2.cvtColor(cv2.cvtColor(output_image, cv2.COLOR_BGRA2BGR), cv2.COLOR_BGR2GRAY)
    return output_image

