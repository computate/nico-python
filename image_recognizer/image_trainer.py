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
import shared_tools

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
    for category_directory in os.scandir(original_directory_path):
        if category_directory.is_dir():
            category_names.append(category_directory.name)
            print("\n%s\n"% category_directory.name)
            child_image_counter = 0
            os.makedirs("%s/%s"% (prepared_directory_path, category_directory.name), exist_ok=True)
            for child_entry in os.scandir("%s/%s" % (original_directory_path, category_directory.name)):
                if child_entry.is_file():
                    processed_image = shared_tools.process_image(child_entry.path)
                    train_images.append(processed_image)
                    train_labels.append(label_counter)
                    the_path = "%s/%s/%s" % (prepared_directory_path, category_directory.name, child_entry.name)
                    cv2.imwrite(the_path, processed_image)
                    total_image_counter = total_image_counter+1
                    child_image_counter = child_image_counter+1
                    print("    #%s in %s done. (%s total images done.)\n"% (child_image_counter, category_directory.name, total_image_counter))
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
