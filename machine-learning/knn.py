from preprocess import x_train
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

from matplotlib import pyplot as plt

from preprocess import x_train
from preprocess import y_train
from preprocess import x_test
from preprocess import y_test
from preprocess import iris

import numpy as np

from joblib import dump

knn = KNeighborsClassifier()
knn.fit(x_train, np.ravel(y_train))

print("\n----------------------Prediction--------------------------------------\n")

predict = knn.predict(x_test.iloc[0:10])
row = y_test["class_encod"]

for i in range(len(predict)):
  print("Predict:", predict[i], "\tActual:", row[y_test["class_encod"].index[i]])

print("\nPercent right of test data:", knn.score(x_test, y_test) * 100)

titles_options = [("Confusion matrix, without normalization", None), 
                  ("Normalized confusion matrix", 'true')]

for title, normalize in titles_options:
    disp = plot_confusion_matrix(knn, x_test, y_test, 
                                display_labels=iris['class'].unique(),
                                cmap=plt.cm.Blues,
                                normalize=normalize)
    disp.ax_.set_title(title)

plt.show()

dump(knn, 'iris-classifier-knn.dmp')
