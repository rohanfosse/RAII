# Introduction aux Commandes Assembleur

L'assembleur est un langage de programmation de bas niveau qui permet aux programmeurs de communiquer directement avec le matériel d'un ordinateur. Chaque instruction assembleur est traduite en une instruction machine spécifique à une architecture donnée. Dans cette section, nous allons passer en revue certaines des commandes assembleur les plus courantes.

## Bases de l'Assembleur
### Registres

Un registre est une petite unité de stockage de données disponible dans le processeur. Les instructions assembleur peuvent utiliser ces registres pour stocker des données, effectuer des opérations arithmétiques et logiques, et contrôler le flux d'exécution.

### Instructions

Les instructions en assembleur sont des commandes qui indiquent au processeur quoi faire.

### 1. LDI (Load Immediate)

**Explication** : Charge une valeur immédiate (c'est-à-dire une valeur spécifiée directement dans l'instruction) dans un registre.

**Exemple** :
```assembly
LDI R16, 5  ; Charge la valeur 5 dans le registre R16
```

### 2. MOV (Move)

**Explication** : Copie la valeur d'un registre dans un autre registre.

**Exemple** :
```assembly
MOV R17, R16  ; Copie la valeur du registre R16 dans le registre R17
```

### 3. ADD (Addition)

**Explication** : Ajoute la valeur de deux registres et stocke le résultat dans un registre spécifié.

**Exemple** :
```assembly
ADD R18, R16, R17  ; Ajoute les valeurs des registres R16 et R17, puis stocke le résultat dans R18
```

### 4. SUB (Subtraction)

**Explication** : Soustrait la valeur d'un registre de celle d'un autre registre et stocke le résultat.

**Exemple** :
```assembly
SUB R18, R16, R17  ; Soustrait la valeur de R17 de R16 et stocke le résultat dans R18
```

### 5. JMP (Jump)

**Explication** : Saute à une adresse ou une étiquette spécifiée, permettant de contrôler le flux d'exécution du programme.

**Exemple** :
```assembly
JMP loopStart  ; Saute à l'étiquette "loopStart"
```

### 6. CMP (Compare)

**Explication** : Compare les valeurs de deux registres.

**Exemple** :
```assembly
CMP R16, R17  ; Compare les valeurs des registres R16 et R17
```

### 7. BRNE (Branch if Not Equal)

**Explication** : Saute à une adresse ou une étiquette si la dernière comparaison (via CMP) a déterminé que les valeurs n'étaient pas égales.

**Exemple** :
```assembly
BRNE notEqualLabel  ; Saute à l'étiquette "notEqualLabel" si R16 et R17 ne sont pas égaux
```

---

Avec ces commandes de base, un programmeur peut réaliser une variété d'opérations, allant de simples calculs arithmétiques à des contrôles de flux complexes. Dans la section suivante, nous explorerons comment utiliser ces commandes pour implémenter la séquence de Fibonacci en assembleur.

---

# Implémentation de la Séquence de Fibonacci en Assembleur

La séquence de Fibonacci est une série de nombres où chaque nombre est la somme des deux précédents. Elle commence généralement par 0 et 1. Les premiers nombres de la séquence sont : 0, 1, 1, 2, 3, 5, 8, ...

## Programme fourni

```assembly
LDI R16, 1      ; copie 0000 0001 dans R16
LDI R17, 2      ; copie 0000 0010 dans R17
MOV R20,%0      ; prend rASM comme argument dans le registre20
ADD R20, R16    ; additionne le R16 dans le R20
ADD R20, R17    ; additionne le R17 dans le R20
MOV R16, R17    ; charge R17 dans R16
MOV R17, R20    ; charge R20 dans R17
MOV%o, R20 : ‘r+' (rASM) ; copie la valeur dans la variable rASM
```

## Explication

1. Les deux premiers nombres de la séquence de Fibonacci (1 et 2) sont chargés dans les registres R16 et R17.
2. La valeur externe `rASM` est chargée dans le registre R20. Cette valeur pourrait représenter l'itération ou l'index de la séquence de Fibonacci que nous souhaitons calculer.
3. Les valeurs dans les registres R16 et R17 sont additionnées et le résultat est stocké dans R20.
4. Les valeurs sont ensuite déplacées entre les registres pour préparer la prochaine itération.
5. La valeur finale dans R20 est copiée dans la variable externe `rASM`.

## Note

Il est important de noter que ce programme utilise des registres de 8 bits. Cela signifie que chaque registre ne peut contenir qu'une valeur binaire de 8 chiffres. Si le résultat d'une addition dépasse cette capacité, il sera tronqué.

---
