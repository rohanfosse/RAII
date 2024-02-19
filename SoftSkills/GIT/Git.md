# Tutoriel Git

## Notions de base de Git

**Installation et configuration**

- Installer Git depuis le site officiel ou via un gestionnaire de paquets.
- Configurer l'utilisateur et l'e-mail avec `git config`.

**Création d'un nouveau dépôt**

- Utiliser `git init` pour initialiser un nouveau dépôt local.
- Ajouter des fichiers avec `git add` et créer un premier commit avec `git commit`.

**Cloner un dépôt**

- Cloner un dépôt existant avec `git clone [url]`.

## Travailler avec les branches

### Explications

Les branches dans Git sont essentielles pour gérer les fonctionnalités, les correctifs et les expérimentations dans des contextes isolés du reste du projet. Chaque branche représente une ligne de développement indépendante. La branche principale, généralement appelée `master` ou `main`, contient la version de production du projet, tandis que les autres branches servent à développer de nouvelles fonctionnalités ou à corriger des bugs.

#### Exemples

##### Création et changement de branche

```sh
git branch feature-x       # Crée une nouvelle branche nommée feature-x
git checkout feature-x     # Change pour la branche feature-x
# ou en une seule commande:
git checkout -b feature-x  # Crée et passe à la branche feature-x
```

##### Visualisation des branches

```sh
git branch                # Liste toutes les branches locales
git branch -a             # Liste toutes les branches, y compris les branches distantes
```

##### Fusionner une branche

```sh
git checkout main         # Se positionner sur la branche qui va recevoir la fusion
git merge feature-x       # Fusionne la branche feature-x dans la branche actuelle
```

##### Suppression de branche

```sh
git branch -d feature-x   # Supprime la branche feature-x (si elle a été fusionnée)
git branch -D feature-x   # Force la suppression de la branche feature-x
```

#### Exercices d'application

1. **Créer une branche pour une nouvelle fonctionnalité:**
   - Commencez par mettre à jour votre branche principale en exécutant `git checkout main` suivi de `git pull`.
   - Créez une nouvelle branche appelée `nouvelle-fonctionnalite` et passez dessus.
   - Ajoutez un nouveau fichier ou modifiez un fichier existant pour simuler le développement de la nouvelle fonctionnalité.
   - Committez vos changements sur cette branche.

2. **Simuler un conflit de fusion:**
   - Retournez sur la branche principale et faites une modification sur le même fichier que celui modifié sur votre branche de fonctionnalité.
   - Committez cette modification sur la branche principale.
   - Essayez de fusionner votre branche de fonctionnalité sur la branche principale. Git devrait signaler un conflit.
   - Résolvez ce conflit en éditant le fichier, puis en effectuant un commit de résolution de conflit.

3. **Rebaser votre branche de fonctionnalité:**
   - Plutôt que de fusionner directement, rebasez votre branche de fonctionnalité sur la branche principale avec `git rebase main` tout en étant sur votre branche `nouvelle-fonctionnalite`.
   - Si des conflits surviennent, résolvez-les et continuez le rebase.
   - Une fois le rebase terminé, fusionnez votre branche de fonctionnalité sur la branche principale avec `git merge nouvelle-fonctionnalite`.

## Notions avancées

### Gestion des Conflits dans Git

#### Explications

Les conflits dans Git surviennent lorsque deux branches ont des modifications contradictoires dans le même segment de code et qu'on tente de les fusionner. Git est incapable de résoudre automatiquement ces différences, et il requiert une intervention manuelle pour déterminer quelle version du code devrait être retenue.

#### Étapes pour Résoudre les Conflits

1. **Identifier le Conflit:**
   Lors d'une fusion ou d'un rebase, Git indiquera qu'il y a un conflit et marquera les fichiers concernés.

2. **Examiner le Conflit:**
   Les zones conflictuelles dans un fichier sont marquées avec des balises `<<<<<<<`, `=======`, et `>>>>>>>`. La partie entre `<<<<<<< HEAD` et `=======` est votre version, et celle entre `=======` et `>>>>>>>` est la version de la branche que vous tentez de fusionner.

3. **Résoudre le Conflit:**
   Ouvrez les fichiers en conflit et décidez manuellement quelles modifications conserver, supprimer ou combiner.

4. **Marquer comme Résolu:**
   Une fois les modifications effectuées, utilisez `git add [fichier]` pour marquer le conflit comme résolu.

5. **Terminer la Fusion:**
   Après avoir résolu tous les conflits, complétez l'opération avec `git commit` pour créer un commit de fusion.

#### Exemples

**Commandes Utiles**

```sh
git status            # Identifie les fichiers en conflit
git diff              # Montre les différences et conflits
git add [fichier]     # Marque le fichier comme résolu
git commit            # Crée un commit de résolution
```

#### Exercices d'application

1. **Provoquer et Résoudre un Conflit Simple:**
   - Modifiez la même ligne dans un fichier dans deux branches différentes.
   - Fusionnez l'une dans l'autre et observez le conflit.
   - Ouvrez le fichier, résolvez le conflit manuellement, puis terminez la fusion.

2. **Utilisation de Mergetool:**
   - Configurez un outil de fusion visuel avec `git config --global merge.tool [nom_de_loutil]`.
   - Lorsqu'un conflit survient, lancez l'outil avec `git mergetool`.
   - Résolvez le conflit en utilisant l'interface graphique, puis enregistrez et fermez l'outil.
   - Terminez la fusion avec un commit.

3. **Résolution de Conflits sur Plusieurs Fichiers:**
   - Provoquez des conflits dans plusieurs fichiers.
   - Utilisez `git status` pour identifier tous les fichiers en conflit.
   - Résolvez chaque conflit un par un, en vérifiant avec `git diff` après chaque résolution.
   - Utilisez `git add` pour marquer chaque fichier résolu et `git commit` pour finaliser.

#### Étapes pour Résoudre les Conflits avec VSCode

1. **Ouvrir le Fichier en Conflit:**
   VSCode marque les fichiers en conflit dans l'explorateur de fichiers avec un symbole C. Cliquer sur le fichier ouvre un éditeur avec les modifications côte à côte.

2. **Utiliser les Commandes de Résolution:**
   VSCode offre des options pour accepter la modification actuelle (`Accept Current Change`), accepter la modification entrante (`Accept Incoming Change`), accepter les deux modifications (`Accept Both Changes`) ou comparer les changements (`Compare Changes`).

3. **Résoudre Manuellement si Nécessaire:**
   Si les options automatiques ne suffisent pas, vous pouvez éditer le fichier manuellement dans l'éditeur de texte.

4. **Marquer le Conflit Comme Résolu:**
   Une fois le conflit résolu, enregistrez le fichier. Ensuite, dans la vue 'Source Control' de VSCode, stagez les changements avec un clic droit sur le fichier et sélectionnez `Stage Changes`.

5. **Finaliser avec un Commit:**
   Toujours dans la vue 'Source Control', tapez un message de commit et validez les modifications résolues avec `Commit`.

#### Exercices d'application

1. **Résoudre un Conflit Simple:**
   - Provoquez un conflit dans votre dépôt Git et ouvrez VSCode.
   - Allez dans l'onglet 'Source Control', cliquez sur le fichier en conflit pour l'ouvrir.
   - Utilisez les commandes de résolution de conflits pour choisir la bonne modification.
   - Enregistrez, stagez, et commitez la résolution.

2. **Résoudre des Conflits Complexes:**
   - Créez des conflits plus complexes en modifiant plusieurs blocs de code ou en ajoutant/supprimant des lignes.
   - Ouvrez les fichiers en conflit dans VSCode et résolvez chaque conflit un par un.
   - Après avoir résolu tous les conflits, sauvegardez les fichiers, puis stagez et commitez les modifications.

3. **Pratique avec des Branches Distantes:**
   - Simulez une situation où vous travaillez avec des branches distantes qui ont des modifications concurrentes.
   - Récupérez les changements avec `git pull` et gérez les conflits qui apparaissent dans VSCode.
   - Une fois les conflits résolus, poussez les modifications résolues sur le dépôt distant.


**Rebasing**

- Utiliser `git rebase [branche]` pour réappliquer les commits sur la pointe d'une autre branche, ce qui permet une histoire plus linéaire.

**Cherry Picking**

- Appliquer des commits spécifiques d'une branche à une autre avec `git cherry-pick [SHA_commit]`.

**Tags**

- Marquer des versions spécifiques avec `git tag [nom_du_tag]`.

**Stash**

- Mettre de côté des modifications non commitées avec `git stash`. Les récupérer avec `git stash pop`.

**Revert et Reset**

- Annuler des commits avec `git revert [SHA_commit]` ou revenir à un état antérieur avec `git reset`.

**Nettoyage de l'historique avec rebase interactif**

- Utiliser `git rebase -i` pour compresser, supprimer ou réordonner les commits.

**Hooks Git**

- Scripts personnalisables qui s'exécutent à certains événements Git, par exemple avant un commit ou avant un push.

## Liste des Commandes Git

