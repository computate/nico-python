import rembg
from PIL import Image, ImageChops, ImageOps
import cv2
import os
import numpy
from matplotlib import pyplot
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow
import json
import pyfiglet
import shared_tools

webcam_path = '/home/ntate/Pictures/Webcam'
model_path = "/home/ntate/AIML/model"
json_path = "/home/ntate/AIML/json"
json_name = "category-names.json"

print("Loading the Model in \"%s\" (This will take a few seconds...)"% model_path)
model = tensorflow.keras.models.load_model(model_path)

def guess(output_image):
    print("Importing the category-names.json file in \"%s/category-names.json...\""% json_path)
    print("Doin' some other stuff...")
    output_image2 = output_image / 255.0
    output_image2 = (numpy.expand_dims(output_image2, 0))
    print("\n        Predicting!\n")
    prediction = model.predict(output_image2)
    return prediction

if __name__ == '__main__':
    while True:
        print("\n\nFinding out the most recent image in %s..." % webcam_path)
        most_recent_file = None
        most_recent_time = 0
        for category_directory in os.scandir(webcam_path):
            if category_directory.is_file():
                category_directory.stat().st_mtime_ns
                mod_time = category_directory.stat().st_mtime_ns
                if mod_time > most_recent_time:
                    most_recent_file = category_directory.name
                    most_recent_time = mod_time
        print("The most recent image found is \"%s\"." % most_recent_file)
    
        output_image = shared_tools.process_image("%s/%s" % (webcam_path, most_recent_file))
    
        with open("%s/%s"% (json_path, json_name)) as open_file:
            category_names = json.load(open_file)
        prediction = guess(output_image)
        print(prediction)
        print(category_names)
        prediction_number = numpy.argmax(prediction[0])
        print(pyfiglet.figlet_format(category_names[prediction_number], font = "banner3-D"))
        print(category_names[prediction_number])
        print("Showing image...")
        pyplot.imshow(output_image)
        pyplot.show()
