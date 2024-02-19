# TCP ( Transmission Control Protocol )

## Introduction

Le protocole TCP (Transmission Control Protocol) est un protocole de transport de la couche 4 du modèle OSI. Il est utilisé pour le transport de données sur un réseau IP. Il est similaire au protocole UDP (User Datagram Protocol) mais il est plus fiable. Il est utilisé pour les applications qui nécessitent une livraison fiable des données.

## Objectifs d'apprentissage

À la fin de cette lecture, vous serez en mesure de :

- Décrire les caractéristiques du protocole TCP.
- Expliquer le fonctionnement du protocole TCP.
- Identifier les applications qui utilisent le protocole TCP.

## Caractéristiques du protocole TCP

Le protocole TCP est un protocole de transport fiable. Il fournit des mécanismes de contrôle de flux et de contrôle de congestion. Il fournit également des mécanismes de reprise après une panne.

Le protocole TCP est un protocole de transport orienté connexion. Il nécessite un établissement de connexion avant le transfert des données. Il nécessite également une libération de connexion après le transfert des données. Il est donc plus lent que le protocole UDP. Il est utilisé pour les applications qui nécessitent une livraison fiable des données.

## Fonctionnement du protocole TCP

Le protocole TCP est utilisé pour le transport de données sur un réseau IP. Il encapsule les données dans des segments TCP. Il ajoute un en-tête TCP à chaque segment TCP. L'en-tête TCP contient les informations suivantes :

- Le numéro de port source.
- Le numéro de port de destination.
- Le numéro de séquence.
- Le numéro d'acquittement.
- La longueur du segment TCP.
- Le flag TCP.
- La taille de la fenêtre.
- Le checksum TCP.

L'en-tête TCP est ajouté à chaque segment TCP. Le segment TCP est encapsulé dans un paquet IP. Le paquet IP est encapsulé dans une trame Ethernet. La trame Ethernet est transmise sur le réseau.

Le numéro de séquence est utilisé pour numéroter les octets de données. Le numéro d'acquittement est utilisé pour confirmer la réception des octets de données. Le flag TCP est utilisé pour indiquer le type de segment TCP. La taille de la fenêtre est utilisée pour contrôler le flux de données. Le checksum TCP est utilisé pour vérifier l'intégrité des données.

Signification des champs :

- Port source : numéro du port source
- Port destination : numéro du port destination
- Numéro de séquence : numéro de séquence du premier octet de ce segment
- Numéro d'acquittement : numéro de séquence du prochain octet attendu
- Taille de l'en-tête : longueur de l'en-tête en mots de 32 bits (les options font partie de l'en-tête)
- Indicateurs ou Flags :
  - Réservé : réservé pour un usage futur
  - ECN/NS : signale la présence de congestion, voir RFC 31684 ; ou Nonce Signaling, voir RFC 35405
  - CWR : Congestion Window Reduced : indique qu'un paquet avec ECE a été reçu et que la congestion a été traitée
  - ECE : ECN-Echo : si SYN=1 indique la capacité de gestion ECN, si SYN=0 indique une congestion signalée par IP (voir RFC 3168)
  - URG : Signale la présence de données urgentes
  - ACK : signale que le paquet est un accusé de réception (acknowledgement)
  - PSH : données à envoyer tout de suite (push)
  - RST : rupture anormale de la connexion (reset)
  - SYN : demande de synchronisation ou établissement de connexion
  - FIN : demande la fin de la connexion
- Fenêtre : taille de fenêtre demandée, c'est-à-dire le nombre d'octets que le récepteur souhaite recevoir sans accusé de réception
- Somme de contrôle : somme de contrôle calculée sur l'ensemble de l'en-tête TCP et des données, mais aussi sur un pseudo en-tête (extrait de l'en-tête IP)
- Pointeur de données urgentes : position relative des dernières données urgentes
- Options : options TCP, si l'en-tête est plus long que 20 octets
- Remplissage : remplissage pour aligner l'en-tête sur un mot de 32 bits

**Source : https://fr.wikipedia.org/wiki/Transmission_Control_Protocol**s