# Cours sur PowerShell

## Introduction à PowerShell

### Qu'est-ce que PowerShell?

PowerShell est un langage de script et un shell de ligne de commande développé par Microsoft. Il est utilisé pour l'automatisation des tâches administratives et la gestion de la configuration système.

### Pourquoi PowerShell est Important?

- **Automatisation** : Automatise des tâches répétitives, économisant du temps.
- **Gestion à Distance** : Permet de gérer des systèmes à distance.
- **Flexible** : Interagit avec une large gamme de technologies Microsoft et autres.

### Exemples de Scripts PowerShell dans des Scénarios du Monde Réel

Dans cette sous-section, nous allons explorer des exemples de scripts PowerShell qui peuvent être utilisés dans des situations courantes d'administration système. Ces scripts sont conçus pour résoudre des problèmes réels et rendre les tâches quotidiennes plus efficaces.

#### Exemple 1: Automatisation des Sauvegardes

La sauvegarde régulière des données critiques est une tâche importante pour tout administrateur système. Le script suivant automatise la sauvegarde d'un répertoire spécifique vers un emplacement de sauvegarde.

```powershell
# Définit les chemins source et de destination
$sourcePath = "C:\ImportantData"
$backupPath = "\\BackupServer\BackupFolder"

# Crée un nom de fichier de sauvegarde basé sur la date et l'heure actuelles
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupFileName = "Backup_$timestamp.zip"

# Crée une archive des données importantes
Compress-Archive -Path $sourcePath -DestinationPath "$backupPath\$backupFileName"
```

#### Exemple 2: Mise à Jour des Logiciels sur Plusieurs Serveurs

Dans un environnement avec plusieurs serveurs, il est crucial de s'assurer que tous les logiciels sont à jour. Le script suivant vérifie et installe les mises à jour sur une liste de serveurs.

```powershell
# Liste des serveurs à mettre à jour
$servers = @('Server1', 'Server2', 'Server3')

foreach ($server in $servers) {
    # Utilise Invoke-Command pour exécuter les mises à jour sur le serveur distant
    Invoke-Command -ComputerName $server {
        # Installe les mises à jour nécessaires
        Get-WindowsUpdate -Install -AcceptAll -AutoReboot
    }
}
```

#### Exemple 3: Surveillance du Réseau et Alertes

La surveillance du réseau est essentielle pour détecter les problèmes dès qu'ils surviennent. Ce script effectue un ping sur une série d'adresses IP et envoie une alerte si l'une d'elles ne répond pas.

```powershell
# Liste des adresses IP à surveiller
$ipAddresses = @('192.168.1.1', '192.168.1.2', '10.0.0.1')

foreach ($ip in $ipAddresses) {
    if (!(Test-Connection -IPAddress $ip -Count 1 -Quiet)) {
        # Envoie une alerte par e-mail
        Send-MailMessage -From 'admin@example.com' -To 'alert@example.com' `
            -Subject "Échec de la surveillance du réseau" `
            -Body "Le périphérique à l'adresse $ip ne répond pas." `
            -SmtpServer 'smtp.example.com'
    }
}
```

Ces scripts représentent des solutions concrètes à des problèmes courants en administration système et démontrent la puissance et la flexibilité de PowerShell pour l'automatisation et la gestion des tâches.

## Fondamentaux de PowerShell

### Interface de PowerShell

- **Console PowerShell** : Une interface en ligne de commande pour exécuter des scripts et des commandes.
- **ISE (Integrated Scripting Environment)** : Un éditeur de script avec des fonctionnalités avancées.

### Commandes de Base

- `Get-Command` : Trouve toutes les commandes disponibles.
- `Get-Help` : Fournit une aide sur les commandes.
- `Set-ExecutionPolicy` : Configure la politique d'exécution des scripts.

### Scripts

- Un script PowerShell est un fichier `.ps1` contenant une série de commandes.
- Les scripts permettent d'exécuter des séquences complexes de tâches automatiquement.

### Gestion de Fichiers

- `Get-ChildItem` : Liste les fichiers et dossiers.
- `Copy-Item` : Copie des fichiers et dossiers.
- `Remove-Item` : Supprime des fichiers et dossiers.

### Administration Système

- `Get-Service` : Liste tous les services en cours d'exécution sur un système.
- `Start-Service` et `Stop-Service` : Démarre ou arrête un service.

### Réseau

- `Test-Connection` : Effectue un ping sur un hôte pour vérifier la connectivité.

### Gestion des Utilisateurs

- `Get-LocalUser` : Liste les utilisateurs locaux.
- `New-LocalUser` : Crée un nouvel utilisateur local.
- `Remove-LocalUser` : Supprime un utilisateur local.

## Exemples de Scripts PowerShell

### Exemple 1

```powershell
# Ce script affiche "Hello World"
Write-Host "Hello World"
```

### Exemple 2

```powershell
# Ce script affiche les fichiers et dossiers dans le dossier courant
Get-ChildItem
```

### Exemple 3

```powershell
# Ce script affiche les utilisateurs locaux
Get-LocalUser
```

## Scripts Avancés et Automatisation

### Scripts Avancés en PowerShell


Dans cette section, nous allons explorer la création de scripts avancés en PowerShell, en utilisant des structures de contrôle, des fonctions, et la gestion des erreurs. Ces concepts sont essentiels pour créer des scripts plus complexes.

#### Utilisation de Variables

Les variables sont utilisées pour stocker des valeurs. Elles peuvent être de différents types, comme des nombres, des chaînes de caractères, ou des objets.

Voici une liste des types de variables les plus courants et de la syntaxe pour les déclarer:

| Type de Variable | Syntaxe |
| --- | --- |
| Nombre | `$number = 5` |
| Chaîne de Caractères | `$string = "Hello"` |
| Tableau | `$array = @("Hello", "World")` |
| Hashtable | `$hashtable = @{ "key" = "value" }` |
| Objet | `$object = New-Object -TypeName PSObject` |
| Booléen | `$boolean = $true` |
| Null | `$null = $null` |
| Sequence | `$sequence = 1..5` |

##### Les variables pré-définies

Il existe des variables pré-définies qui sont automatiquement créées par PowerShell. Elles sont utilisées pour stocker des informations sur le système.

Voici une liste des variables pré-définies les plus courantes:

| Variable | Description |
| --- | --- |
| `$true` | Booléen vrai |
| `$false` | Booléen faux |
| `$null` | Valeur nulle |
| `$HOME` | Dossier personnel de l'utilisateur |
| `$PSHOME` | Dossier d'installation de PowerShell |
| `$PSVersionTable` | Informations sur la version de PowerShell |
| `$PWD` | Dossier courant |
| `$PID` | ID du processus PowerShell |
| `$PROFILE` | Fichier de profil de l'utilisateur |
| `$PSCommandPath` | Chemin du script en cours d'exécution |
| `$PSModulePath` | Chemin des modules PowerShell |
| `$PSItem` | Élément en cours d'itération |
| `$PSBoundParameters` | Paramètres passés à une fonction |

##### Les variables d'environnement

Les variables d'environnement sont utilisées pour stocker des informations sur le système. Elles sont créées par le système d'exploitation et sont accessibles par tous les programmes.

Voici une liste (non-exhaustive) des variables d'environnement les plus courantes:

| Variable | Description |
| --- | --- |
| `$env:USERPROFILE` | Dossier personnel de l'utilisateur |
| `$env:PATH` | Chemin de recherche des exécutables |
| `$env:TEMP` | Dossier temporaire |
| `$env:COMPUTERNAME` | Nom de l'ordinateur |
| `$env:USERNAME` | Nom de l'utilisateur |
| `$env:USERDOMAIN` | Nom du domaine |
| `$env:OS` | Nom du système d'exploitation |

Vous pouvez afficher toutes les variables d'environnement avec la commande suivante:

```powershell
Get-ChildItem Env:
```

##### Les variables d'état

Les variables d'état sont utilisées pour stocker des informations sur l'état du système. Elles sont créées par PowerShell et sont accessibles par tous les programmes.

Voici une liste (non-exhaustive) des variables d'état les plus courantes:

| Variable | Description |
| --- | --- |
| `$?` | Booléen indiquant si la dernière commande a réussi |
| `$^` | Dernière commande exécutée |
| `$error` | Tableau contenant les erreurs |
| `$LASTEXITCODE` | Code de sortie de la dernière commande |
| `$input` | Tableau contenant les entrées de l'utilisateur |
| `$args` | Tableau contenant les arguments passés au script |
| `$MyInvocation` | Informations sur le script en cours d'exécution |
| `$_` | Élément en cours d'itération |

Vous pouvez afficher toutes les variables d'état avec la commande suivante:

```powershell
Get-Variable
```

#### Les opérateurs de comparaison

Les comparaisons sont utilisées pour comparer des valeurs. Elles sont couramment utilisées dans les structures de contrôle.

Voici une liste des opérateurs de comparaison les plus courants:

| Opérateur | Description |
| --- | --- |
| `-eq` | Égal à |
| `-ne` | Différent de |
| `-gt` | Plus grand que |
| `-ge` | Plus grand ou égal à |
| `-lt` | Plus petit que |
| `-le` | Plus petit ou égal à |

Les opérateurs de comparaison retournent un booléen (`$true` ou `$false`). Ils sont équivalents aux opérateurs de comparaison en Bash.

Par exemple, pour vérifier si deux nombres sont égaux:

```powershell
if (5 -eq 5) {
    Write-Host "Les nombres sont égaux"
}
```

#### Les opérateurs logiques

Les opérateurs logiques sont utilisés pour combiner des expressions booléennes. Ils sont couramment utilisés dans les structures de contrôle.

Voici une liste des opérateurs logiques les plus courants:

| Opérateur | Description |
| --- | --- |
| `-and` | ET |
| `-or` | OU |
| `-not` | NON |

Les opérateurs logiques retournent un booléen (`$true` ou `$false`). Ils sont équivalents aux opérateurs logiques en Bash.

Par exemple, pour vérifier si deux nombres sont égaux et plus grands que 5:

```powershell
if ((5 -eq 5) -and (5 -gt 5)) {
    Write-Host "Les nombres sont égaux et plus grands que 5"
}
```

#### Utilisation de Boucles

##### Boucle `foreach`

La boucle `foreach` est utilisée pour itérer sur une collection d'éléments. Elle exécute un bloc de commandes pour chaque élément de la collection. La syntaxe est la suivante:

```powershell
foreach ($item in $collection) {
    # Commandes
}
```

Les collections peuvent être des tableaux, des chaînes de caractères, ou des objets.

**Exemple**:

```powershell
$numbers = 1..5
foreach ($number in $numbers) {
    Write-Host "Le nombre est: $number"
}
```

Ce script affiche:

```text
Le nombre est: 1
Le nombre est: 2
Le nombre est: 3
Le nombre est: 4
Le nombre est: 5
```

##### Boucle `while`

La boucle `while` continue d'exécuter un bloc de commandes tant que la condition est vraie.

La syntaxe est la suivante:

```powershell
while ($condition) {
    # Commandes
}
```

**Exemple**:

```powershell
$count = 1
while ($count -le 5) {
    Write-Host "Compteur: $count"
    $count++
}
```

Ce script compte jusqu'à 5.

#### 2. Utilisation de Conditions

##### a. Instruction `if` - `else`

Permet d'exécuter des commandes basées sur des conditions. Si la condition est vraie, le bloc `if` est exécuté. Sinon, le bloc `else` est exécuté.

La syntaxe est la suivante:

```powershell
if ($condition) {
    # Commandes
} else {
    # Commandes
}
```

**Exemple**:

```powershell
$age = 20
if ($age -ge 18) { # Si l'âge est supérieur ou égal à 18
    Write-Host "Majeur"
} else {
    Write-Host "Mineur"
}
```

Ce script vérifie si une personne est majeure ou mineure. 

Il est possible d'ajouter des conditions supplémentaires avec l'instruction `elseif`:

```powershell
$age = 20
if ($age -ge 18) { # Si l'âge est supérieur ou égal à 18
    Write-Host "Majeur"
} elseif ($age -ge 16) { # Si l'âge est supérieur ou égal à 16
    Write-Host "Presque majeur"
} else {
    Write-Host "Mineur"
}
```

##### b. Instruction `switch`

Permet d'exécuter des commandes basées sur des conditions.

La syntaxe est la suivante:

```powershell
switch ($variable) {
    "valeur1" {
        # Commandes
    }
    "valeur2" {
        # Commandes
    }
    default {
        # Commandes
    }
}
```

**Exemple**:

```powershell
$age = 20
switch ($age) {
    18 {
        Write-Host "Majeur"
    }
    16 {
        Write-Host "Presque majeur"
    }
    default {
        Write-Host "Mineur"
    }
}
```

#### 3. Création de Fonctions

Les fonctions permettent de regrouper des commandes pour les réutiliser.

La syntaxe est la suivante:

```powershell
function Nom-De-La-Fonction {
    # Commandes
}
```

En PowerShell, les fonctions peuvent retourner des valeurs avec l'instruction `return`.

La syntaxe est la suivante:

```powershell
function Nom-De-La-Fonction {
    # Commandes
    return $valeur
}
```

Il est aussi possible de définir des paramètres pour les fonctions.

La syntaxe est la suivante:

```powershell
function Nom-De-La-Fonction($parametre1, $parametre2) {
    # Commandes
}
```

Pour appeler une fonction, il suffit d'utiliser son nom:

```powershell
Nom-De-La-Fonction
```

Si la fonction retourne une valeur, il est possible de l'afficher avec `Write-Host`:

```powershell
Write-Host (Nom-De-La-Fonction)
```

Si la fonction a des paramètres, il faut les spécifier:

```powershell
Nom-De-La-Fonction -parametre1 valeur1 -parametre2 valeur2
```

**Exemple**:

```powershell
function Get-Multiplication($a, $b) {
    return $a * $b
}
Write-Host (Get-Multiplication -a 5 -b 6)
```


#### 4. Gestion des Erreurs

La gestion des erreurs permet de capturer et de gérer les erreurs. Elle est couramment utilisée dans les scripts pour éviter les interruptions.

##### a. Blocs `try` - `catch`

Permet de capturer et de gérer les erreurs.

La syntaxe est la suivante:

```powershell
try {
    # Commandes
} catch {
    # Commandes
}
```

Il est possible de capturer des erreurs spécifiques:

```powershell
try {
    # Commandes
} catch [System.IO.IOException] {
    # Commandes
}
```

La liste des erreurs est disponible [ici](https://docs.microsoft.com/en-us/dotnet/api/system.io.ioexception?view=net-5.0).

**Exemple**:

```powershell
try {
    $result = 1 / 0
} catch {
    Write-Host "Une erreur s'est produite: $_"
}
```

Ce script tente une division par zéro et capture l'erreur.


### Exercices

#### Exercice 1

Créer un script qui affiche les nombres de 1 à 10.

#### Exercice 2

Créer un script qui affiche les nombres de 1 à 10, sauf 5.

#### Exercice 3

Créer un script qui liste les fichiers et dossiers dans le dossier courant, et qui affiche le nombre de fichiers et de dossiers.

#### Exercice 4

Créer un script qui demande à l'utilisateur son nom et son âge, et qui affiche un message de bienvenue.

#### Exercice 5

Créer un script qui demande l'age de l'utilisateur. Si l'input n'est pas un nombre, afficher un message d'erreur.

Indice : Utiliser la fonction `IsNumeric()`.

### Automatisation des Tâches

- Créer des scripts pour automatiser des tâches comme les mises à jour logicielles, la surveillance du réseau, ou la gestion des utilisateurs.

## Bonnes Pratiques

### Sécurité

- Toujours vérifier les scripts avant de les exécuter.
- Utiliser `Set-ExecutionPolicy` avec précaution pour éviter l'exécution de scripts malveillants.

### Lisibilité et Maintenance

- Commenter le code pour expliquer la fonction des scripts.
- Garder les scripts organisés et facilement accessibles.

### Dépannage et Gestion des Erreurs Communes en PowerShell

Le dépannage est un aspect crucial de la gestion de scripts PowerShell. Comprendre et résoudre les erreurs courantes est essentiel pour maintenir des systèmes sains et automatisés. Cette section couvre des stratégies pour identifier et corriger les erreurs communes en PowerShell.

#### Identification des Erreurs

Les erreurs en PowerShell peuvent généralement être classées en deux catégories : erreurs d'exécution et erreurs de script. Les erreurs d'exécution sont souvent liées à des problèmes avec l'environnement, comme un chemin de fichier incorrect ou des permissions insuffisantes. Les erreurs de script sont généralement dues à des fautes de syntaxe ou à une logique défectueuse dans le script lui-même.

Pour identifier les erreurs, PowerShell fournit plusieurs variables automatiques :

- `$Error` : un tableau contenant les erreurs de la session actuelle.
- `$?` : une variable qui retourne `$false` si la dernière opération a échoué.
- `$LASTEXITCODE` : le code de sortie de la dernière commande exécutée dans le shell.

#### Stratégies de Dépannage

##### Utilisation de Verbose et Debug

L'utilisation des paramètres `-Verbose` et `-Debug` peut aider à suivre le déroulement d'un script. `-Verbose` affiche des informations supplémentaires sur les actions effectuées par le script, tandis que `-Debug` sollicite une confirmation avant d'exécuter chaque commande.

##### Logging

La journalisation est un autre outil important pour le dépannage. Les scripts peuvent être écrits pour enregistrer leurs actions et les erreurs dans un fichier de journal, facilitant ainsi le suivi des problèmes.

#### Correction des Erreurs Communes

##### Chemins de Fichier Incorrects

Veillez à utiliser des chemins absolus ou à gérer correctement les chemins relatifs en utilisant des variables comme `$PSScriptRoot` pour les scripts ou `$PWD` pour le répertoire actuel.

##### Permissions Insuffisantes

Assurez-vous que le script est exécuté avec les bonnes permissions, en utilisant `Run as Administrator` si nécessaire, ou en ajustant les politiques d'exécution avec `Set-ExecutionPolicy`.

##### Erreurs de Syntaxe

Les erreurs de syntaxe peuvent souvent être résolues en utilisant `Get-Help` pour vérifier l'utilisation correcte des commandes, et en prêtant attention aux messages d'erreur, qui indiquent souvent la ligne et le caractère où l'erreur a été détectée.

##### Problèmes de Connexion Réseau

Pour les scripts qui dépendent de la connectivité réseau, utilisez `Test-Connection` pour confirmer la connectivité avant de tenter des opérations réseau.

#### Outils de Dépannage

- **ISE (Integrated Scripting Environment)** : Dispose d'un débogueur intégré pour les scripts PowerShell.
- **Visual Studio Code** : Un éditeur de code avec une extension PowerShell pour le débogage.
- **PowerShell Console** : Offre un affichage en temps réel des erreurs et des sorties de script.

## Conclusion

PowerShell est un outil puissant pour l'administration système, offrant une grande flexibilité et capacité d'automatisation. Avec la pratique, il devient un allié inestimable pour tout administrateur de système.
