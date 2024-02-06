print("\nImporting and defining functions...\n")
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Choose how many images to prepare")
    original_directory_path = '/home/ntate/Pictures/aiml/original'
    prepared_directory_path = '/home/ntate/Pictures/aiml/prepared'
    model_path = "/home/ntate/AIML/model"
    json_path = "/home/ntate/AIML/json/"
    json_name = "category-names.json"
    most_recent_file = None
    most_recent_time = 0
    total_image_counter = 0
    label_counter = 0
    train_images = []
    train_labels = []
    category_names = []
    amount_of_training_images = 0
    epochs = 9999

    print("Setting up arguments...")
    parser.add_argument("number", type=int)
    args = parser.parse_args()
    print("You chose to create %s images per category."% args.number)
    amount_of_training_images = args.number

    print("Deleting old prepared images so they are updated...")
    shutil.rmtree(prepared_directory_path, ignore_errors=True)

    print("Finding Images in %s.\n"% original_directory_path)
    for entry in os.scandir(original_directory_path):
        if entry.is_dir():
            category_names.append(entry.name)
            print("\n%s\n"% entry.name)
            child_image_counter = 0
            os.makedirs("%s/%s"% (prepared_directory_path, entry.name), exist_ok=True)
            for child_entry in os.scandir("%s/%s" % (original_directory_path, entry.name)):
                if child_entry.is_file():
                    processed_image = process_image(child_entry.path)
                    train_images.append(processed_image)
                    train_labels.append(label_counter)
                    the_path = "%s/%s/%s" % (prepared_directory_path, entry.name, child_entry.name)
                    cv2.imwrite(the_path, processed_image)
                    total_image_counter = total_image_counter+1
                    child_image_counter = child_image_counter+1
                    print("    #%s in %s done. (%s total images done.)\n"% (child_image_counter, entry.name, total_image_counter))
                    if child_image_counter == amount_of_training_images and amount_of_training_images > 0:
                        break
                    if child_image_counter > amount_of_training_images and amount_of_training_images > 0:
                        print("Somehow, image-trainer.py has prepared more training images than you asked earlier.\nPlease delete those images and try again.")
                        break
            label_counter = label_counter+1
    train_images = numpy.asarray(train_images)
    train_labels = numpy.asarray(train_labels)
    print(train_labels)
    print(category_names)
    print(train_images.shape)

    print("\nBuilding Model...\n")
    train_images = train_images / 255.0
    model = tensorflow.keras.Sequential([
        tensorflow.keras.layers.Flatten(input_shape=(28, 28)),
        tensorflow.keras.layers.Dense(128, activation='relu'),
        tensorflow.keras.layers.Dense(label_counter)
    ])
    print("\nCompiling Model...\n")
    model.compile(optimizer='adam',
                  loss=tensorflow.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=epochs)
    print("Saving Model...")
    model.save(model_path)

    print("\nExporting category_names to a json file in \"%s\"...\n"% json_path)
    with open("%s/%s"% (json_path, json_name), "w") as file_writer:
        file_writer.write(json.dumps(category_names, indent=4))
