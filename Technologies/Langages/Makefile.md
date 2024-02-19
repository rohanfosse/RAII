# Compilation avec Make #
## Introduction
Un **Makefile** est un fichier, utilisé par le programme **make**, regroupant une série de commandes permettant d’exécuter un ensemble d’actions, typiquement la compilation d’un
projet.

Il est constitué d’une ou de plusieurs règles de la
forme :

```bash
cible: dépendances
	commandes
```

Lors du parcours du fichier, le programme make évalue d’abord la première règle ren-
contrée, ou celle dont le nom est spécifié en argument. L’évaluation d’une règle se fait
récursivement :

1. les dépendances sont analysées : si une dépendance est la cible d’une autre règle, cette règle est à son tour évaluée ;
2. lorsque l’ensemble des dépendances a été analysé, et si la cible est plus ancienne que les dépendances, les commandes correspondant à la règle sont exécutées.

## Exemple
Ce qui suit présente la création d’un Makefile pour un exemple de projet simple. Tout d'abord, considérons le dossier *hello* contenant les fichiers hello.h, hello.c et main.c.

### Makefile de base
Un fichier Makefile de base de ce projet pourrait s’écrire :

```bash
hello: hello.o main.o
	gcc -o mon_executable hello.o main.o
	
hello.o: hello.c
	gcc -o hello.o -c hello.c -Wall -O
	
main.o: main.c hello.h
	gcc -o main.o -c main.c -Wall -O
```
En effet pour créer l’exécutable *hello* , nous avons besoin des fichiers objets
*hello.o* et *main.o*.

**make** va d’abord rencontrer *hello.o*, et va donc évaluer la règle dont ce fichier est la cible.

La seule dépendance de cette règle étant hello.c, qui n’est pas cible d’une autre règle, **make** va exécuter la commande :
```bash
gcc -o main.o -c main.c -Wall -O
```

De la même façon, **make** va ensuite analyser la règle dont main.o est la cible et exécuter
la commande :
```bash
gcc -o main.o -c main.c -Wall -O
```

Finalement, toutes les dépendances de la règle initiale ayant été analysées, make va exécuter la commande :
```bash
gcc -o hello hello.o main.o
```

### Quelques cibles standards

Pour améliorer ce Makefile, on peut rajouter quelques cibles standards :

- **all** : à placer généralement au début du fichier ; les dépendances associées correspondent à l’ensemble des exécutables à produire ;
- **clean** : normalement pas de dépendance ; la commande associée supprime tous les fichiers intermédiaires (notamment les fichiers objets) ;
- **mrproper** : la commande correspondante supprime tout ce qui peut être regénéré, ce qui permet une reconstruction complète du projet lors de l’appel suivant à make.

Notre Makefile devient donc ici :

```bash
all: hello

hello: hello.o main.o
	gcc -o mon_executable hello.o main.o
	
hello.o: hello.c
	gcc -o hello.o -c hello.c -Wall -O
	
main.o: main.c hello.h
	gcc -o main.o -c main.c -Wall -O
	
clean:
	rm -f *.o
	
mrproper: clean
	rm -f hello
```

### Introduction de variables

Il est possible de définir des variables dans un Makefile. Elles se déclarent sous la forme
`NOM = valeur` et sont appelées sous la forme `$(NOM)`, à peu près comme dans un shellscript.

Parmi quelques variables standards pour un Makefile de projet C ou C++, on trouve :

- **CC** qui désigne le compilateur utilisé ;
- **CFLAGS** qui regroupe les options de compilation ;
- **LDFLAGS** qui regroupe les options d’édition de liens ;
- **EXEC** ou **TARGET** qui regroupe les exécutables.

Pour notre projet exemple, cela nous donnerait :

```bash
CC=gcc
CFLAGS=-Wall -O
LDFLAGS=
EXEC=hello

all: $(EXEC)

$(EXEC): hello.o main.o
	$(CC) -o $(EXEC) hello.o main.o
	
hello.o: hello.c
	$(CC) -o hello.o -c hello.c $(CFLAGS)
	
main.o: main.c hello.h
	$(CC) -o main.o -c main.c $(CFLAGS)
	
clean:
	rm -f *.o
	
mrproper: clean
	rm -f hello
```

### Les variables internes

Il existe aussi, et c’est encore plus intéressant car très puissant, des variables internes au Makefile, utilisables dans les commandes, avec notamment :

- **$@** : nom de la cible ;
- **$<** : nom de la première dépendance ;
- **$ˆ** : liste des dépendances ;
- **$?** : liste des dépendances plus récentes que la cible ;
- **$** : nom d’un fichier sans son suffixe.

On peut donc encore compacter notre Makefile

```bash
CC=gcc
CFLAGS=-Wall -O
LDFLAGS=
EXEC=hello

$(EXEC): hello.o main.o
	$(CC) -o $@ $^ 
	
hello.o: hello.c
	$(CC) -o $@ -c $< $(CFLAGS)
	
main.o: main.c hello.h
	$(CC) -o $@ -c $< $(CFLAGS)

clean:
	rm -f *.o
	
mrproper: clean
	rm -f hello
```

### Règles d’inférences

On voit néanmoins qu’il y a encore moyen d’améliorer ce Makefile. En effet les règles dont les deux fichiers objets sont les cibles se ressemblent fortement.
Et justement, on peut créer des règles génériques dans un Makefile : il suffit d’utiliser le symbole `%` à la fois pour la cible et pour la dépendance.
Il est également possible de préciser séparement d’autres dépendances pour les cas particuliers, par exemple pour ne pas oublier la dépendance au fichier `exemple.h` pour la règle dont `main.o` est la cible. 

Dans notre exemple, cela nous donnerait :

```bash
CC=gcc
CFLAGS=-Wall -O
LDFLAGS=
EXEC=hello

$(EXEC): hello.o main.o
	$(CC) -o $@ $^ 
	
main.o: exemple.h

%.o: %.c
	$(CC) -o $@ -c $< $(CFLAGS)

clean:
	rm -f *.o
	
mrproper: clean
	rm -f hello
```

## Les conditions

Les directives conditionnelles sont:

- La condition **ifeq** commence la condition, et spécifie la condition. Elle contient deux arguments, séparés par une virgule et entourés de parenthèses.
	Les deux éléments sont comparés. Les lignes du makefile qui suivent ifeq sont respectées si les deux arguments correspondent, sinon elles sont ignorées.

- La condition **ifneq** commence la conditionnelle, et spécifie la condition. Elle contient deux arguments, séparés par une virgule et entourés de parenthèses. Les deux arguments sont comparés. Les lignes du makefile qui suivent la ifneq sont respectées si les deux arguments ne correspondent pas ; sinon elles sont ignorées.

- La condition **ifdef** commence la conditionnelle, et spécifie la condition. Elle contient un seul argument. Si l'argument donné est vrai, alors la condition devient vraie.

- La condition **ifndef** commence la condition et spécifie la condition. Elle contient un seul argument. Si l'argument donné est faux, la condition devient vraie.

- La condition **else** fait en sorte que les lignes suivantes soient respectées si la condition précédente échoue. Dans l'exemple ci-dessus, cela signifie que la deuxième commande de liaison alternative est utilisée lorsque la première alternative n'est pas utilisée. Il est facultatif d'avoir un else dans une conditionnelle.

- La condition **endif** termine la conditionnelle. Chaque conditionnel doit se terminer par un endif.

### Syntaxe des conditions

La syntaxe d'une conditionnelle simple est la suivante :

```bash
instruction conditionnelle
   texte-si-vrai
endif
```

Le `texte-si-vrai` peut être une ligne de texte quelconque, à considérer comme faisant partie du makefile si la condition est vraie. Si la condition est fausse, aucun texte n'est utilisé à la place.

La syntaxe d'une condition complexe se présente comme suit:

```bash
instruction conditionnelle
   text-if-true
else
   text-if-false
endif
```

Dans notre exemple, cela pourrait se présenter comme ceci:

```bash
CC=gcc
CFLAGS=-Wall -O
FLAGS=
LDFLAGS=
EXEC=hello

$(EXEC): hello.o main.o
	$(CC) -o $@ $^ 
	
main.o: exemple.h

%.o: %.c
ifeq ($(CC),gcc)
   $(CC) -o $@ -c $< $(CFLAGS)
else
   $(CC) -o $@ -c $< $(FLAGS)
endif
	

clean:
	rm -f *.o
	
mrproper: clean
	rm -f hello
```


Il existe encore bien d’autres possibilités pour simplifier un **Makefile**. Il est notamment possible de créer des Makefile pour des sous-répertoires correspondant à des sous-parties du projet, et d’avoir un Makefile “**maître**” très simple qui appelle ces “**sous-Makefile**”, avec la variable **MAKE**.

Il existe également des outils de **génération automatique**.


------------
