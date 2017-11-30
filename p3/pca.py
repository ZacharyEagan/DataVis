import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
df = pd.read_csv( filepath_or_buffer="iris_no_headers.csv", header=None, sep=',')

print df

df.columns=['sepal_len','sepal_wid', 'petal_len', 'petal_width', 'class']
df.dropna(how='all',inplace=True)

print "\n\n"
print df.tail()

X = df.ix[:,0:4].values
y = df.ix[:,4].values

from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)

import numpy as np
mean_vec = np.mean(X_std, axis=0)
cov_mat = np.cov(X_std.T)
print cov_mat


eig_vals, eig_vecs = np.linalg.eig(cov_mat)


u,s,v = np.linalg.svd(X_std.T)
print u

eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
eig_pairs.sort()



eig_pairs.reverse()
print "\n"
for i in eig_pairs:
   print i[0]


matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1), eig_pairs[1][1].reshape(4,1)))
print "\n"
print matrix_w

Y = X_std.dot(matrix_w)



print "\n\n\n\n\n"
print Y
print "\n\n"
print X_std

print "\n\n\n"

df = pd.read_csv( filepath_or_buffer="iris_no_headers.csv", header=None, sep=',')

print df

df.columns=['sepal_len','sepal_wid', 'petal_len', 'petal_width', 'class']
df.dropna(how='all',inplace=True)
df.tail();

X = df.ix[:,0:4].values
y = df.ix[:,4].values
from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(n_components = 2)
Y_sklearn = sklearn_pca.fit_transform(X_std)

