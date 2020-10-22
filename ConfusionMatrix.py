import pandas as pd
import os

dataset = pd.read_csv('../Pillbox.csv')

# we only consider dataset that only have images.
dataset = dataset[dataset.has_image == True]
dataset = dataset[['ID','splimage','splshape_text','splcolor_text']]
dataset = dataset[dataset.splimage != 'no_product_image']

# For check with img file if it exist! one time usage
# a = dataset.splimage.unique()
# check_img_exist = pd.DataFrame(a)
# check_img_exist[0] = check_img_exist[0]+'.jpg'
#
# for img in check_img_exist[0]:
#     path = os.path.join('..','pillbox_production_images_full_201812', img)
#     if os.path.isfile(path):
#         check_img_exist['exist'] = True
#     else:
#         check_img_exist['exist'] = False
#
# print(check_img_exist.exist.value_counts())

# import image for validating
# print(dataset.splcolor_text.value_counts()>10)
# a = dataset.splcolor_text.value_counts()
# a.to_csv('../color_count.txt',',')
#
#
# print(dataset[dataset.splshape_text == 'SQUARE'].head(15))