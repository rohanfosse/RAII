# Pense-bête des Commandes Git

## Configuration et Initialisation

**Configurer l'utilisateur**

- `git config --global user.name "Votre Nom"` : Définir le nom de l'utilisateur.
- `git config --global user.email "votre.email@example.com"` : Définir l'email de l'utilisateur.

**Initialisation et Clonage**

- `git init` : Initialiser un nouveau dépôt Git.
- `git clone [url]` : Cloner un dépôt depuis une URL.

## Modifications Locales

**Vérifier l'état et les différences**

- `git status` : Vérifier l'état actuel du dépôt.
- `git diff` : Montrer les différences non stagées.
- `git diff --staged` ou `git diff --cached` : Montrer les différences stagées mais non commitées.

**Stager et Commiter**

- `git add [fichier]` : Ajouter un fichier à l'espace de staging.
- `git add .` : Stager tous les changements.
- `git commit -m "message"` : Commiter les changements stagés avec un message.
- `git commit -am "message"` : Stager tous les changements suivis et commiter.

**Annuler des Modifications**

- `git checkout -- [fichier]` : Annuler les modifications non stagées sur un fichier.
- `git reset [fichier]` : Dés-stager un fichier tout en conservant les modifications.
- `git reset --hard` : Annuler tous les changements non commités, ATTENTION danger.

## Branches et Fusion

**Branches**

- `git branch` : Lister toutes les branches locales.
- `git branch [nom_de_la_branche]` : Créer une nouvelle branche.
- `git checkout [nom_de_la_branche]` : Changer de branche.
- `git branch -d [nom_de_la_branche]` : Supprimer une branche.

**Fusion et Rebase**

- `git merge [nom_de_la_branche]` : Fusionner une autre branche avec la branche courante.
- `git rebase [nom_de_la_branche]` : Re-appliquer les commits sur une autre branche.

## Partage et Mise à Jour

**Récupérer et Publier**

- `git fetch [alias]` : Télécharger tous les changements du dépôt distant.
- `git merge [alias]/[branche]` : Fusionner une branche distante dans la branche courante.
- `git pull` : `git fetch` suivi d'un `git merge`.
- `git push [alias] [branche]` : Publier les commits locaux sur une branche distante.
- `git push --tags` : Publier les tags.

## Inspection et Comparaison

**Logs et Histoire**

- `git log` : Afficher l'historique des commits.
- `git log --follow [fichier]` : Afficher les changements d'un fichier spécifique.
- `git diff [premier-branch]...[deuxième-branch]` : Comparer deux branches.

**Status et Logs Détaillés**

- `git status -s` ou `git status --short` : Afficher un statut concis des modifications.
- `git log --stat` : Afficher les statistiques de modifications pour chaque commit.
- `git log --graph` : Afficher un graphique des branches et des merges dans les logs.

## Annulation

**Annuler des Commits et des Fusions**

- `git commit --amend` : Modifier le dernier commit (non-publié).
- `git reset --soft HEAD^` : Annuler le dernier commit mais garder les modifications.
- `git reset --hard HEAD^` : Annuler le dernier commit et toutes les modifications.
- `git revert [SHA]` : Créer un nouveau commit qui annule les modifications spécifiées.

**Conflits**

- `git mergetool` : Ouvrir les conflits dans un outil de fusion visuel.
- `git add [fichier]` : Marquer les conflits comme résolus.