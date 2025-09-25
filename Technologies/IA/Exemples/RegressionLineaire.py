import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Étape 1 : Générer des données d'entraînement
# Générer des moments aléatoires
x_train = np.random.rand(100, 1) * 10  # Moments aléatoires entre 0 et 10
# Générer des positions en utilisant une relation linéaire simple, avec du bruit
y_train = 2.5 * x_train + np.random.randn(100, 1) * 2

# Étape 2 : Entraîner le modèle de régression linéaire
model = LinearRegression()
model.fit(x_train, y_train)

# Étape 3 : Tester le modèle
# Générer de nouvelles données pour tester le modèle
x_test = np.array([[0], [5], [10]])
y_test = model.predict(x_test)

# Étape 4 : Afficher les résultats
# Afficher les données d'entraînement et la prédiction du modèle
plt.scatter(x_train, y_train, color='blue', label='Données d\'entraînement')
plt.plot(x_test, y_test, color='red', label='Prédiction du modèle')
plt.xlabel('Temps')
plt.ylabel('Position')
plt.legend()
plt.show()

print(f'Prédictions à des moments différents : {x_test.flatten()} -> {y_test.flatten()}')
