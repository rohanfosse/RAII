# Introduction au langage C

## 1. Histoire et importance du C

Bien sûr, ajoutons deux paragraphes à la première section pour approfondir l'introduction.
Introduction au langage C
1. Histoire et importance du C

Le langage C a été créé dans les années 1970 par Dennis Ritchie chez Bell Labs. Il est à la base de nombreux systèmes d'exploitation, dont UNIX. Aujourd'hui, il est encore largement utilisé, notamment pour la programmation système.

Le C est connu pour sa simplicité et sa flexibilité, ce qui le rend particulièrement précieux pour la programmation système, les applications embarquées et les performances critiques. Bien que considéré comme un langage de niveau intermédiaire, le C offre un niveau d'accès direct à la mémoire à travers des pointeurs, ce qui permet une gestion fine des ressources.

Outre son rôle dans la programmation bas niveau, le C a influencé de nombreux autres langages de programmation tels que C++, C#, Java et même Python. Sa syntaxe et ses conventions sont devenues une base pour la conception de nombreux autres langages. Apprendre le C peut fournir une base solide pour comprendre comment les ordinateurs fonctionnent à un niveau plus profond.

---

## 2. Structure d'un programme C

Un programme C est composé de fonctions, de variables, et de directives pour le préprocesseur. La fonction `main()` est le point d'entrée d'un programme C, c'est-à-dire que l'exécution commence par cette fonction. Un programme C typique comprend également des en-têtes (ou "headers") qui sont inclus au début du code afin d'utiliser certaines fonctionnalités, comme les opérations d'entrée/sortie standard.

### Directives du préprocesseur

Les directives du préprocesseur commencent par le symbole # et ne sont pas des instructions C à proprement parler, mais des indications pour le préprocesseur. Elles sont traitées avant la compilation proprement dite. La directive la plus courante est #include, qui est utilisée pour inclure le contenu d'un autre fichier dans le programme.

### Exemple basique

```c
#include <stdio.h>  // Inclusion du header pour les fonctions d'entrée/sortie

int main() {
    // Déclaration de deux variables entières
    int a = 5;
    int b = 10;

    // Calcul et affichage de la somme
    int somme = a + b;
    printf("La somme de %d et %d est %d.\n", a, b, somme);

    return 0;  // Indique une fin d'exécution réussie
}
```

### Explication :
Dans l'exemple ci-dessus :
1. Nous avons inclus l'en-tête `stdio.h` qui contient des déclarations pour les fonctions d'entrée/sortie comme `printf`.
2. La fonction `main` est définie. C'est ici que notre programme commence son exécution.
3. À l'intérieur de `main`, nous déclarons et initialisons deux variables `a` et `b`.
4. Nous calculons ensuite leur somme et l'affichons à l'aide de la fonction `printf`.
5. Enfin, la fonction `main` retourne `0` pour indiquer que tout s'est bien passé.

---

## 3. Types de données en C

Dans le langage C, chaque variable est associée à un type de données. Ce type définit la nature des données que la variable peut contenir ainsi que les opérations qui peuvent être effectuées sur elle. Les types de données permettent au compilateur de comprendre comment allouer la mémoire et comment interpréter les données stockées. Il existe plusieurs types de données fondamentaux en C, chacun avec ses propres caractéristiques.

### Types entiers : 
Le type `int` est utilisé pour stocker des nombres entiers. Sa taille peut varier selon la machine et le compilateur, mais elle est généralement de 4 octets (32 bits) sur la plupart des architectures modernes.

```c
int age = 25;         // Un entier positif
int temperature = -5; // Un entier négatif
```

Il existe aussi des variantes du type `int` comme `short` et `long` qui peuvent stocker respectivement des entiers plus petits et plus grands.

### Types à virgule flottante :
Pour les nombres à virgule, on utilise les types `float` et `double`. `float` est généralement sur 4 octets tandis que `double` est sur 8 octets, offrant une plus grande précision.

```c
float pi = 3.14f;          // f indique que c'est un float
double e = 2.718281828459; 
```

### Types caractères :
Le type `char` est utilisé pour stocker un seul caractère. En interne, les caractères sont stockés sous forme de nombres entiers selon la table ASCII.

```c
char premiereLettre = 'A'; 
char signe = '#';
```

### Explication :
Dans cette section, nous avons exploré les types de données fondamentaux en C. Chaque type a une taille mémoire spécifique et est conçu pour une utilisation particulière. Il est essentiel de comprendre ces types pour écrire des programmes efficaces et éviter les erreurs courantes comme les débordements.

---

## 4. Opérateurs en C

En programmation, les opérateurs permettent d'effectuer des opérations sur des variables et des valeurs. Le langage C propose une gamme riche d'opérateurs qui peuvent être classés en différentes catégories en fonction de leur fonctionnalité.

### Opérateurs arithmétiques:
Ces opérateurs sont utilisés pour effectuer des opérations mathématiques de base.

```c
int a = 10, b = 20;

int somme = a + b;       // Addition
int difference = a - b; // Soustraction
int produit = a * b;    // Multiplication
int quotient = b / a;   // Division
int reste = b % a;      // Modulo (reste de la division)
```

### Opérateurs de comparaison:
Ils permettent de comparer deux valeurs. Le résultat de ces opérations est toujours un booléen : `1` (vrai) ou `0` (faux).

```c
int a = 5, b = 10;

int egal = (a == b);      // Vérifie si a est égal à b
int different = (a != b); // Vérifie si a est différent de b
int inferieur = (a < b);  // Vérifie si a est inférieur à b
```

### Opérateurs logiques:
Ces opérateurs sont utilisés pour effectuer des opérations booléennes sur des valeurs.

```c
int vrai = 1, faux = 0;

int et = vrai && faux;   // ET logique
int ou = vrai || faux;   // OU logique
int non = !vrai;         // NON logique
```

### Explication:
Les opérateurs jouent un rôle crucial en programmation, car ils déterminent la logique et les calculs réalisés dans le code. En comprenant bien comment chaque opérateur fonctionne, vous pouvez écrire des programmes plus efficaces et éviter des erreurs courantes. Par exemple, une confusion courante chez les débutants est de mélanger l'opérateur d'affectation `=` avec l'opérateur de comparaison `==`.

---

## 5. Contrôles de flux en C

Le contrôle de flux est un concept fondamental en programmation qui détermine comment les instructions sont exécutées de manière séquentielle ou conditionnelle. Le langage C offre plusieurs structures de contrôle de flux pour manipuler l'ordre d'exécution des instructions en fonction de conditions ou de boucles.

### Structures conditionnelles:

La structure `if` permet d'exécuter des blocs de code en fonction de la véracité d'une condition.

```c
int age = 22;

if (age >= 18) {
    printf("Vous êtes majeur.\n");
} else {
    printf("Vous êtes mineur.\n");
}
```

Si la condition nécessite plusieurs vérifications, `else if` peut être utilisé.

```c
int score = 85;

if (score >= 90) {
    printf("Excellent!\n");
} else if (score >= 70) {
    printf("Bien!\n");
} else {
    printf("Peut mieux faire.\n");
}
```

### Boucles:

Les boucles permettent d'exécuter un bloc de code plusieurs fois.

- Boucle `for` :

Elle est généralement utilisée lorsque le nombre d'itérations est connu.

```c
for (int i = 0; i < 5; i++) {
    printf("Répétition %d\n", i+1);
}
```

- Boucle `while` :

Cette boucle s'exécute tant qu'une condition est vraie.

```c
int i = 0;
while (i < 5) {
    printf("Répétition %d\n", i+1);
    i++;
}
```

- Boucle `do..while` :

Similaire à `while`, mais la condition est évaluée après l'exécution du bloc, garantissant au moins une exécution.

```c
int i = 0;
do {
    printf("Répétition %d\n", i+1);
    i++;
} while (i < 5);
```

### Explication:

Le contrôle de flux est essentiel pour donner de la logique et de la structure à un programme. Les conditions et les boucles permettent de créer des branches et des répétitions dans le code, rendant les programmes capables de prendre des décisions et d'effectuer des tâches répétitives de manière efficace.

---

## 6.Les pointeurs en C

### **Déclaration et initialisation**:

Un pointeur est déclaré comme une variable, mais il est précédé d'un astérisque `*`.

```c
int var = 10;
int *ptr_int;       // Déclaration d'un pointeur vers un int
```

Dans cet exemple, `ptr_int` est déclaré comme un pointeur sur un `int`. Il n'a pas encore de valeur d'adresse assignée.

```c
ptr_int = &var;     // ptr_int contient maintenant l'adresse de var
```

Ici, l'opérateur `&` obtient l'adresse mémoire de `var` et l'assigne à `ptr_int`. Donc, `ptr_int` pointe maintenant vers `var`.

### **Déréférencement de pointeur**:

Le déréférencement est l'action d'accéder à la valeur stockée à l'adresse qu'un pointeur pointe.

```c
int value = *ptr_int;  // value contiendra 10
```

Dans cet exemple, l'astérisque devant `ptr_int` déréférence le pointeur, ce qui signifie que nous accédons à la valeur stockée à l'adresse sur laquelle `ptr_int` pointe, qui est `var`. Donc, `value` obtiendra la valeur 10.

### **Pointeurs et tableaux**:

Un tableau est intrinsèquement lié aux pointeurs.

```c
int arr[3] = {10, 20, 30};
int *ptr_arr = arr;    // Pointe vers le premier élément du tableau
```

Ici, `ptr_arr` est initialisé avec l'adresse du premier élément du tableau. Donc, `*ptr_arr` serait 10.

```c
int second_element = *(ptr_arr + 1);  // Récupère 20
```

En ajoutant 1 à `ptr_arr`, nous déplaçons le pointeur vers le prochain élément du tableau. Donc, `*(ptr_arr + 1)` donne 20.

### **Pointeurs et chaînes de caractères**:

Les chaînes sont représentées comme des tableaux de caractères et peuvent donc être manipulées avec des pointeurs.

```c
char *str = "Hello";
printf("%c\n", *(str+1));  // Affiche "e"
```

`str` pointe vers le premier caractère, 'H'. En ajoutant 1 à `str` et en le déréférençant, on accède au deuxième caractère, 'e'.

### **Pointeurs vers des pointeurs**:

Les pointeurs peuvent aussi pointer vers d'autres pointeurs, ajoutant une autre couche d'indirection.

```c
int x = 5;
int *ptr1 = &x;
int **ptr2 = &ptr1;
```

Ici, `ptr1` pointe vers `x`, tandis que `ptr2` pointe vers le pointeur `ptr1` lui-même. Pour accéder à `x` via `ptr2`, on utilise `**ptr2`.

### **Pointeurs et fonctions**:

Les pointeurs permettent de passer des références de variables à des fonctions.

```c
void updateValue(int *p, int newVal) {
    *p = newVal;
}

int main() {
    int num = 10;
    updateValue(&num, 20);
    printf("%d\n", num);  // Affiche "20"
}
```

Dans cet exemple, au lieu de passer la valeur de `num` à `updateValue`, nous passons son adresse. La fonction `updateValue` utilise ensuite cette adresse pour modifier directement la valeur de `num` dans la fonction `main`.

---

## 7. Malloc et gestion de la mémoire en C

La mémoire dynamique est un aspect essentiel de la programmation en C. Elle permet d'allouer de la mémoire pendant l'exécution du programme, plutôt qu'à la compilation. La fonction `malloc` (memory allocation) est fréquemment utilisée pour cette allocation dynamique.

### **Utilisation de malloc**:

La fonction `malloc` alloue un bloc de mémoire de la taille spécifiée et retourne un pointeur vers le premier octet du bloc.

```c
int *ptr = (int*) malloc(sizeof(int));  
```

Ici, nous demandons à `malloc` d'allouer un espace mémoire suffisant pour stocker un `int`. La fonction `sizeof` retourne la taille en octets du type ou de l'objet fourni. `malloc` retourne un pointeur de type `void*`, donc nous effectuons un cast pour le convertir en `int*`.

### **Vérification de l'allocation**:

L'allocation dynamique peut échouer si la mémoire est insuffisante. Il est donc crucial de vérifier si `malloc` a réussi.

```c
if (ptr == NULL) {
    printf("Échec de l'allocation de mémoire.\n");
    exit(1);
}
```

Si `malloc` échoue, elle retourne `NULL`. Dans cet exemple, si `ptr` est `NULL`, le programme affiche un message d'erreur et se termine.

### **Libération de la mémoire**:

L'une des responsabilités du programmeur en C est de s'assurer que toute mémoire allouée dynamiquement est également libérée. Sinon, cela peut entraîner des fuites de mémoire.

```c
free(ptr);
```

Après avoir utilisé la mémoire allouée par `malloc`, vous devez utiliser `free` pour la libérer. Dans cet exemple, la mémoire pointée par `ptr` est libérée.

### **Utilisation avec des tableaux**:

`malloc` est souvent utilisé pour créer des tableaux de taille dynamique.

```c
int n = 5;
int *arr = (int*) malloc(n * sizeof(int));
```

Ici, un tableau d'entiers de taille `n` est créé. Chaque élément peut être accédé et modifié comme un tableau normal.

---

## Exercices

### Exercice 1: Inversion de chaîne de caractères

**Énoncé :**  
Écrivez une fonction `char* reverseString(char* str)` qui prend en entrée une chaîne de caractères et renvoie une nouvelle chaîne allouée dynamiquement qui est l'inversion de la chaîne d'origine. N'oubliez pas de libérer la mémoire lorsque vous avez fini.

**Note :**  
N'utilisez pas de fonctions standard pour inverser la chaîne. Utilisez des pointeurs pour parcourir et inverser la chaîne.

---

### Exercice 2: Recherche de tableau dynamique

**Énoncé :**  
Créez une fonction `int* createArray(int size)` qui prend en entrée une taille et retourne un tableau d'entiers alloué dynamiquement de cette taille, rempli de nombres entiers consécutifs à partir de 1. Écrivez ensuite une fonction `int findInArray(int* arr, int size, int value)` qui recherche une valeur dans le tableau et renvoie son indice si elle est trouvée, sinon `-1`.

---

### Exercice 3: Matrice dynamique

**Énoncé :**  
Écrivez une fonction `int** createMatrix(int rows, int cols)` qui crée une matrice (tableau 2D) de `rows` x `cols` allouée dynamiquement. Remplissez cette matrice avec des multiples consécutifs de 3, et renvoyez le pointeur vers cette matrice. Assurez-vous de libérer correctement toute la mémoire!

---

### Exercice 4: Pointeur de pointeur

**Énoncé :**  
Créez une fonction `void changeValues(int** ptr1, int** ptr2)` qui échange les valeurs pointées par `ptr1` et `ptr2`. Testez votre fonction avec deux variables de type `int` et deux pointeurs pointant respectivement vers ces variables.

---

### Exercice 5: Gestion de la mémoire

**Énoncé :**  
Imaginez que vous écrivez un logiciel pour un système avec des ressources limitées. Vous devez vous assurer que chaque octet de mémoire compte. Écrivez un programme qui simule l'allocation et la libération de la mémoire pour différentes tâches. Utilisez des pointeurs pour représenter les blocs de mémoire alloués, et assurez-vous de vérifier que l'allocation a réussi et de libérer la mémoire lorsque vous avez fini.

---


