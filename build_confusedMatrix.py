import pandas as pd
import os
data = pd.read_csv('../dataset_afterpred.csv')

print(data.number_polygon.value_counts())
print(data.predict_shape.value_counts())
print(data.splshape_text.value_counts())
class_labels = ['ROUND','OVAL','CAPSULE','TRIANGLE','QUADRANGLE','FREEFORM']

def generate_confusion_matrix(dataframe):
    result = list()

    for i in range(len(class_labels)):
        result.append(list())
        for j in range(len(class_labels)):
            result[i].append(0)

