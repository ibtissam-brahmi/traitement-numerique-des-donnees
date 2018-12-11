# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:21:46 2018

@author: hp
"""
from sklearn import *
from sklearn.datasets.samples_generator import make_blobs
import numpy as np
import matplotlib.pyplot as plt

#mnist = fetch_mldata('MNIST original'), génère une erreur du réseau (could not read bytes)
#print(mnist)

help(datasets.make_blobs)
data,clust = make_blobs(n_samples=1000, centers=4, n_features=2)
plt.figure()
plt.scatter(data[clust == 0, 0], data[clust == 0, 1], color='red')
plt.scatter(data[clust == 1, 0], data[clust == 1, 1], color='pink')
plt.scatter(data[clust==2, 0], data[clust==2, 1], color='green')
plt.scatter(data[clust==3, 0], data[clust==3, 1], color='yellow')
plt.title('donnees reparties en 4 clusters')
plt.xlabel('feature_1')
plt.ylabel('feature_2')
plt.xlim = (-15,15)
plt.ylim = (-15,15)
plt.show()


data1, clust1 = make_blobs(n_samples=100, centers=2, n_features=2)
data2, clust2 = make_blobs(n_samples=500, centers=3, n_features=2)
data_stacked = np.vstack((data1,data2))
clust_stacked = np.hstack((clust1,clust2))

plt.scatter(data_stacked[clust_stacked==0, 0], data_stacked[clust_stacked==0, 1], color='red')
plt.scatter(data_stacked[clust_stacked==1, 0], data_stacked[clust_stacked==1, 1], color='blue')
plt.scatter(data_stacked[clust_stacked==2, 0], data_stacked[clust_stacked==2, 1], color='green')
plt.title('donnees rassemblees')
plt.xlabel('feature_1')
plt.ylabel('feature_2')
plt.show()

