import pandas as pd
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

df = pd.read_csv( filepath_or_buffer="iris_no_headers.csv", header=None, sep=',')
#df = pd.read_csv( filepath_or_buffer="postscndryunivsrvy2013dirinfo.csv", header=None, sep=',')
df.columns=['sepal_len','sepal_wid', 'petal_len', 'petal_width', 'class']
df.dropna(how='all',inplace=True)
df.tail();

X = df.ix[:,0:4].values
y = df.ix[:,4].values


X_std = StandardScaler().fit_transform(X)


sklearn_pca = sklearnPCA(n_components = 3)
Y_sklearn = sklearn_pca.fit_transform(X_std)

print Y_sklearn


fig = plt.figure(1, figsize=(8,6))
ax = Axes3D(fig, elev=-150, azim=110)

ax = fig.add_subplot(111,projection='3d')
plt.rcParams['legend.fontsize'] = 10

print Y_sklearn[0,:]
print Y_sklearn[:,1]
#ax.plot(Y_sklearn[:,0],Y_sklearn[:,1],Y_sklearn[:,2])
ax.scatter(Y_sklearn[:,0],Y_sklearn[:,1],Y_sklearn[:,2], c = df.columns, cmap=plt.cm.Set1, edgecolor = 'k', s=40)

plt.show()
