# Introduction aux Commandes Assembleur

L’assembleur est un langage de bas niveau qui permet de piloter directement le processeur. Chaque instruction correspond à une opération machine précise et dépend de l’architecture (AVR, ARM, x86…). Comprendre les **registres**, les **flags** et le **flux de contrôle** est essentiel pour raisonner correctement sur un programme.

---

## Bases de l’Assembleur

### Registres

Un registre est une petite zone mémoire ultra-rapide à l’intérieur du processeur.
**Sur AVR 8 bits** :

- Il existe **32 registres** nommés **R0 à R31** (8 bits chacun).
- Certaines instructions (comme `LDI`) ne s’appliquent qu’aux registres **R16–R31**.
- Les valeurs **16 bits** sont manipulées en **paires** de registres : _octet bas_ et _octet haut_ (par ex. “bas” dans R24, “haut” dans R25).

### Registre d’état (SREG) et flags

Beaucoup d’instructions mettent à jour des **indicateurs** (flags) dans le **SREG** :

- **Z** (Zero) : résultat nul,
- **C** (Carry) : retenue/“emprunt” sur addition/soustraction (utile pour l’**arithmétique multi-octets**),
- **N** (Negative) : bit de signe,
- **V** (Overflow) : dépassement signé,
- **S** (Sign) : combinaison N⊕V,
- **H** (Half-carry) : retenue entre bits 3→4 (utile en BCD).

Les **branches conditionnelles** testent ces flags.

### Syntaxe : 1, 2 ou 3 opérandes

Selon l’architecture, une instruction peut avoir **2 opérandes** (AVR : `ADD Rd, Rr` ⇒ `Rd ← Rd + Rr`) ou **3 opérandes** (certains assembleurs RISC/Von Neumann).

> **Attention** : la **syntaxe varie**. Sur AVR, `ADD` a **2 opérandes**.

---

## Instructions fréquentes (vision AVR)

### 1. LDI (Load Immediate)

**But** : charger une **constante** dans un registre (R16–R31).

```asm
LDI R16, 5    ; R16 ← 5
```

### 2. MOV (Move)

**But** : copier la valeur d’un registre vers un autre.

```asm
MOV R17, R16  ; R17 ← R16
```

### 3. ADD et ADC (Addition)

**ADD** additionne 8 bits, **ADC** additionne **avec retenue C** (pour la partie “haut” d’un mot 16 bits).

```asm
; 16 bits (bas dans R18/R20, haut dans R19/R21)
MOV  R20, R18        ; c.low  ← a.low
MOV  R21, R19        ; c.high ← a.high
ADD  R20, R16        ; c.low  += b.low        (met C si dépassement)
ADC  R21, R17        ; c.high += b.high + C   (addition complète 16 bits)
```

### 4. SUB/SBC (Soustraction)

`SUB` 8 bits, `SBC` 8 bits avec retenue (multi-octets).

### 5. CP (Compare) et CPC (Compare with Carry)

**But** : comparer deux registres (met à jour les flags sans stocker le résultat).
`CP` compare 8 bits, `CPC` compare avec retenue pour les mots > 8 bits.

### 6. Branches conditionnelles (exemples)

- **BRNE** : _Branch if Not Equal_ → saute si **Z=0** (résultat non nul).
- **BREQ** : saute si **Z=1**.
- **BRGE** : _Branch if Greater or Equal (signé)_ → saute si **S=0** après `CP` (comparaison signée).
- **BRSH/BRLO** : comparaison **non signée** (utilisent **C**).

  - **BRSH** (_Branch if Same or Higher_) ≈ **≥** non signé (C=0).
  - **BRLO** (_Branch if Lower_) ≈ **<** non signé (C=1).

> **Bon réflexe** : choisir la branche adaptée **signée vs non signée** selon la nature des données (compteurs 0..255 ⇒ non signées).

### 7. JMP / RJMP & labels

- **RJMP** : saut relatif (proche), **JMP** : saut absolu.
- **Labels numérotés** et suffixes **`b/f`** :

  - `1:` définit un label.
  - `1b` = “label **1** vers l’**arrière**”, `2f` = “label **2** vers l’**avant**”.
    Pratique pour de petites boucles/petits blocs.

### 8. INC/DEC

**INC** incrémente, **DEC** décrémente un registre (mettent à jour les flags).

---

## Opérations multi-octets (ex. 16 bits)

Comme les registres AVR sont **8 bits**, les nombres plus grands se stockent sur plusieurs registres. Pour **additionner 16 bits** :

1. Additionner les **octets bas** avec `ADD` (met à jour **C**),
2. Additionner les **octets hauts** avec `ADC` (réutilise la **retenue C**).

Ce principe s’étend au 24/32 bits (enchaîner `ADD` puis deux/trois `ADC`).

---

## Flux de contrôle typique d’un calcul itératif

Beaucoup d’algorithmes (par ex. suites récurrentes) suivent ce **patron** :

1. **Initialiser** des registres (valeurs de départ et compteur).
2. **Comparer** compteur vs. limite (`CP`), puis **brancher** selon le flag (`BR…`).
3. **Calculer** l’itération (souvent : somme multi-octets via `ADD/ADC`).
4. **Mettre à jour** les registres (décalage des valeurs “ancien → nouveau”).
5. **Incrémenter** le compteur (`INC`), **boucler** (`RJMP` vers le label du début).
6. **Sortir** quand la condition est atteinte et **utiliser** la valeur finale.

## Inline assembleur (GCC) : lier variables et registres

Quand on insère de l’assembleur dans du C/C++ (syntaxe **GCC “extended asm”**), on **relie** des variables à des **opérandes** :

- **Placeholders** : `%0`, `%1`, … désignent les opérandes dans le bloc asm.
- **Contraintes** :

  - `"r"` : placer l’opérande dans un **registre**.
  - `"+r"` : **lecture/écriture** (la variable est aussi une **sortie**).
  - `"=&r"` : **early clobber** (le registre ne peut pas être partagé avec une autre entrée au même moment).

- **Paires bas/haut** (16 bits) : on peut nommer **l’octet bas/haut** d’un opérande 16 bits avec **`%A0`** (low) et **`%B0`** (high), pratique pour `ADD/ADC`.
- **Clobbers** : annoncer ce que l’asm modifie hors opérandes (ex. `"cc"` pour les **flags SREG**, et registres nommés si on les force).
- **`volatile`** : empêcher le compilateur de réordonner/supprimer le bloc asm.

> Idée clé : on décrit précisément **qui entre**, **qui sort** et **ce qui est abîmé**, afin que le compilateur aligne son allocation de registres avec le code assembleur.

---

## Implémentation de la Séquence de Fibonacci en Assembleur

La séquence de Fibonacci est une série de nombres où chaque terme est obtenu en additionnant les deux précédents. Elle commence généralement par :

```assembly
F(0) = 0
F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8 …
```

C’est une suite très utilisée pour illustrer les algorithmes, car elle est simple mais met en jeu des notions de **boucle**, de **décalage de valeurs** et d’**arithmétique multi-registres**.

---

### Programme fourni (extrait simplifié)

```assembly
LDI R16, 1       ; copie 0000 0001 (valeur décimale 1) dans R16
LDI R17, 2       ; copie 0000 0010 (valeur décimale 2) dans R17
MOV R20, %0      ; charge la valeur de la variable rASM dans le registre R20
ADD R20, R16     ; R20 ← R20 + R16
ADD R20, R17     ; R20 ← R20 + R17
MOV R16, R17     ; R16 ← R17 (on "décale" les valeurs)
MOV R17, R20     ; R17 ← R20 (prépare la prochaine valeur de la suite)
MOV %0, R20      ; recopie le contenu final de R20 dans la variable rASM
```

---

### Explication détaillée

#### 1. Initialisation des premiers termes

```assembly
LDI R16, 1
LDI R17, 2
```

- `LDI` signifie **Load Immediate** → on place directement une valeur **immédiate** (codée dans l’instruction) dans un registre.
- Ici, on charge les **deux premières valeurs de travail** de la suite :

  - `R16 = 1`
  - `R17 = 2`

**Remarque** : normalement, la suite commence par `0, 1`, mais ici l’exemple démarre à `1, 2` pour simplifier. Cela dépend du point de départ choisi.

---

#### 2. Préparation d’un registre de calcul

```assembly
MOV R20, %0
```

- `MOV` signifie **Move** : on copie la valeur d’une variable externe (`rASM`) dans un registre.
- Ici, `%0` est un **opérande symbolique** utilisé dans l’assembleur inline GCC : il correspond à la variable passée en argument côté C.
- Cette instruction place donc la valeur courante de `rASM` dans le registre `R20`.

`R20` servira de **registre accumulateur** pour stocker les résultats intermédiaires.

---

#### 3. Addition des termes

```assembly
ADD R20, R16
ADD R20, R17
```

- `ADD Rd, Rr` réalise une addition : **Rd ← Rd + Rr**.
- Première instruction : `R20 ← R20 + R16`
- Deuxième instruction : `R20 ← R20 + R17`

À ce stade, `R20` contient donc :

```
rASM + R16 + R17
```

Autrement dit, le nouveau terme est obtenu en ajoutant les deux registres précédents (`R16` et `R17`) au contenu de `R20`.

---

#### 4. Décalage des valeurs

```assembly
MOV R16, R17
MOV R17, R20
```

- `MOV R16, R17` : on met dans `R16` l’ancienne valeur de `R17`. Cela revient à faire **a ← b** (dans la logique de Fibonacci).
- `MOV R17, R20` : on met dans `R17` le nouveau résultat calculé. Cela revient à faire **b ← c**.

Ce mécanisme permet d’avancer d’une étape dans la suite de Fibonacci :

- le “premier terme” prend la valeur du second,
- le “second terme” prend la nouvelle valeur calculée.

Ainsi, à la prochaine itération, on pourra recommencer le calcul.

---

#### 5. Sauvegarde du résultat

```assembly
MOV %0, R20
```

- Enfin, on copie la valeur finale contenue dans `R20` dans la variable externe `rASM`.
- L’opérande `‘r+’ (rASM)` utilisé dans l’inline asm indique que `rASM` est **à la fois lu et modifié**.

Le programme en C qui appelle cet assembleur pourra donc récupérer directement le résultat mis à jour dans `rASM`.

---

### Résumé du fonctionnement

1. On charge deux registres avec les valeurs de départ.
2. On utilise un registre supplémentaire (`R20`) comme **accumulateur**.
3. On additionne les valeurs pour calculer le nouveau terme de la suite.
4. On décale les registres pour préparer l’itération suivante.
5. On sauvegarde le résultat dans une variable externe pour le reste du programme.
