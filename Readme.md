# KPCA Appliqué

Ce petit write up fait suite à celui sur la découverte des KPCA disponible sur le dépot github **[ici](https://github.com/Matomatt/wyes-ai/tree/KPCA/Decouverte_KPCA)**. 
## Sommaire
* [1. Notre problème ](#1-notre-problème)
* [2. Reduction d'une dimension](#2-réduction-dune-dimension)
* [3. Reduction de deux dimensions](#3-réduction-de-deux-dimensions)
* [4. Reduction de trois dimensions](#4-réduction-de-trois-dimensions)
* [5. Reduction de quatre dimensions](#5-réduction-de-quatre-dimensions)
* [6. Reduction de cinq dimensions](#6-réduction-de-cinq-dimensions)
* [7. Notre code](#7-notre-code)
* [8. Conclusion](#8-conclusion)

## 1. Notre problème
La lecture des informations provenant du dispositif est composé de 12 capteurs (6 pour le coté gauche et 6 autres pour le cotés droit) ce qui nous offres un mouvement un décrit par **6 dimensionalités** pour chaque œil.

![image n°1](images/image_1.png)

> le graphique de gauche correspond aux 6 capteurs de gauche et le graphique de droite aux 6 capteurs situé à à droite. 

Afin d'optimiser et de simplifier notre démarche de reconnaissance et d'identification des mouvements, nous **nous proposons de réduire un maximum le nombre de composantes disponibles**. Nous utiliserons ici le principe de réduction de dimensionnalités permise par les KCPA.   

## 4. Reduction d'une dimension

## 5. Reduction de deux dimensions

## 6. Reduction de trois dimensions

## 7. Reduction de quatre dimensions

## 8. Reduction de cinq dimensions

## 9. Notre code
L'integralité du code se situe dans la classe [movement](movement.py). Le playload qui nous a permis de generer les images de ce write up est disponible dans le fichier [playload](playload.py)
Plusieurs méthodes ont été implémentés dans la classe **movement** : 
* Le constructeurs et les méthodes d'initialisation (tel que la lecture du dataset)
* Les methodes permettant de generer une visualition graphique des mouvements en fonction des capteurs et etc.
* La méthode **dimensionReduction** qui permet de "fusionner" deux capteurs afin de réduire le nombre de dimensions

## 9. Conclusion