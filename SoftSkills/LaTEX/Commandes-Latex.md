# Commandes Latex

**Document Structure**

- `\documentclass{}`: Définir la classe du document (article, report, book, etc.).
- `\usepackage{}`: Inclure des paquets supplémentaires.
- `\begin{document}` et `\end{document}`: Marquer le début et la fin du contenu du document.

**Sectioning**

- `\section{}`: Commencer une nouvelle section.
- `\subsection{}`: Commencer une nouvelle sous-section.
- `\subsubsection{}`: Commencer une nouvelle sous-sous-section.
- `\paragraph{}`: Commencer un paragraphe.
- `\subparagraph{}`: Commencer un sous-paragraphe.

**Table des Matières**

- `\tableofcontents`: Insérer la table des matières.
- `\listoffigures`: Insérer la liste des figures.
- `\listoftables`: Insérer la liste des tableaux.

## Mise en Forme du Texte

**Text Formatting**

- `\textbf{}`: Mettre le texte en gras.
- `\textit{}`: Mettre le texte en italique.
- `\underline{}`: Souligner le texte.
- `\texttt{}`: Appliquer une police à chasse fixe.
- `\emph{}`: Mettre le texte en évidence (habituellement en italique).

**Font Size**

- `\tiny`, `\scriptsize`, `\footnotesize`, `\small`, `\normalsize`, `\large`, `\Large`, `\LARGE`, `\huge`, `\Huge`: Commandes pour changer la taille de la police.

**Alignment**

- `\begin{center}`, `\end{center}`: Centrer le texte.
- `\begin{flushleft}`, `\end{flushleft}`: Aligner le texte à gauche.
- `\begin{flushright}`, `\end{flushright}`: Aligner le texte à droite.

## Listes et Tableaux

**Listes**

- `\begin{itemize}`, `\end{itemize}`: Créer une liste à puces.
- `\begin{enumerate}`, `\end{enumerate}`: Créer une liste numérotée.
- `\begin{description}`, `\end{description}`: Créer une liste de descriptions.

**Tableaux**

- `\begin{table}`, `\end{table}`: Commencer et terminer un environnement de tableau flottant.
- `\begin{tabular}`, `\end{tabular}`: Commencer et terminer un environnement tabulaire pour le formatage des tableaux.

## Figures et Images

**Inclusion d'Images**

- `\usepackage{graphicx}`: Inclure le paquet pour la gestion des images.
- `\includegraphics{}`: Inclure une image.
- `\begin{figure}`, `\end{figure}`: Commencer et terminer un environnement de figure flottante.
- `\caption{}`: Ajouter une légende à une figure.

## Mathématiques

**Environnements Mathématiques**

- `$...$` ou `\( ... \)`: Mettre en forme le texte en mode mathématique (inline).
- `\[ ... \]` ou `$$ ... $$`: Mettre en forme le texte en mode mathématique (displayed).
- `\begin{equation}`, `\end{equation}`: Commencer et terminer un environnement d'équation numérotée.

**Symboles Mathématiques**

- `\alpha`, `\beta`, `\gamma`, etc.: Lettres grecques.
- `\times`, `\div`, `\pm`, etc.: Opérateurs mathématiques.
- `\frac{}{}`: Créer une fraction.
- `\sqrt{}`: Racine carrée.

## Références Croisées et Citations

**Références Croisées**

- `\label{}`: Mettre une étiquette pour référencer des éléments.
- `\ref{}`: Référencer des éléments avec une étiquette.
- `\pageref{}`: Référencer le numéro de page d'un élément étiqueté.

**Bibliographie et Citations**

- `\bibliographystyle{}`: Définir le style de la bibliographie.
- `\bibliography{}`: Insérer la bibliographie.
- `\cite{}`: Citer une référence.

## Autres

**Inclusion de Code Source**

- `\usepackage

{listings}`: Inclure le paquet pour lister le code.

- `\begin{lstlisting}`, `\end{lstlisting}`: Insérer un bloc de code.

**Hyperliens**

- `\usepackage{hyperref}`: Inclure le paquet pour la gestion des hyperliens.
- `\href{URL}{text}`: Créer un hyperlien.
- `\url{URL}`: Insérer une URL cliquable.

**Personnalisation de l'En-tête et du Pied de Page**

- `\usepackage{fancyhdr}`: Inclure le paquet pour les en-têtes et pieds de page personnalisés.
- `\pagestyle{fancy}`: Appliquer le style de page.
