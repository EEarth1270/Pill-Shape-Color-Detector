import pandas as pd
import sys
from func import confusionMatrix as cF
from sklearn.metrics import classification_report


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


data = pd.read_csv('../dataset_afterpred.csv')

# print(data.number_polygon.value_counts())
# print(data.predict_shape.value_counts())
# print(data.splshape_text.value_counts())
class_label = ['ROUND','OVAL','CAPSULE','TRIANGLE','QUADRANGLE','FREEFORM']
#
res = cF.generate_confusion_matrix(data,class_label)
cF.print_confusion_matrix(res, class_label, '../../Confused_Matrix2.txt')
with open('../Confused_Matrix.txt', 'w') as f:
    sys.stdout = f
    a = classification_report(data['splshape_text'],data['predict_shape'],target_names=class_label)
    print(a)
    print_polygon(data)


