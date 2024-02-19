# Introduction à Docker

Docker est une plateforme open-source qui permet de développer, de déployer et d'exécuter des applications dans des conteneurs. Les conteneurs sont des environnements légers et portables qui permettent d'exécuter des applications de manière isolée. Docker permet de créer des conteneurs à partir d'images, qui sont des modèles de conteneurs préconfigurés. Ces images peuvent être partagées et réutilisées, ce qui facilite le déploiement d'applications.

## Installation

Pour installer Docker, vous pouvez suivre les instructions disponibles sur le site officiel de Docker : [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).

### Installation sur Linux

Pour installer Docker sur Linux, vous pouvez utiliser le gestionnaire de paquets de votre distribution. Par exemple, sur Ubuntu, vous pouvez exécuter les commandes suivantes :

```sh
sudo apt update
sudo apt install docker.io
```

### Installation sur Windows

Pour installer Docker sur Windows, vous pouvez télécharger Docker Desktop à partir du site officiel de Docker : [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop).

### Installation sur macOS avec Homebrew

Si vous utilisez macOS, vous pouvez installer Docker à l'aide de Homebrew en exécutant la commande suivante :

```sh
brew install --cask docker
```

## A quoi sert Docker ?

Docker est utilisé pour créer, déployer et exécuter des applications dans des conteneurs. Voici quelques cas d'utilisation courants de Docker :

- **Développement d'applications :** Docker permet de créer des environnements de développement isolés, ce qui facilite la mise en place de projets complexes avec des dépendances spécifiques.

- **Déploiement d'applications :** Docker permet de packager des applications avec toutes leurs dépendances dans des conteneurs, ce qui facilite le déploiement sur des serveurs ou des services cloud.

- **Tests et intégration continue :** Docker permet de créer des environnements de test isolés, ce qui facilite l'exécution de tests automatisés et l'intégration continue.

- **Microservices :** Docker facilite la création et le déploiement de microservices, qui sont des applications modulaires et indépendantes.


## Le vocabulaire de Docker

Avant de commencer à utiliser Docker, il est important de comprendre quelques termes clés :

- **Conteneur :** Un conteneur est une instance d'une image Docker. Il s'agit d'un environnement isolé qui contient une application et toutes ses dépendances.

- **Image :** Une image Docker est un modèle de conteneur préconfiguré. Elle contient le code source, les bibliothèques, les dépendances et les fichiers de configuration nécessaires pour exécuter une application.

- **Dockerfile :** Un Dockerfile est un fichier de configuration qui décrit comment construire une image Docker. Il contient des instructions pour copier des fichiers, installer des dépendances, définir des variables d'environnement, etc.

- **Registre :** Un registre Docker est un service qui permet de stocker, de partager et de télécharger des images Docker. Le registre public de Docker, appelé Docker Hub, est un endroit où vous pouvez trouver des images prêtes à l'emploi pour de nombreuses applications et services.

- **Compose :** Docker Compose est un outil qui permet de définir et de gérer des applications multi-conteneurs. Il utilise un fichier de configuration YAML pour décrire les services, les réseaux et les volumes nécessaires pour exécuter une application.

## Utilisation de Docker

Une fois Docker installé, vous pouvez utiliser la ligne de commande `docker` pour gérer des conteneurs, des images et d'autres ressources Docker. Voici quelques commandes utiles pour commencer :

### Vérifier la version de Docker

Pour vérifier la version de Docker installée sur votre système, vous pouvez exécuter la commande suivante :

```sh
docker --version
```

### Lister les images Docker

Pour lister les images Docker disponibles sur votre système, vous pouvez exécuter la commande suivante :

```sh
docker images
```

### Lister les conteneurs Docker

Pour lister les conteneurs Docker en cours d'exécution sur votre système, vous pouvez exécuter la commande suivante :

```sh
docker ps
```

### Créer un conteneur à partir d'une image

Pour créer un conteneur à partir d'une image Docker, vous pouvez exécuter la commande suivante :

```sh
docker run -it --name mon-conteneur ubuntu:latest /bin/bash
```

Cette commande crée un nouveau conteneur à partir de l'image `ubuntu:latest` et ouvre un terminal interactif dans le conteneur. Le paramètre `-it` indique que le terminal est interactif (c'est à dire qu'il accepte les entrées de l'utilisateur) et que le flux de sortie est attaché au terminal. Le paramètre `--name` permet de donner un nom au conteneur.

### Arrêter et supprimer un conteneur

Pour arrêter un conteneur en cours d'exécution, vous pouvez exécuter la commande suivante :

```sh
docker stop mon-conteneur
```

Pour supprimer un conteneur, vous pouvez exécuter la commande suivante :

```sh
docker rm mon-conteneur
```

### Construire une image à partir d'un Dockerfile

Pour construire une image Docker à partir d'un Dockerfile, vous pouvez exécuter la commande suivante :

```sh
docker build -t mon-image:latest .
```

Cette commande construit une nouvelle image à partir du Dockerfile situé dans le répertoire courant et lui donne le tag `mon-image:latest`.

### Publier une image sur Docker Hub

Pour publier une image Docker sur Docker Hub, vous pouvez exécuter les commandes suivantes :

```sh
docker login
docker push mon-image:latest
```

La commande `docker login` vous permet de vous connecter à votre compte Docker Hub. La commande `docker push` publie l'image `mon-image:latest` sur Docker Hub.

## Exemples de Dockerfile

### Application Node.js

Voici un exemple de Dockerfile qui décrit comment construire une image Docker pour une application Node.js :

```Dockerfile
# Utiliser une image de base
FROM node:14

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY package.json package-lock.json ./

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers
COPY . .

# Exposer le port 3000
EXPOSE 3000

# Commande par défaut
CMD ["npm", "start"]
```

Ce Dockerfile utilise l'image de base `node:14` comme point de départ, définit le répertoire de travail, copie les fichiers de l'application, installe les dépendances, expose le port 3000 et définit la commande par défaut pour démarrer l'application.

### Application Python ML

Voici un exemple de Dockerfile qui décrit comment construire une image Docker pour une application Python de machine learning :

```Dockerfile
# Utiliser une image de base
FROM python:3.8

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY requirements.txt ./

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le reste des fichiers
COPY . .

# Commande par défaut
CMD ["python", "app.py"]
```

Ce Dockerfile utilise l'image de base `python:3.8` comme point de départ, définit le répertoire de travail, copie les fichiers de l'application, installe les dépendances et définit la commande par défaut pour démarrer l'application.

## Ressources supplémentaires

- [Documentation officielle de Docker](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/) : Registre public de Docker
- [Docker Compose](https://docs.docker.com/compose/) : Outil pour définir et gérer des applications multi-conteneurs
- [Docker Swarm](https://docs.docker.com/engine/swarm/) : Outil pour déployer et gérer des clusters de conteneurs Docker
- [Kubernetes](https://kubernetes.io/) : Plateforme open-source pour automatiser le déploiement, la mise à l'échelle et la gestion des applications conteneurisées
- [Awesome Compose](https://github.com/docker/awesome-compose) : Collection de modèles Docker Compose pour différents services et applications
