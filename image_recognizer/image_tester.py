import rembg
from PIL import Image, ImageChops, ImageOps
import cv2
import os
import numpy
from matplotlib import pyplot
import shared_tools
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow
import json
import argparse
import shutil
import xlwt
import guesser
if __name__ == '__main__':
    json_path = os.getenv("IMAGE_RECOGNIZER_JSON_PATH")
    json_name = "category-names.json"
    test_image_path = os.getenv("IMAGE_RECOGNIZER_TEST_PATH")
    spreadsheet_path = os.getenv("IMAGE_RECOGNIZER_SPREADSHEET_PATH")
    print("Importing the category-names.json file in \"%s/category-names.json...\""% json_path)
    with open("%s/%s"% (json_path, json_name)) as open_file:
        category_names = json.load(open_file)
    test_data = numpy.zeros([len(category_names), len(category_names)])
    print(test_data)
    for category_directory in os.scandir(test_image_path):
        if category_directory.is_dir():
            for test_image_file in os.scandir("%s/%s" % (test_image_path, category_directory.name)):
                if test_image_file.is_file():
                    print("test image: %s" % test_image_file.path)
                    processed_image = shared_tools.process_image(test_image_file.path)
                    prediction = guesser.guess(processed_image)
                    print("prediction: %s" % prediction)
                    prediction_number = numpy.argmax(prediction[0])
                    row_num = category_names.index(category_directory.name)
                    col_num = prediction_number
                    test_data[row_num][col_num] = test_data[row_num][col_num] + 1
                    print(test_data)
    print(category_names)
