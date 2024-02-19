# Introduction à Python

## Partie 1: Installation de Python

### Étape 1: Téléchargement de Python

1. Allez sur le site officiel de Python : [python.org](https://python.org).
2. Naviguez jusqu'à la section "Downloads" et choisissez la dernière version de Python pour votre système d'exploitation (Windows, MacOS, Linux/UNIX).
3. Téléchargez l'installateur correspondant à votre système.

### Étape 2: Installation de Python

- **Windows:**
  1. Exécutez l'installateur téléchargé.
  2. Cochez la case "Add Python X.X to PATH" au début de l'installation pour vous assurer que Python est ajouté au PATH de votre système.
  3. Cliquez sur "Install Now".

- **MacOS/Linux:**
  1. Ouvrez un terminal.
  2. Changez le répertoire vers l'emplacement où le fichier a été téléchargé.
  3. Tapez `sudo bash ./Python-X.X.X-macosx10.x.pkg` pour MacOS ou `sudo apt-get install ./python-X.X.X` pour la plupart des distributions Linux, et suivez les instructions.

### Étape 3: Vérification de l'installation

1. Ouvrez un terminal ou une invite de commande.
2. Tapez `python --version` ou `python3 --version`.
3. Vous devriez voir la version de Python que vous venez d'installer s'afficher.

## Partie 2: Installation de Jupyter Notebook

### Étape 1: Installation de pip

`pip` est le gestionnaire de paquets de Python et devrait être installé avec Python. Pour vérifier si `pip` est installé, tapez `pip --version` dans votre terminal ou invite de commande.

### Étape 2: Installation de Jupyter

1. Dans votre terminal ou invite de commande, tapez la commande suivante pour installer Jupyter Notebook :

   ```bash
   pip install notebook
   ```

### Étape 3: Lancement de Jupyter Notebook

1. Dans le terminal ou l'invite de commande, tapez :

   ```bash
   jupyter notebook
   ```

2. Cela ouvrira Jupyter Notebook dans votre navigateur par défaut. Vous pouvez commencer à créer des notebooks pour écrire et exécuter du code Python.

## Partie 3: Bases de Python

Python est un langage de programmation puissant et facile à apprendre. Voici quelques concepts de base pour commencer :

- **Variables et Types de Données** : Python est un langage à typage dynamique, ce qui signifie que vous n'avez pas besoin de déclarer le type d'une variable lorsque vous la créez.

  ```python
  x = 5  # int
  y = "Hello, World!"  # str
  ```

- **Structures de Contrôle** : Les instructions conditionnelles et les boucles permettent de contrôler le flux d'exécution du programme.

  ```python
  # If statement
  if x > 0:
      print("x est positif")

  # For loop
  for i in range(5):
      print(i)
  ```

- **Fonctions** : Les fonctions sont définies avec le mot-clé `def` et sont utilisées pour encapsuler des blocs de code réutilisables.

  ```python
  def ma_fonction():
      print("Bonjour, Python !")
  
  ma_fonction()
  ```

- **Modules et Paquets** : Python permet d'importer des modules et des paquets pour étendre les fonctionnalités de base.

  ```python
  import math
  print(math.sqrt(16))
  ```