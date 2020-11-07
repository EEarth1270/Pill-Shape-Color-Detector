import os
import cv2
import numpy as np

from func import fed


def color_histogram_of_test_image(test_src_image):
    # load the image
    chans = cv2.split(test_src_image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter = 0
    for (chan, color) in zip(chans, colors):
        counter = counter + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)

        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
            # print(feature_data)

    with open('test.data', 'w') as myfile:
        myfile.write(feature_data)


def color_histogram_of_training_image(img_name):
    # detect image color by using image file name to label training data
    if 'red' in img_name:
        data_source = 'RED'
    elif 'yellow' in img_name:
        data_source = 'YELLOW'
    elif 'green' in img_name:
        data_source = 'GREEN'
    elif 'orange' in img_name:
        data_source = 'ORANGE'
    elif 'white' in img_name:
        data_source = 'WHITE'
    elif 'black' in img_name:
        data_source = 'BLACK'
    elif 'blue' in img_name:
        data_source = 'BLUE'
    elif 'purple' in img_name:
        data_source = 'PURPLE'
    elif 'brown' in img_name:
        data_source = 'BROWN'
    elif 'pink' in img_name:
        data_source = 'PINK'
    # load the image
    image = cv2.imread(img_name)
    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter = 0
    for (chan, color) in zip(chans, colors):
        counter = counter + 1

        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)

        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)

        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue

    with open('training.data', 'a') as myfile:
        myfile.write(feature_data + ',' + data_source + '\n')


def training():
    # red color training images
    for f in os.listdir('../color_training_dataset/red'):
        color_histogram_of_training_image('../color_training_dataset/red/' + f)

    # yellow color training images
    for f in os.listdir('../color_training_dataset/yellow'):
        color_histogram_of_training_image('../color_training_dataset/yellow/' + f)

    # green color training images
    for f in os.listdir('../color_training_dataset/green'):
        color_histogram_of_training_image('../color_training_dataset/green/' + f)

    # orange color training images
    for f in os.listdir('../color_training_dataset/orange'):
        color_histogram_of_training_image('../color_training_dataset/orange/' + f)

    # white color training images
    for f in os.listdir('../color_training_dataset/white'):
        color_histogram_of_training_image('../color_training_dataset/white/' + f)

    # black color training images
    for f in os.listdir('../color_training_dataset/black'):
        color_histogram_of_training_image('../color_training_dataset/black/' + f)

    # blue color training images
    for f in os.listdir('../color_training_dataset/blue'):
        color_histogram_of_training_image('../color_training_dataset/blue/' + f)

    # brown color training images
    for f in os.listdir('../color_training_dataset/brown'):
        color_histogram_of_training_image('../color_training_dataset/brown/' + f)

    for f in os.listdir('../color_training_dataset/pink'):
        color_histogram_of_training_image('../color_training_dataset/pink/' + f)

    for f in os.listdir('../color_training_dataset/purple'):
        color_histogram_of_training_image('../color_training_dataset/purple/' + f)