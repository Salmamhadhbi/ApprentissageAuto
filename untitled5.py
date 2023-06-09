# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rwbm6Dv8d46m2WpQ65U0sqbVtdBXCB4H
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# Charger le jeu de données
df = pd.read_csv('creditcard.csv')

# Diviser les données en caractéristiques (X) et variable cible (y)
X = df.drop('Class', axis=1)
y = df['Class']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construction du modèle de forêts aléatoires
model_rf = RandomForestClassifier()

# Entraîner le modèle sur l'ensemble d'entraînement
model_rf.fit(X_train, y_train)

#Supprimer les échantillons avec des valeurs manquantes des données d'entraînement
X_train_dropna = X_train.dropna()
y_train_dropna = y_train[X_train.index].dropna()

# Supprimer les échantillons avec des valeurs manquantes des données de test
X_test_dropna = X_test.dropna()
y_test_dropna = y_test[X_test.index].dropna()

# Construction du modèle de forêts aléatoires
model_rf = RandomForestClassifier()

# Entraîner le modèle sur les données d'entraînement sans valeurs manquantes
model_rf.fit(X_train_dropna, y_train_dropna)

# Prédire les classes pour l'ensemble de test sans valeurs manquantes
y_pred_rf = model_rf.predict(X_test_dropna)

# Évaluation du modèle
print(confusion_matrix(y_test_dropna, y_pred_rf))
print(classification_report(y_test_dropna, y_pred_rf))

"""2éme algorithme Réseaux de neurones :"""

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# Charger le jeu de données
df = pd.read_csv('creditcard.csv')

# Diviser les données en caractéristiques (X) et variable cible (y)
X = df.drop('Class', axis=1)
y = df['Class']

# Supprimer les échantillons avec des valeurs manquantes
X_dropna = X.dropna()
y_dropna = y[X_dropna.index]

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_dropna, y_dropna, test_size=0.2, random_state=42)

# Construction du modèle de réseaux de neurones
model_nn = MLPClassifier(hidden_layer_sizes=(64, 64))

# Entraîner le modèle sur l'ensemble d'entraînement
model_nn.fit(X_train, y_train)

# Prédire les classes pour l'ensemble de test
y_pred_nn = model_nn.predict(X_test)

# Évaluation du modèle
print(confusion_matrix(y_test, y_pred_nn))
print(classification_report(y_test, y_pred_nn))