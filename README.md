# Pill-Shape-Color-Detector
This Project using OpenCV and Neural Network.

Dataset: https://www.kaggle.com/dhuh137/pillbox

Shape Prediction and Color Prediction in this file
``` python
func/fed.py
```

### Stronk members
Mr.KIATISAK PETHOR [EEarth1270](https://github.com/EEarth1270) <-- Preprocess and Shape prediction part<br> 
Mr.CHAICHET PHAIBUNWITTHAYASAK [mrforgotten](https://github.com/mrforgotten) <-- integrated and Node implementation part<br> 
Mr.VORAPOL CHAROENKITMONGKOL [flukerbooker](https://github.com/flukerbooker) <-- Color prediction part<br> 

Most preprocessing, shape prediction will be in this file, and it will run magic code that will predict the shape

```
pill_classification_node/server/pyfol/shape_predict/func/fed.py
```
<p>Then, the picture will be throw in to this file and the color prediction will start from here</p>

```
pill_classification_node/server/pyfol/shape_predict/func/src/colorPredictor.py
```
<p>It will also run two file</p>

`pill_classification_node/server/pyfol/shape_predict/func/src/color_recognition_api/knn_classifier.py`<br>

and <br>

`pill_classification_node/server/pyfol/shape_predict/func/src/color_recognition_api/color_histogram_feature_extraction.py`<br>

Thanks to,
https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
https://github.com/ahmetozlu/color_recognition
