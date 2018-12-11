# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 08:38:02 2018

@author: hp
"""
#importer les librairies nécessaires
from sklearn import *
import numpy as np
import matplotlib.pyplot

###################### Manipulation d'un jeu de données ###############

#importer les données
iris = datasets.load_iris()

#afficher les données
print(iris.data)
print(iris.target)
print(iris.feature_names)
print(iris.target_names)

print(iris.data.mean(0))
print(iris.data.std(0))
print(iris.data.max(0))
print(iris.data.min(0))
print('le nombre de données est',np.shape(iris.data)[0])
print('le nombre de variables est',np.shape(iris.data)[1])
print('le nombre de classes est', np.size(iris.target_names))


##################### Téléchargement et importation des données ########################

