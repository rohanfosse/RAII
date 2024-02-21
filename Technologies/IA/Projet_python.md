# Projet : Analyse des Performances des Joueurs Professionnels de CS:GO

Objectif : Utiliser le dataset des joueurs professionnels de CS:GO pour analyser et visualiser différentes statistiques de performance, afin d'identifier des tendances, des forces, et des faiblesses chez les joueurs et les équipes.

## Étapes du projet

### Préparation des données

- Téléchargez le dataset depuis Kaggle : https://www.kaggle.com/datasets/naumanaarif/csgo-pro-players-dataset
- Chargez les données dans un DataFrame pandas pour faciliter la manipulation et l'analyse.
- Nettoyez les données si nécessaire (traitement des valeurs manquantes, normalisation des noms des joueurs et des équipes, etc.).

### Analyse exploratoire des données (EDA)

- Obtenez un résumé statistique du dataset pour comprendre la distribution des principales statistiques (par exemple, nombre de kills, décès, assists, précision des tirs, etc.).
- Identifiez les joueurs et les équipes présents dans le dataset pour déterminer l'étendue des données.
- Explorez les corrélations entre les différentes statistiques pour identifier des relations intéressantes.

### Analyse des statistiques spécifiques

- Performance individuelle : Analysez les performances individuelles des joueurs en termes de kills, décès, assists, ratio kill/death (K/D), précision des tirs, et nombre de rounds joués. Identifiez les meilleurs performeurs dans chaque catégorie.
- Comparaison entre équipes : Comparez les performances moyennes des équipes, en utilisant des statistiques agrégées comme le nombre moyen de kills, le ratio K/D moyen par équipe, et la précision moyenne des tirs.
- Analyse des tendances : Identifiez des tendances dans les performances des joueurs et des équipes au fil du temps, en utilisant des statistiques de performance agrégées par mois ou par année.

### Visualisation des données

- Utilisez matplotlib ou seaborn pour créer des graphiques illustrant les performances individuelles et par équipe, comme des histogrammes, des boxplots, et des scatter plots.
- Illustrer la progression des joueurs avec des graphiques linéaires ou des graphiques à barres empilées pour montrer l'évolution des performances au fil du temps.
- Créez des graphiques de comparaison pour mettre en évidence les différences de performances entre les joueurs et les équipes.

### Livrables

- Un script Python qui effectue l'analyse et la visualisation des données.
- Un rapport ou un notebook Jupyter contenant les analyses statistiques, les visualisations, et une interprétation des résultats.

### Bonus

- Utilisez des techniques de machine learning pour prédire les performances futures des joueurs ou des équipes, en utilisant des modèles de régression ou de classification.
- Créez un tableau de bord interactif pour visualiser les performances des joueurs et des équipes, en utilisant des outils comme Dash ou Streamlit.

## Ressources

- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [Matplotlib Documentation](https://matplotlib.org/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/tutorial.html)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/user_guide.html)
