import sys
import pandas as pd
from func import fed
from tqdm import tqdm
from sklearn.metrics import classification_report
import os
dataset = pd.read_csv('/../Pillbox.csv')


# we only consider dataset that only have images.
dataset = dataset[dataset.has_image == True]
dataset = dataset[['ID', 'splimage', 'splshape_text', 'splcolor_text']]
dataset = dataset[dataset.splimage != 'no_product_image']

# For check with img file if it exist! one time usage

# for img in dataset['splimage']:
#     img = img + '.jpg'
#     path = os.path.join('..', 'pillbox_production_images_full_201812', img)
#     dataset['exist'] = os.path.exists(path)
#
# a = dataset[dataset.exist == True]
# a.to_csv('../fail_image.csv')

# import image for validating
# print(dataset.splcolor_text.value_counts()>10)
# a = dataset.splcolor_text.value_counts()
# a.to_csv('../color_count.txt',',')
cond = dataset.splshape_text == 'RECTANGLE'
dataset.loc[cond, 'splshape_text'] = 'QUADRANGLE'
cond2 = dataset.splshape_text == 'DIAMOND'
dataset.loc[cond2, 'splshape_text'] = 'QUADRANGLE'
cond3 = dataset.splshape_text == 'SQUARE'
dataset.loc[cond3, 'splshape_text'] = 'QUADRANGLE'
cond4 = dataset.splshape_text == 'TRAPEZOID'
dataset.loc[cond4, 'splshape_text'] = 'FREEFORM'
cond4 = dataset.splshape_text == 'HEXAGON (6 SIDED)'
dataset.loc[cond4, 'splshape_text'] = 'FREEFORM'
cond4 = dataset.splshape_text == 'OCTAGON (8 SIDED)'
dataset.loc[cond4, 'splshape_text'] = 'FREEFORM'
cond4 = dataset.splshape_text == 'PENTAGON (5 SIDED)'
dataset.loc[cond4, 'splshape_text'] = 'FREEFORM'
cond4 = dataset.splshape_text == 'TEAR'
dataset.loc[cond4, 'splshape_text'] = 'OVAL'
cond4 = dataset.splshape_text == 'DOUBLE CIRCLE'
dataset.loc[cond4, 'splshape_text'] = 'ROUND'
cond4 = dataset.splshape_text == 'BULLET'
dataset.loc[cond4, 'splshape_text'] = 'FREEFORM'
cond4 = dataset.splshape_text == 'SEMI-CIRCLE'
dataset.loc[cond4, 'splshape_text'] = 'FREEFORM'
# print(dataset[dataset.splshape_text == 'TEAR'])


def grid_search(dataframe, block_sizes, constants, co_ef):
    for block in tqdm(block_sizes):
        for cont in tqdm(constants):
            for co in tqdm(co_ef):
                for index, row in tqdm(dataframe.iterrows(),mininterval = 5):
                    condition = dataframe['splimage'] == row.splimage
                    img = row.splimage + '.jpg'
                    path = os.path.join('..', 'pillbox_production_images_full_201812', img)
                    number_polygon, shape = fed.Grid_shape_pred(path, block, cont, co)
                    dataframe.loc[condition, 'number_polygon'] = number_polygon
                    dataframe.loc[condition, 'predict_shape'] = shape
                file_name = '../out_folder/confusion/block{}_cont{}_coef{}.txt'.format(block, cont, co)
                with open(file_name, 'w') as f:
                    sys.stdout = f
                    a = classification_report(dataframe['splshape_text'], dataframe['predict_shape'],
                                              target_names=class_label)
                    print(a)
                    print_polygon(dataframe)


def print_polygon(dataframe):
    print('Round')
    print(dataframe[dataframe['splshape_text'] == 'ROUND'].number_polygon.value_counts())
    print('OVAL')
    print(dataframe[dataframe['splshape_text'] == 'OVAL'].number_polygon.value_counts())
    print('CAPSULE')
    print(dataframe[dataframe['splshape_text'] == 'CAPSULE'].number_polygon.value_counts())
    print('TRIANGLE')
    print(dataframe[dataframe['splshape_text'] == 'TRIANGLE'].number_polygon.value_counts())
    print('QUADRANGLE')
    print(dataframe[dataframe['splshape_text'] == 'QUADRANGLE'].number_polygon.value_counts())
    print('FREEFORM')
    print(dataframe[dataframe['splshape_text'] == 'FREEFORM'].number_polygon.value_counts())


block_size = [15, 17,19,21,23,25]
contant = [3, 3.5]
coef = [0.037, 0.039, 0.042, 0.046, 0.048]
class_label = ['ROUND', 'OVAL', 'CAPSULE', 'TRIANGLE', 'QUADRANGLE', 'FREEFORM']

grid_search(dataset,block_size,contant,coef)

