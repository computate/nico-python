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

directory_path = '/home/ntate/Pictures/Webcam'
model_path = "/home/ntate/AIML/model"
json_path = "/home/ntate/AIML/json"
json_name = "category-names.json"

print("Loading the Model in \"%s\" (This will take a few seconds...)"% model_path)
model = tensorflow.keras.models.load_model(model_path)

while True:
    print("\n\nFinding out the most recent image in %s..." % directory_path)
    most_recent_file = None
    most_recent_time = 0
    for entry in os.scandir(directory_path):
        if entry.is_file():
            entry.stat().st_mtime_ns
            mod_time = entry.stat().st_mtime_ns
            if mod_time > most_recent_time:
                most_recent_file = entry.name
                most_recent_time = mod_time
    print("The most recent image found is \"%s\"." % most_recent_file)

    print("Removing Backround...")
    input_image = Image.open("%s/%s" % (directory_path, most_recent_file))
    output_image = rembg.remove(input_image)
    #print("Showing new Image.")
    #output_image.show()

    print("Cropping Image...")
    def trim(input_image):
        bg = Image.new(input_image.mode, input_image.size, input_image.getpixel((0,0)))
        diff = ImageChops.difference(input_image, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            return input_image.crop(bbox)
        else:
            return input_image
    output_image = trim(output_image)
    #print("Showing newer image.")
    #output_image.show()

    print("Making the image B&W, Scaling the image, and adding padding...")
    output_image = numpy.array(ImageOps.pad(output_image, (28, 28), color=(0,0,0,255)))
    output_image = cv2.cvtColor(cv2.cvtColor(output_image, cv2.COLOR_BGRA2BGR), cv2.COLOR_BGR2GRAY)

    print("Importing the category-names.json file in \"%s/category-names.json...\""% json_path)
    with open("%s/%s"% (json_path, json_name)) as open_file:
        category_names = json.load(open_file)
    print("Doin' some other stuff...")
    output_image2 = output_image / 255.0
    output_image2 = (numpy.expand_dims(output_image2, 0))
    print("\n\n\n        Predicting!\n\n\n")
    prediction = model.predict(output_image2)
    print(prediction)
    prediction_number = numpy.argmax(prediction[0])
    print(pyfiglet.figlet_format(category_names[prediction_number], font = "banner3-D"))
    print("Showing image...")
    pyplot.imshow(output_image)
    pyplot.show()