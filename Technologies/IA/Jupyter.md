Configurer Jupyter Notebook pour travailler sur des projets d'intelligence artificielle (IA) implique plusieurs étapes, allant de l'installation de Jupyter à la configuration de l'environnement de travail avec les bibliothèques nécessaires. Voici un guide étape par étape pour vous aider à démarrer.

### Étape 1 : Installation de Python et de pip

Jupyter nécessite Python, donc si vous ne l'avez pas déjà installé, téléchargez et installez la dernière version de Python depuis le site officiel. Assurez-vous d'inclure `pip`, le gestionnaire de paquets Python, lors de l'installation.

### Étape 2 : Installation de Jupyter Notebook via pip

Ouvrez votre terminal ou invite de commande et exécutez la commande suivante pour installer Jupyter Notebook :

```bash
pip install notebook
```

### Étape 3 : Lancement de Jupyter Notebook

Pour lancer Jupyter Notebook, exécutez :

```bash
jupyter notebook
```

Cette commande ouvrira automatiquement Jupyter dans votre navigateur web par défaut. Si cela ne se produit pas, copiez et collez l'URL affichée dans le terminal dans votre navigateur.

### Étape 4 : Installation des bibliothèques d'IA

Pour travailler sur des projets d'IA, vous aurez besoin de plusieurs bibliothèques spécialisées. Les plus courantes incluent :

- **NumPy** pour le calcul scientifique et le travail avec des tableaux.
- **Pandas** pour la manipulation et l'analyse des données.
- **Matplotlib** et **Seaborn** pour la visualisation des données.
- **Scikit-learn** pour le machine learning.
- **TensorFlow** ou **PyTorch** pour le deep learning.

Vous pouvez les installer via pip en exécutant les commandes suivantes dans votre terminal :

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
pip install tensorflow  # ou pytorch, selon votre préférence
```

### Étape 5 : Création d'un environnement virtuel (Optionnel)

Les environnements virtuels en Python sont des espaces isolés qui permettent de gérer séparément les dépendances pour différents projets. Utiliser des environnements virtuels est une pratique recommandée car cela aide à éviter les conflits entre les versions des bibliothèques nécessaires pour différents projets. Cela permet à chaque projet d'avoir ses propres dépendances, indépendamment des autres projets, ce qui facilite la gestion des packages et la reproductibilité des projets.

#### Pourquoi utiliser un environnement virtuel ?

1. **Isolation** : Chaque environnement virtuel est isolé des autres et contient ses propres copies indépendantes des bibliothèques et des interpréteurs Python. Cela signifie que les modifications apportées dans un environnement virtuel n'affectent pas les autres.

2. **Gestion des dépendances** : Les environnements virtuels facilitent la gestion des versions spécifiques des bibliothèques nécessaires pour un projet. Cela est particulièrement utile lorsque différents projets nécessitent différentes versions d'une même bibliothèque.

3. **Facilité d'installation** : Avec les environnements virtuels, il est facile de configurer un nouvel environnement de développement sur différentes machines. Cela simplifie le partage de projets et la collaboration entre développeurs.

4. **Reproductibilité** : Les environnements virtuels aident à garantir que les projets sont reproductibles, ce qui est crucial pour le débogage et le développement collaboratif. En fournissant un fichier `requirements.txt` qui liste toutes les dépendances, il est facile de recréer l'environnement de développement.

### Comment créer et utiliser un environnement virtuel ?

Voici comment créer et activer un environnement virtuel en utilisant `venv`, qui est inclus dans Python 3.3 et versions ultérieures :

1. **Création d'un environnement virtuel** :

   - Sur Windows :

     ```bash
     python -m venv mon_env
     ```

   - Sur macOS et Linux :

     ```bash
     python3 -m venv mon_env
     ```

   Cette commande crée un nouveau dossier `mon_env` qui contient l'interpréteur Python, ainsi qu'une copie de `pip`. Ce dossier stockera également toutes les bibliothèques installées dans l'environnement virtuel.

2. **Activation de l'environnement virtuel** :

   - Sur Windows :

     ```bash
     mon_env\Scripts\activate
     ```

   - Sur macOS et Linux :

     ```bash
     source mon_env/bin/activate
     ```

   Une fois activé, l'invite de commande indiquera généralement le nom de l'environnement virtuel, montrant que toutes les commandes `python` et `pip` exécutées dans cette session de terminal utiliseront l'interpréteur Python et les bibliothèques installées dans l'environnement virtuel.

3. **Désactivation de l'environnement virtuel** :

   Pour revenir à l'interpréteur Python global et désactiver l'environnement virtuel, utilisez :

   ```bash
   deactivate
   ```

4. **Installation des dépendances dans l'environnement virtuel** :

   Avec l'environnement virtuel activé, vous pouvez installer des bibliothèques spécifiques à votre projet en utilisant `pip`, sans affecter l'installation globale de Python sur votre système.

   ```bash
   pip install nom_du_package
   ```

5. **Création d'un fichier `requirements.txt`** :

   Pour faciliter le partage de votre environnement, vous pouvez générer un fichier `requirements.txt` qui liste toutes les bibliothèques installées dans votre environnement virtuel :

   ```bash
   pip freeze > requirements.txt
   ```

   Pour installer les dépendances à partir de ce fichier dans un autre environnement, utilisez :

   ```bash
   pip install -r requirements.txt
   ```

### Étape 6 : Démarrer un projet d'IA

Avec Jupyter lancé, créez un nouveau notebook via l'interface utilisateur de Jupyter. Vous pouvez maintenant importer les bibliothèques installées et commencer à travailler sur votre projet d'IA.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
# Importez d'autres bibliothèques selon vos besoins
```
