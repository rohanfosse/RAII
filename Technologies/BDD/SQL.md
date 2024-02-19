# SQL

# Introduction à SQL

SQL, pour "Structured Query Language", est un langage de programmation standardisé conçu pour la gestion et la manipulation de systèmes de gestion de bases de données relationnelles (SGBDR). Depuis sa normalisation par l'American National Standards Institute (ANSI) et l'International Organization for Standardization (ISO), SQL est devenu le fondement inébranlable de la manipulation et de l'interrogation de données relationnelles.

Les bases de données relationnelles reposent sur le modèle relationnel, une approche intuitive qui organise les données en tables composées de lignes et de colonnes. Ces tables facilitent la représentation des relations entre les types de données variés, permettant ainsi une analyse et une gestion efficaces des ensembles de données complexes. SQL offre les moyens de définir, de manipuler, et de contrôler les données au sein de ces bases de données avec une précision et une flexibilité remarquables.

Le langage SQL s'articule autour de divers éléments syntaxiques, y compris des commandes pour la définition de données (DDL), la manipulation de données (DML), et la gestion des transactions. Ces éléments sont fondamentaux non seulement pour l'administration quotidienne des données mais aussi pour fournir les moyens d'effectuer des analyses statistiques et de récupérer des informations dans le cadre de décisions opérationnelles et stratégiques.

À travers ce document, nous explorerons les principes de SQL, en détaillant son application dans la création de structures de données robustes, l'optimisation des requêtes pour la récupération de données, et l'évaluation des performances des transactions. Notre objectif est d'offrir aux étudiants et professionnels de l'informatique une compréhension approfondie de SQL, en soulignant son rôle indispensable dans le domaine de la science des données et de l'ingénierie logicielle.

## Fondamentaux de SQL

Le langage SQL repose sur des concepts fondamentaux qui constituent les briques de base de la gestion des bases de données relationnelles. Ces concepts incluent la définition de données, la manipulation de données, et l'intégrité des données, qui sont tous essentiels pour la création et la maintenance d'une base de données structurée et fiable.

### Types de Données en SQL

SQL définit un ensemble riche de types de données qui permettent une représentation précise des informations. Les types de données standards tels que `INTEGER`, `VARCHAR`, `BOOLEAN`, et `DATE` sont conçus pour accommoder les besoins diversifiés de stockage de données, allant des simples nombres entiers aux chaînes de caractères complexes et aux structures temporelles.

Voici un tableau récapitulatif des types de données les plus courants en SQL :

| Type de Données | Description |
| --------------- | ----------- |
| `INTEGER` | Entier signé de 32 bits |
| `BIGINT` | Entier signé de 64 bits |
| `SMALLINT` | Entier signé de 16 bits |
| `DECIMAL` | Nombre décimal de précision variable |
| `NUMERIC` | Nombre décimal de précision variable |
| `REAL` | Nombre à virgule flottante de 32 bits |
| `DOUBLE PRECISION` | Nombre à virgule flottante de 64 bits |
| `CHAR` | Chaîne de caractères de longueur fixe |
| `VARCHAR` | Chaîne de caractères de longueur variable |
| `TEXT` | Chaîne de caractères de longueur variable |
| `BOOLEAN` | Valeur booléenne |
| `DATE` | Date |
| `TIME` | Heure |
| `TIMESTAMP` | Date et heure |
| `INTERVAL` | Intervalle de temps |



### Structure de Base des Données

Au cœur du SQL se trouve la table, l'entité qui contient les données sous forme de lignes et de colonnes. Chaque colonne dans une table est conçue pour contenir un type de données spécifique, tandis que chaque ligne représente un enregistrement unique contenant les données réelles.

#### Création de Tables

La création de tables est réalisée à travers la commande `CREATE TABLE`, qui définit non seulement les colonnes et leurs types mais aussi diverses contraintes qui peuvent être appliquées pour garantir l'intégrité et la validité des données.

La syntaxe de base de la commande `CREATE TABLE` est la suivante :

```sql
CREATE TABLE table_name (
    column_1 data_type,
    column_2 data_type,
    column_3 data_type,
    ...
);
```

Voici un exemple de création d'une table `users` avec trois colonnes :

```sql

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INTEGER
);
```

#### Insertion de Données

Une fois les tables créées, la commande `INSERT INTO` est utilisée pour peupler ces tables avec des données. Cette opération est cruciale pour le début de la gestion des informations au sein de la base de données.

La syntaxe de base de la commande `INSERT INTO` est la suivante :

```sql
INSERT INTO table_name (column_1, column_2, column_3, ...)
VALUES (value_1, value_2, value_3, ...);
```

Voici un exemple d'insertion de données dans la table `users` :

```sql
INSERT INTO users (id, name, age)
VALUES (1, 'John Doe', 25);
```

#### Sélection de Données

La commande `SELECT` est utilisée pour récupérer des données à partir d'une table. Cette commande est essentielle pour l'analyse et la gestion des données, car elle permet de récupérer des informations spécifiques à partir de tables complexes.

La syntaxe de base de la commande `SELECT` est la suivante :

```sql
SELECT column_1, column_2, column_3, ... FROM table_name;
```

Voici un exemple de sélection de données à partir de la table `users` :

```sql
SELECT name, age FROM users;
```

#### Mise à Jour de Données

La commande `UPDATE` est utilisée pour modifier les données existantes dans une table. Cette commande est essentielle pour la gestion des données, car elle permet de mettre à jour les informations existantes en fonction des besoins de l'application.

La syntaxe de base de la commande `UPDATE` est la suivante :

```sql
UPDATE table_name
SET column_1 = value_1, column_2 = value_2, ...
WHERE condition;
```

Voici un exemple de mise à jour de données dans la table `users` :

```sql
UPDATE users
SET age = 26
WHERE id = 1;
```

### La Clause WHERE

La clause `WHERE` est utilisée pour filtrer les données récupérées à partir d'une table. Cette clause est essentielle pour la gestion des données, car elle permet de récupérer des informations spécifiques en fonction des besoins de l'application.

La syntaxe de base de la clause `WHERE` est la suivante :

```sql
SELECT column_1, column_2, column_3, ...
FROM table_name
WHERE condition;
```

Voici un exemple de sélection de données à partir de la table `users` :

```sql
SELECT name, age FROM users WHERE age > 25;
```

### La Clause ORDER BY

La clause `ORDER BY` est utilisée pour trier les données récupérées à partir d'une table. Cette clause est essentielle pour la gestion des données, car elle permet de récupérer des informations spécifiques en fonction des besoins de l'application.

La syntaxe de base de la clause `ORDER BY` est la suivante :

```sql
SELECT column_1, column_2, column_3, ...
FROM table_name
ORDER BY column_1, column_2, ... ASC|DESC;
```

Voici un exemple de sélection de données à partir de la table `users` :

```sql
SELECT name, age FROM users ORDER BY age DESC;
```

### La Clause GROUP BY

La clause `GROUP BY` est utilisée pour regrouper les données récupérées à partir d'une table. Cette clause est essentielle pour la gestion des données, car elle permet de récupérer des informations spécifiques en fonction des besoins de l'application.

La syntaxe de base de la clause `GROUP BY` est la suivante :

```sql
SELECT column_1, column_2, column_3, ...
FROM table_name
GROUP BY column_1, column_2, ...;
```

Voici un exemple de sélection de données à partir de la table `users` :

```sql
SELECT age, COUNT(*) FROM users GROUP BY age;
```

### La Clause HAVING

La clause `HAVING` est utilisée pour filtrer les données récupérées à partir d'une table. Cette clause est essentielle pour la gestion des données, car elle permet de récupérer des informations spécifiques en fonction des besoins de l'application.

La syntaxe de base de la clause `HAVING` est la suivante :

```sql
SELECT column_1, column_2, column_3, ...
FROM table_name
GROUP BY column_1, column_2, ...
HAVING condition;
```

Voici un exemple de sélection de données à partir de la table `users` :

```sql
SELECT age, COUNT(*) FROM users GROUP BY age HAVING COUNT(*) > 1;
```

### La Clause LIMIT

La clause `LIMIT` est utilisée pour limiter le nombre de données récupérées à partir d'une table. Cette clause est essentielle pour la gestion des données, car elle permet de récupérer des informations spécifiques en fonction des besoins de l'application.

La syntaxe de base de la clause `LIMIT` est la suivante :

```sql
SELECT column_1, column_2, column_3, ...
FROM table_name
LIMIT number;
```

Voici un exemple de sélection de données à partir de la table `users` :

```sql
SELECT name, age FROM users LIMIT 10;
```

---

## Exercice d'Application SQL

### Contexte

Une université souhaite organiser et stocker les informations concernant les étudiants, les cours proposés et les inscriptions aux cours. Vous êtes chargé de créer la structure de base de données nécessaire pour stocker ces informations en utilisant SQL.

### Exercice 1: Création de Tables

1. Créez une table `Etudiants` avec les colonnes suivantes :
   - `EtudiantID` (clé primaire, entier, auto-incrémenté)
   - `Nom` (varchar de 50 caractères)
   - `Prenom` (varchar de 50 caractères)
   - `DateNaissance` (date)
   - `Email` (varchar de 100 caractères, unique)

2. Créez une table `Cours` avec les colonnes suivantes :
   - `CoursID` (clé primaire, entier, auto-incrémenté)
   - `NomCours` (varchar de 100 caractères)
   - `Professeur` (varchar de 100 caractères)

3. Créez une table `Inscriptions` avec les colonnes suivantes :
   - `InscriptionID` (clé primaire, entier, auto-incrémenté)
   - `EtudiantID` (entier, clé étrangère référençant `EtudiantID` de la table `Etudiants`)
   - `CoursID` (entier, clé étrangère référençant `CoursID` de la table `Cours`)
   - `DateInscription` (date)

### Exercice 2: Insertion de Données

1. Insérez au moins 5 enregistrements dans la table `Etudiants`.
2. Insérez au moins 3 enregistrements dans la table `Cours`.
3. Insérez des données dans la table `Inscriptions` qui associent les étudiants aux cours.

### Exercice 3: Requêtes

1. Sélectionnez tous les étudiants nés après le 1er janvier 2000.
2. Sélectionnez tous les cours enseignés par le professeur "Dupont".
3. Sélectionnez tous les étudiants inscrits au cours "Informatique 101".
4. Comptez le nombre d'étudiants inscrits à chaque cours.
