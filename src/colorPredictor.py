from func import fed
import os.path
import pandas as pd
from tqdm import tqdm

dataset = pd.read_csv('../../Pillbox.csv')
dataset = dataset[dataset.has_image == True]
dataset = dataset[['splimage', 'splcolor_text']]
dataset = dataset[dataset.splimage != 'no_product_image']
print(os.getcwdb())
data = dataset.splcolor_text == 'GRAY'
print(data.value_counts())

for index, row in tqdm(dataset.iterrows()):
    condition = dataset['splimage'] == row.splimage
    img = row.splimage + '.jpg'
    path_image = os.path.join('..', '..', 'pillbox_production_images_full_201812', img)
    prediction = fed.colorPrediction(path_image)
    dataset.loc[condition, 'predict_color'] = prediction
dataset.to_csv('../../dataset_afterpred.csv')