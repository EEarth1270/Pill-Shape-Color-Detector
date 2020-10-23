import pandas as pd
import os
import confusionMatrix as cF
data = pd.read_csv('../dataset_afterpred.csv')

# print(data.number_polygon.value_counts())
# print(data.predict_shape.value_counts())
# print(data.splshape_text.value_counts())
class_label = ['ROUND','OVAL','CAPSULE','TRIANGLE','QUADRANGLE','FREEFORM']

res = cF.generate_confusion_matrix(data,class_label)
cF.print_confusion_matrix(res,class_label)

