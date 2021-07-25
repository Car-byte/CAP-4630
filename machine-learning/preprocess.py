import numpy as np
import pandas as pd

import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from matplotlib import pyplot as plt

import random

columns = ['sepal_length', ' sepal_width', 'petal_length', 'petal_width', 'class']
iris = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', names=columns)

print("\n----------------------Before Scaling Data--------------------------------------\n")
print(iris.describe())

plot = sns.pairplot(iris, hue="class", markers=["o", "s", "D"])
plt.show()

iris['class_encod'] = iris['class'].apply(lambda x: 0 if x == 'Iris-setosa' else 1 if x == 'Iris-versicolor' else 2)

y = iris[['class_encod']]
x = iris.iloc[:, 0:4] 

scaler = MinMaxScaler()
scaled = scaler.fit_transform(x.values)
x = pd.DataFrame(scaled, columns=x.columns)

print("\n----------------------After Scaling Data--------------------------------------\n")
print(x.describe())

random.seed(0)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,
                                                    random_state=0, stratify=y)

np.shape(y_train)
