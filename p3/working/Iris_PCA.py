import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()
#print iris
#print type(iris)


#df = pd.read_csv(filepath_or_buffer="iris_no_headers.csv", header=None, sep=",")
#df = pd.read_csv(filepath_or_buffer="iris_no_headers.csv", header=None, sep=",")
df = pd.read_csv(filepath_or_buffer="iris_no_headers.csv", header=None, sep=",")
#df = pd.read_csv(filepath_or_buffer="data/Libraries_Annual_Statistics_Comparison_2010-2011.csv", header=None, sep=",")
#=['sepal_len','sepal_wid', 'petal_len', 'petal_width', 'class']

#X = iris.data[:, :2]
X = df.ix[:,0:3].values; 

y = iris.target
dct = {'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}
print y

y =[]
for pnt in df.ix[:,4].values:
   y.append(dct[pnt])

print X
print "\n"
print y
x_min, x_max = X[:, 0].min() - .5, X [:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X [:, 1].max() + .5

#plt.figure(2, figsize=(8,6))
#plt.clf()

#plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
#plt.xlabel('Sepal length');
#plt.ylabel('Sepal width')
#plt.xlim(x_min, x_max)
#plt.ylim(y_min, y_max)
#plt.xticks(())
#plt.yticks(())
#plt.show()
 

fig = plt.figure(1, figsize=(8,6))
ax = Axes3D(fig, elev=-150, azim=110)
#X_reduced = PCA(n_components=3).fit_transform(iris.data)
X_reduced = PCA(n_components=3).fit_transform(X)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1],X_reduced[:, 2],c=y, cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("Iris PCA plot")
ax.set_xlabel("vector 1")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("vector 2")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("vector 3")
ax.w_zaxis.set_ticklabels([])

plt.show()


