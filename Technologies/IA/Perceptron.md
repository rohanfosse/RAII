# Les bases de l'IA et du Perceptron en Python

L'intelligence artificielle (IA) est un domaine de l'informatique qui vise à créer des systèmes capables de réaliser des tâches qui nécessiteraient normalement l'intelligence humaine. Parmi les nombreux modèles utilisés en IA, le perceptron est l'un des plus simples. Il s'agit d'un type de réseau de neurones artificiels utilisé pour la classification linéaire. Dans ce cours, nous allons explorer les bases de l'IA et comment implémenter un perceptron en Python.

## Introduction à l'IA

L'IA peut être divisée en deux catégories principales : l'IA faible et l'IA forte. L'IA faible est conçue et entraînée pour effectuer une tâche spécifique, tandis que l'IA forte possède les capacités cognitives d'un être humain. La plupart des technologies d'IA actuelles, y compris les perceptrons, relèvent de l'IA faible.

## Le Perceptron

Le perceptron est un type de réseau de neurones artificiels très simple, utilisé pour la classification binaire. Il peut être considéré comme la brique de base des réseaux de neurones plus complexes. Le perceptron a été développé par Frank Rosenblatt en 1957, inspiré par les neurones biologiques. Son fonctionnement repose sur la mise à jour itérative de poids associés à chaque entrée pour prédire correctement la classe d'une donnée.

### Fonctionnement du Perceptron

Le perceptron prend en entrée un vecteur de caractéristiques \(X\) (par exemple, les mesures d'une fleur) et produit une sortie binaire, indiquant l'appartenance à l'une des deux classes possibles (par exemple, Iris Setosa ou non Setosa). Voici les composants clés de son fonctionnement :

1. **Entrées (Inputs)**: Chaque entrée \(x_i\) dans le vecteur \(X\) est associée à un poids \(w_i\). Les poids représentent l'importance de chaque entrée pour la décision finale. Une entrée supplémentaire, souvent appelée biais (\(b\) ou \(w_0\)), est ajoutée pour permettre au perceptron de s'adapter mieux aux données. Le biais a toujours une valeur d'entrée de 1.

2. **Somme pondérée (Net Input)**: Le perceptron calcule la somme pondérée de ses entrées, appelée également entrée nette. Cette somme est la base de la décision du perceptron et est calculée comme suit : \(z = w_0 + w_1x_1 + w_2x_2 + ... + w_nx_n\), où \(w_0\) est le biais, \(w_1, ..., w_n\) sont les poids, et \(x_1, ..., x_n\) sont les entrées.

3. **Fonction d'activation**: La somme pondérée est ensuite passée à travers une fonction d'activation pour obtenir la sortie. Dans le cas du perceptron, la fonction d'activation la plus couramment utilisée est la fonction d'activation de seuil, qui produit une sortie binaire :
   \[
   \text{sortie} =
   \begin{cases} 
   1 & \text{si } z \geq 0 \\
   -1 & \text{sinon}
   \end{cases}
   \]
   Cette sortie indique la classe prédite par le perceptron.

4. **Apprentissage**: L'apprentissage dans un perceptron se fait par la mise à jour des poids en fonction des erreurs de prédiction. Pour chaque exemple d'entraînement, le perceptron fait une prédiction. Si la prédiction est correcte, aucun changement n'est effectué. Si la prédiction est incorrecte, les poids sont ajustés selon la règle suivante : \(w_i = w_i + \eta(y - \hat{y})x_i\), où \(\eta\) est le taux d'apprentissage, \(y\) est la vraie classe de l'exemple, et \(\hat{y}\) est la classe prédite. Le biais est également mis à jour de manière similaire.

### Limitations

Le perceptron ne peut classer correctement que les données qui sont linéairement séparables, c'est-à-dire qu'il existe une ligne droite (ou un hyperplan dans des dimensions plus élevées) qui peut séparer les données en deux classes. Pour des problèmes plus complexes, non linéairement séparables, des modèles plus avancés, comme les réseaux de neurones multicouches (aussi appelés perceptrons multicouches), sont nécessaires.

### Exemple d'application

Pour illustrer l'exemple d'application du perceptron avec un ensemble de données simple, nous allons simuler un scénario de classification binaire. Imaginons que nous ayons un ensemble de données fictif représentant deux types de fleurs, chacune caractérisée par deux caractéristiques : la longueur et la largeur des sépales. Notre objectif est d'entraîner un perceptron pour classer ces fleurs en deux catégories.

D'abord, nous devons installer la bibliothèque NumPy, si ce n'est pas déjà fait, car elle sera utilisée pour les opérations mathématiques :

```bash
pip install numpy
```

Ensuite, voici le code Python pour l'exemple d'application :

```python
import numpy as np

class Perceptron(object):
    def __init__(self, learning_rate=0.01, n_iterations=10):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        self.weights = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iterations):
            errors = 0
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights[1:] += update * xi
                self.weights[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.weights[1:]) + self.weights[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

# Création de l'ensemble de données fictif
# Caractéristiques : longueur et largeur des sépales
X = np.array([[1, 2], [2, 1], [3, 3], [4, 1]])
# Étiquettes : 1 pour le type de fleur A, -1 pour le type de fleur B
y = np.array([1, -1, 1, -1])

# Entraînement du perceptron
perceptron = Perceptron(learning_rate=0.01, n_iterations=10)
perceptron.fit(X, y)

# Test du perceptron avec de nouvelles données
print("Prédictions pour de nouvelles observations :")
print(perceptron.predict([[2, 2], [3, 2], [1, 3]]))
```

### Explication du Code

1. **Définition de la classe Perceptron** : Cette classe implémente un perceptron simple avec des méthodes pour l'entraînement (`fit`) et la prédiction (`predict`).

2. **Initialisation** : Le perceptron est initialisé avec un taux d'apprentissage (`learning_rate`) et un nombre d'itérations (`n_iterations`).

3. **Entraînement (`fit`)** : La méthode `fit` entraîne le perceptron sur l'ensemble de données fourni (`X` pour les caractéristiques et `y` pour les étiquettes). Les poids sont ajustés en fonction des erreurs de prédiction.

4. **Prédiction (`predict`)** : La méthode `predict` utilise les poids appris pour prédire la classe de nouvelles observations.

5. **Ensemble de données fictif** : `X` représente les caractéristiques (longueur et largeur des sépales) de quatre fleurs, et `y` contient les étiquettes correspondantes (1 pour le type A, -1 pour le type B).

6. **Test du modèle** : Après l'entraînement, le perceptron est testé avec de nouvelles observations pour voir comment il classe les fleurs en fonction de leurs caractéristiques.
