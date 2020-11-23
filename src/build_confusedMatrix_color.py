import pandas as pd
import sys
import numpy as np
from func import confusionMatrixColor as cF
from sklearn.metrics import classification_report

data = pd.read_csv('../../dataset_afterpred_train_color.csv')
print(type(data['splcolor_text']))
data['splcolor_text'] = data['splcolor_text'].apply(lambda x: x.split(';')[0])
print(type(data['splcolor_text']))
list1 = ['WHITE', 'RED', 'YELLOW', 'ORANGE', 'GREEN', 'PINK', 'GRAY', 'PURPLE', 'BLUE',
         'BROWN', 'TURQUOISE', 'BLACK', 'NONE']
print(list1)
class_label = list1
res = cF.generate_confusion_matrix(data, class_label)
cF.print_confusion_matrix(res, class_label, '../../Confused_Matrix_Train.txt')
# with open('../../Confused_Matrix_Train2.txt', 'w') as f:
#     sys.stdout = f
#     a = classification_report(data, data['predict_color'], target_names=class_label)
#     print(a)
