# Cours sur la Régression Linéaire avec Python

## Régression Linéaire Simple

La régression linéaire simple est une méthode statistique qui permet d'étudier la relation entre deux variables quantitatives : une variable dépendante \(Y\) et une variable indépendante \(X\). L'objectif est de modéliser cette relation à travers une équation linéaire qui prédit la valeur de \(Y\) à partir de \(X\), permettant ainsi de faire des prédictions ou d'inférer la nature de la relation entre les deux variables.

### Formulation Mathématique

L'équation d'une régression linéaire simple est donnée par :

\[ Y = \beta_0 + \beta_1X + \epsilon \]

où :
- \(Y\) est la variable dépendante que l'on cherche à prédire.
- \(X\) est la variable indépendante utilisée pour la prédiction.
- \(\beta_0\) est l'intercept, ou l'ordonnée à l'origine, qui représente la valeur de \(Y\) lorsque \(X = 0\).
- \(\beta_1\) est la pente de la droite, qui indique la variation de \(Y\) pour une variation d'une unité de \(X\).
- \(\epsilon\) est le terme d'erreur, représentant la différence entre les valeurs observées et les valeurs prédites par le modèle. Ce terme capture tous les autres facteurs qui influencent \(Y\) mais ne sont pas inclus dans le modèle.

### Estimation des Coefficients

Les coefficients \(\beta_0\) et \(\beta_1\) sont estimés à partir des données disponibles en minimisant la somme des carrés des résidus (SSR), où un résidu est la différence entre une observation réelle \(y_i\) et la prédiction \(\hat{y}_i\) donnée par le modèle. La méthode la plus courante pour cette estimation est la méthode des moindres carrés.

### Hypothèses Fondamentales

La régression linéaire simple repose sur plusieurs hypothèses importantes :

1. **Linéarité** : La relation entre \(X\) et \(Y\) doit être linéaire.
2. **Indépendance** : Les résidus (erreurs) sont indépendants les uns des autres.
3. **Homoscédasticité** : La variance des termes d'erreur est constante pour toutes les valeurs de \(X\).
4. **Normalité** : Les résidus suivent une distribution normale.

### Évaluation du Modèle

L'évaluation de la qualité d'un modèle de régression linéaire simple peut se faire à travers plusieurs métriques et diagnostics, notamment :

- **Coefficient de détermination (\(R^2\))** : Mesure la proportion de la variance de \(Y\) expliquée par le modèle. \(R^2\) varie entre 0 et 1, une valeur proche de 1 indiquant que le modèle explique une grande partie de la variance de \(Y\).
- **Test de significativité des coefficients** : Permet de tester si les coefficients \(\beta_0\) et \(\beta_1\) sont significativement différents de zéro, indiquant ainsi si \(X\) a un effet significatif sur \(Y\).
- **Analyse des résidus** : Permet de vérifier les hypothèses du modèle, notamment l'homoscédasticité et la normalité des résidus.

### Exemple Pratique

Imaginons que nous voulons modéliser la relation entre les années d'expérience (\(X\)) et le salaire (\(Y\)) d'employés. Après avoir collecté les données, nous appliquons la régression linéaire simple pour estimer les coefficients. Si nous obtenons une équation de la forme \( Y = 30000 + 5000X \), cela signifie qu'un employé sans expérience (0 année) aurait un salaire de base de 30 000 (intercept), et pour chaque année d'expérience supplémentaire, le salaire augmenterait de 5 000.

### Exemple en Python avec `scikit-learn`

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Données d'exemple
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Séparation des données en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Création du modèle de régression linéaire
model = LinearRegression()

# Entraînement du modèle
model.fit(X_train, y_train)

# Prédiction sur l'ensemble de test
y_pred = model.predict(X_test)

# Affichage des résultats
plt.scatter(X, y, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('Régression Linéaire Simple')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

print("Coefficient (pente):", model.coef_)
print("Ordonnée à l'origine:", model.intercept_)
```

Dans cet exemple, nous avons utilisé `scikit-learn` pour créer un modèle de régression linéaire simple, l'entraîner sur un ensemble de données, et effectuer des prédictions. Nous avons également tracé la ligne de régression sur un graphique pour visualiser le modèle.

## Régression Linéaire Multiple

La régression linéaire multiple est une extension de la régression linéaire simple permettant de modéliser la relation entre une variable dépendante \(Y\) et deux variables indépendantes \(X_1, X_2, ..., X_n\) ou plus. Elle est utilisée pour examiner l'effet simultané de plusieurs variables indépendantes sur la variable dépendante. Cette méthode est particulièrement utile dans les cas où la relation avec la variable dépendante est influencée par plusieurs facteurs.

### Formulation Mathématique

L'équation d'une régression linéaire multiple est donnée par :

\[ Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_nX_n + \epsilon \]

où :
- \(Y\) est la variable dépendante.
- \(X_1, X_2, ..., X_n\) sont les variables indépendantes.
- \(\beta_0\) est l'intercept.
- \(\beta_1, \beta_2, ..., \beta_n\) sont les coefficients des variables indépendantes, représentant l'effet de chaque variable sur \(Y\).
- \(\epsilon\) est le terme d'erreur, représentant la différence entre les valeurs observées et les valeurs prédites par le modèle.

### Estimation des Coefficients

Les coefficients sont estimés en utilisant la méthode des moindres carrés, qui vise à minimiser la somme des carrés des résidus (différences entre les valeurs observées et prédites). Cette approche mathématique permet d'obtenir une estimation des coefficients qui décrit le mieux la relation entre les variables dépendantes et indépendantes dans l'ensemble des données.

### Hypothèses Fondamentales

La régression linéaire multiple repose sur des hypothèses similaires à celles de la régression linéaire simple, avec quelques considérations supplémentaires dues à la présence de plusieurs variables indépendantes :

1. **Linéarité** : La relation entre les variables indépendantes et la variable dépendante est linéaire.
2. **Indépendance des erreurs** : Les erreurs (résidus) sont indépendantes les unes des autres.
3. **Homoscédasticité** : La variance des termes d'erreur est constante pour toutes les valeurs des variables indépendantes.
4. **Absence de multicollinéarité** : Les variables indépendantes ne doivent pas être trop fortement corrélées entre elles.
5. **Normalité des erreurs** : Les erreurs suivent une distribution normale.

### Évaluation du Modèle

L'évaluation d'un modèle de régression linéaire multiple peut inclure :

- **Coefficient de détermination ajusté (\(R^2\) ajusté)** : Contrairement au \(R^2\), le \(R^2\) ajusté prend en compte le nombre de prédicteurs dans le modèle, offrant une mesure plus précise de la qualité d'ajustement pour les modèles avec un grand nombre de variables.
- **Tests statistiques pour les coefficients** : Ces tests évaluent si chaque coefficient a une relation statistiquement significative avec la variable dépendante.
- **VIF (Variance Inflation Factor)** : Mesure l'augmentation de la variance d'un coefficient estimé due à la collinéarité. Un VIF élevé indique une forte multicollinéarité.
- **Analyse des résidus** : L'analyse des résidus peut révéler des violations des hypothèses du modèle, comme la non-linéarité, l'hétéroscédasticité, ou la présence de valeurs aberrantes.

### Exemple Pratique

Imaginons que nous voulons prédire le prix de vente d'une maison (\(Y\)) en fonction de sa superficie (\(X_1\)), du nombre de chambres (\(X_2\)), et de l'âge de la maison (\(X_3\)). Après avoir collecté les données, nous appliquons la régression linéaire multiple pour estimer les coefficients. L'équation résultante pourrait ressembler à :

\[ \text{Prix} = \beta_0 + \beta_1(\text{Superficie}) + \beta_2(\text{NbChambres}) + \beta_3(\text{Âge}) + \epsilon \]

Chaque coefficient nous indique l'effet attendu sur le prix de la maison d'une unité d'augmentation de la variable correspondante, tout en maintenant les autres variables constantes.

### Exemple en Python

Supposons que nous avons un ensemble de données avec plusieurs caractéristiques (variables indépendantes) :

```python
# Données d'exemple
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

# Pas besoin de séparer les données pour cet exemple simple

# Création et entraînement du modèle
model = LinearRegression().fit(X, y)

# Prédiction
y_pred = model.predict(X)

print("Coefficients:", model.coef_)
print("Ordonnée à l'origine:", model.intercept_)
```

## Autres Types de Régression

Oui, au-delà de la régression linéaire simple et multiple, il existe d'autres formes de régression linéaire adaptées à des situations spécifiques ou à des structures de données particulières. Voici quelques-unes de ces variantes, avec une description de leur utilisation et de leur fonctionnement.

### Régression Ridge (L2)

La régression Ridge, également connue sous le nom de régression de Tikhonov, est une technique utilisée pour analyser des données multicollinéaires. Elle ajoute un terme de pénalité égal au carré de la magnitude des coefficients à la fonction de coût. Ce terme de pénalité est multiplié par un paramètre \(\lambda\), qui contrôle l'importance de cette pénalité.

\[ \text{Minimiser : } \sum_{i=1}^{n} (y_i - \beta_0 - \sum_{j=1}^{p} \beta_j x_{ij})^2 + \lambda \sum_{j=1}^{p} \beta_j^2 \]

La régression Ridge est particulièrement utile pour réduire la complexité du modèle et prévenir le surajustement en réduisant les coefficients des variables corrélées.

### Régression Lasso (L1)

La régression Lasso (Least Absolute Shrinkage and Selection Operator) est similaire à la régression Ridge, mais elle utilise une pénalité L1 sur les coefficients, ce qui peut conduire à des coefficients exactement nuls. Cela signifie que la régression Lasso peut également effectuer une sélection de variables automatique en plus de la régularisation.

\[ \text{Minimiser : } \sum_{i=1}^{n} (y_i - \beta_0 - \sum_{j=1}^{p} \beta_j x_{ij})^2 + \lambda \sum_{j=1}^{p} |\beta_j| \]

La régression Lasso est utile lorsque nous avons un grand nombre de variables, et que nous souhaitons créer un modèle plus simple et plus interprétable en éliminant les variables non pertinentes.

### Régression Elastic Net

La régression Elastic Net combine les pénalités L1 et L2, utilisées respectivement dans les régressions Lasso et Ridge. Elle est particulièrement utile lorsque plusieurs variables sont corrélées entre elles. Elastic Net ajoute à la fois la somme des carrés des coefficients (comme dans Ridge) et la somme des valeurs absolues des coefficients (comme dans Lasso) à la fonction de coût.

\[ \text{Minimiser : } \sum_{i=1}^{n} (y_i - \beta_0 - \sum_{j=1}^{p} \beta_j x_{ij})^2 + \lambda_1 \sum_{j=1}^{p} |\beta_j| + \lambda_2 \sum_{j=1}^{p} \beta_j^2 \]

Cette méthode permet une régularisation plus flexible et peut récupérer un groupe de variables corrélées, là où Lasso pourrait n'en sélectionner qu'une seule.

### Régression Polynomiale

La régression polynomiale est une forme de régression linéaire où la relation entre la variable indépendante \(X\) et la variable dépendante \(Y\) est modélisée comme un polynôme de degré \(n\).

\[ Y = \beta_0 + \beta_1X + \beta_2X^2 + ... + \beta_nX^n + \epsilon \]

Bien que l'équation soit polynomiale, la régression polynomiale est considérée comme une forme de régression linéaire parce que l'équation est linéaire par rapport aux coefficients \(\beta\). La régression polynomiale est utile pour modéliser des relations non linéaires.

## Bonnes Pratiques

- **Normalisation des données** : Il est souvent utile de normaliser ou de standardiser les caractéristiques, surtout en régression multiple, pour améliorer la stabilité numérique du modèle.
- **Vérification des hypothèses** : La régression linéaire repose sur plusieurs hypothèses (linéarité, homoscédasticité, indépendance des erreurs, etc.). Il est important de les vérifier pour s'assurer de la validité du modèle.
- **Évaluation du modèle** : Utilisez des métriques comme le R², le RMSE (Root Mean Square Error) pour évaluer la performance de votre modèle de régression.
- **Sélection de variables** : Pour les régressions multiples, la sélection de variables peut être cruciale pour éviter le surajustement et améliorer l'interprétabilité du modèle.

## Exercices

1. Créez un modèle de régression linéaire simple pour prédire la consommation d'essence d'une voiture en fonction de sa vitesse.

