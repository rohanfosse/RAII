# Introduction au C++

Bienvenue dans ce cours d'introduction au C++. Après avoir complété un projet en C et Arduino, vous avez déjà une bonne base pour comprendre les concepts fondamentaux de la programmation. Le C++ est une extension du C qui ajoute des fonctionnalités importantes, notamment la programmation orientée objet. Il est largement utilisé dans l'industrie et offre une performance comparable à celle du C tout en permettant une abstraction et une organisation du code plus avancées.

## Installation de l'Environnement de Développement

Avant de commencer, assurez-vous d'avoir un environnement de développement C++ installé sur votre machine. Vous pouvez utiliser des IDEs tels que Microsoft Visual Studio, CLion ou des compilateurs comme g++ sur Linux.

```bash
# Sur Ubuntu, installez le compilateur g++ avec la commande suivante :
sudo apt-get install g++
```

Sur Windows, l'IDE (Environnement de Développement Intégré) recommandé est Microsoft Visual Studio. Voici comment le configurer :

1. Téléchargez et installez [Microsoft Visual Studio](https://visualstudio.microsoft.com/) depuis le site officiel.
2. Pendant l'installation, sélectionnez le workload "Desktop development with C++" pour installer les outils nécessaires pour le développement en C++.

Si vous avez déjà installé Visual Studio, vous pouvez installer les extensions nécessaires dans le mene "Extension".

## Structure de base d'un programme C++

Le C++ conserve beaucoup de la syntaxe et de la sémantique du C, mais ajoute des fonctionnalités. Voici la structure de base d'un programme C++ :

```c++
#include <iostream>  // Inclut la bibliothèque iostream

int main() {  // Définit la fonction main qui est le point d'entrée du programme
    std::cout << "Bonjour le monde!" << std::endl;  // Affiche "Bonjour le monde!" sur la console
    return 0;  // Retourne 0 pour indiquer que le programme s'est terminé avec succès
}
```

## Variables

En C++, comme en C, les variables doivent être déclarées avec un type avant d'être utilisées. Voici les types de base en C++ :

| Type | Description |
| ---- | ----------- |
| `int` | Entier signé |
| `float` | Nombre à virgule flottante |
| `double` | Nombre à virgule flottante double précision |
| `char` | Caractère |
| `bool` | Booléen |

```c++
int maVariable = 42;  // Définit une variable de type int appelée maVariable avec la valeur 42
```


## Espaces de Noms

Les espaces de noms sont une fonctionnalité du C++ qui permet d'organiser le code en groupes logiques et d'éviter les conflits de noms.

```c++
namespace MonEspace {  // Définit un espace de noms appelé MonEspace
    int maVariable = 42;  // Définit une variable dans MonEspace
}

int main() {
    std::cout << MonEspace::maVariable << std::endl;  // Accède à maVariable dans MonEspace
    return 0;
}
```

Les espaces de noms peuvent être imbriqués :

```c++

namespace MonEspace {  // Définit un espace de noms appelé MonEspace
    namespace MonEspaceInterne {  // Définit un espace de noms appelé MonEspaceInterne
        int maVariable = 42;  // Définit une variable dans MonEspaceInterne
    }
}

int main() {
    std::cout << MonEspace::MonEspaceInterne::maVariable << std::endl;  // Accède à maVariable dans MonEspaceInterne
    return 0;
}
```

Les espaces de noms peuvent servir à organiser le code, mais aussi à éviter les conflits de noms. Par exemple, si deux bibliothèques définissent une fonction `maFonction`, il est possible de les distinguer en utilisant les espaces de noms :

```c++
namespace MaBibliotheque1 {
    void maFonction() {
        std::cout << "Bonjour de MaBibliotheque1!" << std::endl;
    }
}

namespace MaBibliotheque2 {
    void maFonction() {
        std::cout << "Bonjour de MaBibliotheque2!" << std::endl;
    }
}

int main() {
    MaBibliotheque1::maFonction();  // Appelle maFonction dans MaBibliotheque1
    MaBibliotheque2::maFonction();  // Appelle maFonction dans MaBibliotheque2
    return 0;
}
```

## Structures de Contrôle et Boucles

Ces structures sont les mêmes que celles en C. 

## Fonctions

Les fonctions sont définies de la même manière qu'en C, mais peuvent être surchargées. Cela signifie qu'il est possible de définir plusieurs fonctions avec le même nom mais des paramètres différents.

```c++
void maFonction() {  // Définit une fonction appelée maFonction qui ne prend pas de paramètres
    std::cout << "Bonjour de maFonction!" << std::endl;
}

void maFonction(int parametre) {  // Définit une fonction appelée maFonction qui prend un paramètre de type int
    std::cout << "Bonjour de maFonction avec parametre " << parametre << "!" << std::endl;
}

int main() {
    maFonction();  // Appelle maFonction sans paramètre
    maFonction(42);  // Appelle maFonction avec le paramètre 42
    return 0;
}
```

## Tableaux

Les tableaux sont définis de la même manière qu'en C.

```c++
int monTableau[5];  // Définit un tableau de 5 entiers

int main() {
    monTableau[0] = 42;  // Affecte la valeur 42 à la première case du tableau
    std::cout << monTableau[0] << std::endl;  // Affiche la valeur de la première case du tableau
    return 0;
}
```

## Pointeurs

Les pointeurs sont définis de la même manière qu'en C.

```c++
int maVariable = 42;  // Définit une variable de type int appelée maVariable avec la valeur 42
int* monPointeur = &maVariable;  // Définit un pointeur sur maVariable

int main() {
    std::cout << *monPointeur << std::endl;  // Affiche la valeur pointée par monPointeur
    return 0;
}
```



## Classe

Une classe est une structure de données qui contient des variables et des fonctions. Les variables et fonctions d'une classe sont appelées membres de la classe. Les variables membres sont des variables qui appartiennent à une classe et les fonctions membres sont des fonctions qui appartiennent à une classe. Les classes sont la base de la programmation orientée objet (POO).

```c++
class MaClasse {  // Définit une classe appelée MaClasse
public:  // Début de la section publique
    int maVariable;  // Définit une variable membre

    void maMethode() {  // Définit une méthode membre
        std::cout << "Bonjour de MaClasse!" << std::endl;
    }
};

int main() {
    MaClasse obj;  // Crée un objet de type MaClasse
    obj.maMethode();  // Appelle la méthode maMethode sur obj
    return 0;
}
```

## L'héritage

L'héritage est une fonctionnalité de la POO qui permet de créer des classes dérivées d'une classe de base. Les classes dérivées héritent des membres de la classe de base et peuvent les modifier ou ajouter de nouveaux membres.

```c++
class MaClasseDeBase {  // Définit une classe de base appelée MaClasseDeBase

public:
    int maVariable;  // Définit une variable membre

    void maMethode() {  // Définit une méthode membre
        std::cout << "Bonjour de MaClasseDeBase!" << std::endl;
    }
};

class MaClasseDerivee : public MaClasseDeBase {  // Définit une classe dérivée de MaClasseDeBase appelée MaClasseDerivee

public:
    void maMethode() {  // Redéfinit la méthode maMethode
        std::cout << "Bonjour de MaClasseDerivee!" << std::endl;
    }
};

int main() {
    MaClasseDerivee obj;  // Crée un objet de type MaClasseDerivee
    obj.maMethode();  // Appelle la méthode maMethode sur obj
    return 0;
}
```

### Exercices

1. Créez une classe `Personne` avec les attributs `nom`, `prenom` et `age`. Ajoutez une méthode `afficher` qui affiche les informations de la personne.

2. Créez une classe `Etudiant` qui hérite de `Personne` et ajoutez un attribut `numeroEtudiant`. Redéfinissez la méthode `afficher` pour afficher les informations de l'étudiant.

3. Créez une classe `Enseignant` qui hérite de `Personne` et ajoutez un attribut `salaire`. Redéfinissez la méthode `afficher` pour afficher les informations de l'enseignant.

## Encapsulation

L'encapsulation est une fonctionnalité de la POO qui permet de cacher les détails d'implémentation d'une classe. Les membres privés d'une classe ne peuvent être accédés que par les méthodes de la classe.

```c++
class MaClasse {  // Définit une classe appelée MaClasse
private:  // Début de la section privée
    int maVariable;  // Définit une variable membre

public:  // Début de la section publique
    void setMaVariable(int valeur) {  // Définit une méthode membre publique
        maVariable = valeur;
    }

    int getMaVariable() {  // Définit une méthode membre publique
        return maVariable;
    }
};

int main() {
    MaClasse obj;  // Crée un objet de type MaClasse
    obj.setMaVariable(42);  // Appelle la méthode setMaVariable sur obj
    std::cout << obj.getMaVariable() << std::endl;  // Appelle la méthode getMaVariable sur obj
    return 0;
}
```

L'encapuslation est utile lorsque l'on veut s'assurer que les membres d'une classe ne sont pas modifiés de manière inattendue. Par exemple, si on veut s'assurer que la valeur d'une variable est toujours positive, on peut utiliser l'encapsulation pour s'assurer que la variable ne peut être modifiée que par une méthode qui vérifie que la valeur est positive.

### Exercice

1. Modifiez la classe `Personne` pour que les attributs soient privés et ajoutez des méthodes `set` et `get` pour accéder aux attributs.

2. Modifiez la classe `Etudiant` pour que les attributs soient privés et ajoutez des méthodes `set` et `get` pour accéder aux attributs.


## Polymorphisme

Le polymorphisme est un concept clé de la programmation orientée objet (POO) qui permet aux objets d'être traités comme des instances d'une classe parente, ce qui conduit à une manière simplifiée de manipuler des objets de classes différentes d'une manière uniforme. En C++, le polymorphisme peut être mis en œuvre de plusieurs manières, notamment par l'héritage et l'overloading (la surcharge de fonctions et d'opérateurs). Voici un aperçu des différentes formes de polymorphisme en C++ :

### 1. Polymorphisme par la Surcharge (Overloading) :

#### a. Surcharge de Fonctions :
La surcharge de fonctions permet à plusieurs fonctions de partager le même nom mais d'avoir des listes de paramètres différentes, soit en nombre soit en type de paramètres.

```c++
class Math {
public:
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
};

int main() {
    Math math;
    std::cout << math.add(10, 20) << std::endl;  // Affiche 30
    std::cout << math.add(10.5, 20.5) << std::endl;  // Affiche 31
    return 0;
}
```

#### b. Surcharge d'Opérateurs :
La surcharge d'opérateurs permet de définir de nouvelles opérations pour les opérateurs en C++.

```c++
class Complex {
public:
    double real, imag;
    Complex(double r, double i) : real(r), imag(i) {}

    Complex operator + (const Complex& other) {
        return Complex(this->real + other.real, this->imag + other.imag);
    }
};

int main() {
    Complex num1(1.0, 2.0), num2(3.0, 4.0);
    Complex sum = num1 + num2;
    std::cout << sum.real << " + " << sum.imag << "i" << std::endl;  // Affiche 4 + 6i
    return 0;
}
```

### 2. Polymorphisme par l'Héritage :

Le polymorphisme peut également être réalisé en C++ à l'aide de l'héritage et des pointeurs de classe de base.

```c++
class Animal {
public:
    virtual void makeSound() {
        std::cout << "Un son générique d'animal" << std::endl;
    }
};

class Dog : public Animal {
public:
    void makeSound() override {
        std::cout << "Woof" << std::endl;
    }
};

class Cat : public Animal {
public:
    void makeSound() override {
        std::cout << "Meow" << std::endl;
    }
};

int main() {
    Animal* animals[2];
    animals[0] = new Dog();
    animals[1] = new Cat();
    
    for(int i = 0; i < 2; ++i) {
        animals[i]->makeSound();
    }

    delete animals[0];
    delete animals[1];
    
    return 0;
}
```

Dans cet exemple, la classe `Animal` a une méthode virtuelle `makeSound`. Les classes `Dog` et `Cat` héritent de la classe `Animal` et surchargent la méthode `makeSound`. Dans la fonction `main`, un tableau de pointeurs `Animal` est créé et utilisé pour appeler la méthode `makeSound` sur des objets `Dog` et `Cat`. Cela permet d'obtenir un comportement polymorphique, où la version appropriée de `makeSound` est appelée en fonction du type d'objet réel pointé par le pointeur `Animal`.

#### Exercices

1. Créez une classe `Forme` avec une méthode `aire` et une méthode `perimetre`. Créez des classes `Rectangle` et `Cercle` qui héritent de `Forme` et redéfinissez les méthodes `aire` et `perimetre` pour calculer l'aire et le périmètre d'un rectangle et d'un cercle.

2. Créez une classe `Vehicule` avec une méthode `avancer`. Créez des classes `Voiture` et `Avion` qui héritent de `Vehicule` et redéfinissez la méthode `avancer` pour afficher "La voiture avance" et "L'avion avance".
