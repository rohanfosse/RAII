# Tutoriel LaTeX

## Introduction

LaTeX est un langage de balisage utilisé pour la préparation de documents. Il est largement utilisé dans les domaines de la recherche et de l'éducation pour la rédaction de rapports, d'articles, de thèses, etc. LaTeX est basé sur le langage de programmation TeX, qui a été créé par Donald Knuth dans les années 1970. LaTeX est un langage de programmation de haut niveau qui permet de structurer et de formater le contenu d'un document. Il est utilisé pour générer des documents de haute qualité avec une mise en page cohérente.

## Installation de LaTeX

### Installation de LaTeX sur Windows

1. **Installer MiKTeX :**
   MiKTeX est une distribution TeX pour Windows. Il est disponible en téléchargement gratuit sur [miktex.org](https://miktex.org/download).

2. **Installer un éditeur LaTeX :**
    Vous pouvez utiliser n'importe quel éditeur de texte pour écrire du code LaTeX. Cependant, il est recommandé d'utiliser un éditeur LaTeX dédié qui fournit des fonctionnalités supplémentaires telles que la coloration syntaxique, la complétion automatique, la compilation, etc. Voici quelques éditeurs LaTeX populaires :

    - [TeXstudio](https://www.texstudio.org/)
    - [TeXmaker](https://www.xm1math.net/texmaker/)
    - [TeXworks](https://www.tug.org/texworks/)
    - [Overleaf](https://www.overleaf.com/)

Dans ce tutoriel, et si vous ne souhaitez pas installer LaTeX sur votre ordinateur, nous utiliserons **Overleaf**, un éditeur LaTeX en ligne.

## Commencer avec Overleaf

1. **Création d'un compte Overleaf :**
   Allez sur [Overleaf](https://www.overleaf.com/) et créez un compte.

2. **Création d'un nouveau projet :**
   Une fois connecté, cliquez sur "New Project" et choisissez "Blank Project" pour démarrer un rapport à partir de zéro.

3. **Nommer votre projet :**
   Donnez un nom à votre projet pour pouvoir le retrouver facilement plus tard.

## Les bases de LaTeX

### Structure d'un document LaTeX

Un document LaTeX est divisé en deux parties principales :

#### Préambule

  Le préambule est la première partie du document. Il contient des informations sur le document, telles que le type de document, le titre, l'auteur, la date, etc. Il contient également des commandes qui affectent la mise en page du document.

  Voici un exemple de préambule :

  ```latex
    \documentclass[12pt]{article} % Type de document et taille de police
    \usepackage[utf8]{inputenc} % Encodage du document
    \usepackage[T1]{fontenc} % Encodage des caractères
    \usepackage[french]{babel} % Langue du document

    \title{Titre de votre document} % Titre du document
    \author{Votre Nom} % Auteur du document
    \date{\today} % Date du document
```

#### Corps

Le corps est la deuxième partie du document. Il contient le contenu du document, tel que le texte, les images, les tableaux, etc. Le corps commence par la commande `\begin{document}` et se termine par la commande `\end{document}`.

Voici un exemple de corps :

```latex
\begin{document}
    
\maketitle % Affiche le titre, l'auteur et la date
    
\tableofcontents % Affiche la table des matières
    
\chapter{Introduction} % Chapitre 1
\section{Contexte} % Section 1.1
\subsection{Sous-section} % Section 1.1.1
    
    % ... votre contenu ...
    
\chapter{Conclusion} % Chapitre 2
    
    % ... votre contenu ...
    
\end{document}
```

Dans cet exemple, nous avons utilisé les commandes `\section` et `\subsection` pour créer des sections et des sous-sections. Il est possible de créer des sous-sous-sections avec la commande `\subsubsection`.

### Mise en forme du texte



### Rédaction du Rapport sur Overleaf

1. **Utilisation de la structure de base :**
   Overleaf vous fournit un éditeur où vous pouvez écrire ou coller le code LaTeX. Voici un exemple de structure de rapport que vous pouvez utiliser :

   ```latex
   \documentclass[12pt]{report}

   \usepackage[utf8]{inputenc}
   \usepackage[T1]{fontenc}
   \usepackage[french]{babel}

   \title{Titre de votre Rapport}
   \author{Votre Nom}
   \date{\today} % Utilisez \today pour la date actuelle ou spécifiez une date

   \begin{document}

   \maketitle
   \tableofcontents

   \chapter{Introduction}
   \section{Contexte}
   \subsection{Sous-section}

   % ... votre contenu ...

   \chapter{Conclusion}

   % ... votre contenu ...

   \end{document}
   ```

2. **Compilation du rapport :**
   Overleaf compile automatiquement votre document à mesure que vous écrivez. Vous pouvez voir le PDF généré sur le côté droit de l'écran.

3. **Ajout de sections et de contenu :**
   Continuez à écrire votre rapport en ajoutant des chapitres, des sections et du texte. Vous pouvez également insérer des images, des tableaux et des références croisées.

4. **Gestion des erreurs :**
   Si Overleaf rencontre des erreurs lors de la compilation de votre document, il vous indiquera où elles se trouvent afin que vous puissiez les corriger.

### Ressources et Tutoriels sur Overleaf

- **Overleaf Documentation :**
  Overleaf offre une documentation complète et des guides pour apprendre LaTeX, disponibles sur leur [page Learn LaTeX](https://www.overleaf.com/learn).

- **Exemples de projets :**
  Overleaf dispose d'une galerie de [modèles de projets](https://www.overleaf.com/gallery) que vous pouvez utiliser comme point de départ.

- **Tutoriels interactifs :**
  Il y a des [tutoriels interactifs](https://www.overleaf.com/learn/latex/Tutorials) sur Overleaf qui vous guident à travers les fonctionnalités de base et avancées de LaTeX.

En utilisant Overleaf, vous avez non seulement accès à un éditeur LaTeX puissant, mais aussi à un système de gestion de versions et à la possibilité de collaborer en temps réel avec d'autres utilisateurs.
