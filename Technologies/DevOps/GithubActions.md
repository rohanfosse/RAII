# Introduction à GitHub Actions

GitHub Actions est un outil d'automatisation qui permet de construire, tester, et déployer votre code directement depuis GitHub. Il facilite l'intégration et la livraison continues (CI/CD) pour les projets logiciels.

## Qu'est-ce que GitHub Actions?

GitHub Actions est un service d'automatisation de workflow qui permet aux développeurs de définir des séries d'instructions (appelées "actions") dans leurs dépôts GitHub. Ces actions peuvent être déclenchées par différents événements sur GitHub, tels que le push d'un commit, la création d'une pull request ou la publication d'une release.

## Pourquoi utiliser GitHub Actions?

- **Automatisation du workflow**: Automatisez des tâches répétitives telles que les tests, le build, et le déploiement de votre code.
- **Intégration et livraison continues (CI/CD)**: Intégrez et déployez automatiquement votre code à chaque push ou pull request, assurant une livraison rapide et fiable.
- **Personnalisable et flexible**: Créez des workflows personnalisés pour répondre aux besoins spécifiques de votre projet.
- **Écosystème riche**: Utilisez des actions pré-construites disponibles dans le GitHub Marketplace ou créez les vôtres.

## Composants clés de GitHub Actions

### Workflows

Les workflows sont des processus automatisés que vous définissez dans votre dépôt GitHub. Ils sont configurés à l'aide de fichiers YAML (.yml ou .yaml) situés dans le répertoire `.github/workflows` de votre dépôt.

#### Exemple de fichier de workflow

```yaml
name: CI # Nom du workflow

on: [push] # Événement déclencheur

jobs: # Jobs à exécuter
  build:
    runs-on: ubuntu-latest # Runner à utiliser

    steps:
    - uses: actions/checkout@v2 # Action pour récupérer le code source
    - name: Set up Node.js # Étape pour configurer Node.js
      uses: actions/setup-node@v1 # Action pour configurer Node.js
      with:
        node-version: '12.x' # Version de Node.js à utiliser
    - name: Install dependencies # Étape pour installer les dépendances
      run: npm install # Commande pour installer les dépendances
    - name: Run tests # Étape pour exécuter les tests
      run: npm test # Commande pour exécuter les tests
```

### Événements

Un workflow est déclenché par un événement spécifique sur GitHub, tel qu'un push, une pull request, ou un événement planifié (cron). Vous pouvez configurer des workflows pour écouter un ou plusieurs événements.

#### Exemple d'événement de déclenchement

```yaml
on: 
  push:
    branches:
      - main
      - develop
  pull_request:
    branches:
      - main
```

### Jobs

Un workflow peut contenir un ou plusieurs jobs. Les jobs sont des ensembles d'étapes qui s'exécutent sur le même runner. Par défaut, les jobs s'exécutent en parallèle, mais vous pouvez les configurer pour qu'ils s'exécutent de manière séquentielle.

#### Exemple de jobs

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Build and test
        run: |
          npm install
          npm test
  deploy:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to production
        run: |
          npm run build
          npm run deploy
```

### Étapes

Les étapes sont des actions individuelles que vous pouvez exécuter dans un job. Une étape peut être une tâche simple (comme exécuter une commande shell) ou une action réutilisable.

#### Exemple d'étapes

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v2
  - name: Set up Node.js
    uses: actions/setup-node@v1
    with:
      node-version: '12.x'
  - name: Install dependencies
    run: npm install
  - name: Run tests
    run: npm test
```

### Actions

Les actions sont des unités réutilisables de code qui peuvent être exécutées dans une étape d'un job. Vous pouvez utiliser des actions pré-existantes du GitHub Marketplace ou créer les vôtres.

#### Exemple d'action

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v2
  - name: Set up Node.js
    uses: actions/setup-node@v1
    with:
      node-version: '12.x'
  - name: Install dependencies
    run: npm install
  - name: Run tests
    run: npm test
```

### Runners

Les runners sont des serveurs qui exécutent vos workflows. GitHub offre des runners hébergés gratuits pour Linux, Windows, et macOS. Vous pouvez également héberger vos propres runners pour des besoins spécifiques.

## Création de votre premier Workflow

1. **Créez un fichier de workflow**: Dans votre dépôt GitHub, créez un dossier `.github/workflows` et ajoutez un fichier YAML pour définir votre workflow.
2. **Définissez un événement de déclenchement**: Spécifiez l'événement qui déclenchera votre workflow (par exemple, `on: push`).
3. **Ajoutez des jobs et des étapes**: Définissez les jobs à exécuter et les étapes à l'intérieur de ces jobs. Utilisez des actions pour exécuter des tâches spécifiques.
4. **Testez votre workflow**: Effectuez l'événement déclencheur (par exemple, poussez un commit) pour voir votre workflow en action.

## Bonnes pratiques

- **Utilisez des secrets pour stocker des données sensibles**: Stockez des données telles que des tokens d'accès et des mots de passe dans les secrets GitHub au lieu de les inclure en texte clair dans vos fichiers de workflow.
- **Réutilisez les actions lorsque c'est possible**: Utilisez des actions pré-construites du GitHub Marketplace pour éviter de réinventer la roue.
- **Optimisez l'exécution des workflows**: Minimisez le temps d'exécution en parallélisant les jobs et en utilisant des caches pour les dépendances.

## Ressources supplémentaires

- **Documentation officielle**: La documentation officielle de GitHub Actions est une excellente ressource pour approfondir vos connaissances.
- **GitHub Marketplace**: Parcourez le Marketplace pour trouver des actions qui peuvent être utilisées dans vos workflows.
- **Communauté GitHub**: Rejoignez la communauté GitHub pour poser des questions, partager des astuces, et obtenir de l'aide sur l'utilisation de GitHub Actions.