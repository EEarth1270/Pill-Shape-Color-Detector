import pandas as pd
import os
import fed
dataset = pd.read_csv('../Pillbox.csv')

# we only consider dataset that only have images.
dataset = dataset[dataset.has_image == True]
dataset = dataset[['ID','splimage','splshape_text','splcolor_text']]
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
dataset.loc[cond,'splshape_text'] = 'QUADRANGLE'
cond2 = dataset.splshape_text == 'DIAMOND'
dataset.loc[cond2,'splshape_text'] = 'QUADRANGLE'
cond3 = dataset.splshape_text == 'SQUARE'
dataset.loc[cond3,'splshape_text'] = 'QUADRANGLE'
cond4 = dataset.splshape_text == 'TRAPEZOID'
dataset.loc[cond4,'splshape_text'] = 'FREEFORM'
cond4 = dataset.splshape_text == 'HEXAGON (6 SIDED)'
dataset.loc[cond4,'splshape_text'] = 'FREEFORM'
cond4 = dataset.splshape_text == 'OCTAGON (8 SIDED)'
dataset.loc[cond4,'splshape_text'] = 'FREEFORM'
cond4 = dataset.splshape_text == 'PENTAGON (5 SIDED)'
dataset.loc[cond4,'splshape_text'] = 'FREEFORM'
cond4 = dataset.splshape_text == 'TEAR'
dataset.loc[cond4,'splshape_text'] = 'OVAL'
cond4 = dataset.splshape_text == 'DOUBLE CIRCLE'
dataset.loc[cond4,'splshape_text'] = 'ROUND'
cond4 = dataset.splshape_text == 'BULLET'
dataset.loc[cond4,'splshape_text'] = 'FREEFORM'
cond4 = dataset.splshape_text == 'SEMI-CIRCLE'
dataset.loc[cond4,'splshape_text'] = 'FREEFORM'
# print(dataset[dataset.splshape_text == 'TEAR'])


print(dataset.splshape_text.value_counts())
# dataset.splimage.unique().tofile('../file_image_count.csv', ',')

for img in dataset['splimage']:
    condition = dataset['splimage'] == img
    img = img+'.jpg'
    path = os.path.join('..', 'pillbox_production_images_full_201812', img)
    number_polygon, shape = fed.shapeDetector(path)
    print(path, number_polygon, shape)
    dataset.loc[condition, 'number_polygon'] = number_polygon
    dataset.loc[condition, 'predict_shape'] = shape

dataset.to_csv('../dataset_afterpred.csv')
