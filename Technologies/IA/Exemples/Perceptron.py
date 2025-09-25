# Write an exemple in python a a perceptron algorithm

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Étape 1 : Générer des données d'entraînement
# Générer des données avec deux classes

X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=42)

# Afficher les données
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='red', label='Classe 0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='blue', label='Classe 1')
plt.xlabel('Caractéristique 1')
plt.ylabel('Caractéristique 2')
plt.legend()
plt.show()

# Étape 2 : Entraîner le modèle de perceptron
# Diviser les données en un ensemble d'entraînement et un ensemble de test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
model = Perceptron()
model.fit(X_train, y_train)

# Étape 3 : Tester le modèle
# Tester le modèle sur l'ensemble de test

y_pred = model.predict(X_test)

# Étape 4 : Afficher les résultats
# Afficher les données de test et les prédictions du modèle

plt.scatter(X_test[y_test == 0][:, 0], X_test[y_test == 0][:, 1], color='red', label='Classe 0 (réel)')
plt.scatter(X_test[y_test == 1][:, 0], X_test[y_test == 1][:, 1], color='blue', label='Classe 1 (réel)')
plt.scatter(X_test[y_pred == 0][:, 0], X_test[y_pred == 0][:, 1], color='orange', label='Classe 0 (prédit)')
plt.scatter(X_test[y_pred == 1][:, 0], X_test[y_pred == 1][:, 1], color='green', label='Classe 1 (prédit)')
plt.xlabel('Caractéristique 1')
plt.ylabel('Caractéristique 2')
plt.legend()
plt.show()

# Calculer la précision du modèle
accuracy = accuracy_score(y_test, y_pred)
print(f'Précision du modèle : {accuracy:.2f}')

