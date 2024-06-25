---

# Evolution des Papillons

Ce projet est une simulation de l'évolution des générations de papillons en utilisant un modèle mathématique. Le programme en Python génère des données pour visualiser cette évolution et les imprime sous un format compatible avec gnuplot.

## Table des Matières
1. [Introduction]
2. [Modèle Mathématique]
3. [Prérequis]
4. [Installation]
5. [Utilisation]
6. [Sortie du Programme]
7. [Exemples]
8. [Contributeurs]
9. [Licence]

## Introduction

Ce projet simule l'évolution de la population de papillons sur plusieurs générations selon un modèle mathématique simple. Les résultats sont destinés à être visualisés à l'aide de gnuplot.

## Modèle Mathématique

Le modèle utilisé est défini comme suit :

- x_i = n où n est le nombre d'individus de la première génération.
- x_{i+1} = (k * x_i * (1000 - x_i)) / 1000 pour i >= 1, k étant le taux de croissance, compris entre 1 et 4.

## Prérequis

- Python 3
- gnuplot pour la visualisation des données

## Installation

Clonez le dépôt Git :

```bash
git clone https://git@github.com:florian-labadie/106-Bombyx.git
cd evolution-papillons
```

## Utilisation

Le programme peut être utilisé de deux manières :

1. Pour spécifier un taux de croissance \( k \) :
   ```bash
   ./106bombyx n k > data
   ```

2. Pour spécifier une génération initiale et finale :
   ```bash
   ./106bombyx n i0 i1 > data
   ```

### Arguments

- `n` : Nombre d'individus de la première génération
- `k` : Taux de croissance de 1 à 4
- `i0` : Génération initiale (incluse)
- `i1` : Génération finale (incluse)

## Sortie du Programme

Le programme génère des données au format suivant, qui peuvent être directement utilisées avec gnuplot :

```
k xi
1.00 0.10
1.01 9.90
...
```

## Exemples

### Utilisation avec un taux de croissance spécifique

Pour générer des données pour n = 10 et k = 2.5:

```bash
./106bombyx 10 2.5 > data
```

### Utilisation avec une génération initiale et finale

Pour générer des données pour n = 10 de la génération 1000 à 1010 :

```bash
./106bombyx 10 1000 1010 > data
```
### Affichage graphique

Pour afficher le graphique de bifurcation vers le chaos.

```bash
cat drawer.gnu | gnuplot
```
## Contributeurs

- Labadie Florian ([GitHub](https://github.com/florian-labadie))
- Axel Lavrador ([GitHub)](https://github.com/florian-labadie))

---
