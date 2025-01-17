# Clock
projet de groupe à quatre
# Clock with Alarm

## Description

Ce projet implémente une horloge numérique interactive avec une fonctionnalité d'alarme. L'utilisateur peut choisir le format de l'heure (12h ou 24h), définir une heure de départ et, éventuellement, configurer une alarme. L'application affiche en continu l'heure et déclenche un message lorsque l'alarme est activée.

---

## Fonctionnalités

- **Affichage de l'heure :**
  - Format 12 heures (AM/PM) ou 24 heures.
  - Incrémentation des secondes, minutes et heures.

- **Alarme :**
  - Possibilité de définir une alarme pour une heure précise.
  - Affichage d'un message "Ring ring! Ring ring!" lorsque l'alarme se déclenche.
  - L'alarme reste active pendant 10 secondes.

- **Interactions utilisateur :**
  - Saisie de l'heure de départ et de l'heure de l'alarme.
  - Choix entre format 12 heures ou 24 heures.

---

## Structure des fichiers

- **`test.py`** : Contient le script principal pour exécuter l'horloge et l'alarme.
- **`timeclass.py`** : Implémente les classes principales `Time` et `Alarm`.

---

## Prérequis

- Python 3.x
- Bibliothèques Python :
  - `time`
  - `keyboard`

---

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/<nom-utilisateur>/<nom-du-depot>.git
   ```
2. Accédez au répertoire:  
   ```bash
   cd clock  
   ```
3. Installez les bibliothèques nécessaires :
   ```bash
   pip install keyboard
   ```
# Utilisation  

1. Lancez le programme :
   ```bash
   python test.py
   ```
2. Suivez les instructions à l'écran pour :
   + Choisir le format d'heure (12h/24h).
   + Définir une heure de départ.
   + Configurer une alarme (optionnel).
3. Appuyez sur la touche A pour interagir avec le programme et sur B pour quitter une action spécifique.

___

## Classes et Methodes  

### Classe `Time`

La classe `Time` permet de gérer l'heure, les minutes et les secondes, ainsi que d'incrémenter l'heure en fonction du temps écoulé.

#### Attributs

```plaintext
- **min_hour** : Valeur minimale de l'heure, par défaut 0.
- **max_hour** : Valeur maximale de l'heure, par défaut 23.
- **max_second_minute** : Valeur maximale des minutes et secondes, par défaut 59.
````

#### Methodes  
- **`__init__(self, hour, minute, second, format="24h")`** : Initialise l'heure, les minutes, et les secondes. Le format par défaut est "24h".
- **`in_seconds(self)`** : Retourne l'heure sous forme de secondes depuis minuit.
- **`increment_time(self)`** : Incrémente l'heure d'une seconde, gère le passage des minutes et des heures.
- **`__str__(self)`** : Retourne l'heure sous forme de chaîne de caractères dans le format spécifié (12h ou 24h).

### Explication détaillée

- **Attributs** : Cette section décrit les attributs principaux de la classe `Time`, comme les heures minimales et maximales, ainsi que les limites des secondes et des minutes.
  
- **Méthodes** :  
  - `__init__`: Cette méthode initialise l'heure à partir des paramètres donnés et définit le format de l'heure (12h ou 24h).  
  - `in_seconds`: Retourne l'heure sous forme de secondes depuis minuit, ce qui permet d'effectuer des calculs de comparaison avec d'autres horaires.  
  - `increment_time`: Cette méthode incrémente l'heure d'une seconde, gère le passage des secondes, minutes, et heures, et redémarre l'horloge si nécessaire (par exemple, de 23:59:59 à 00:00:00).  
  - `__str__`: Retourne l'heure sous forme d'une chaîne de caractères formatée, en fonction du format de l'heure spécifié.  

---

Ainsi, la classe `Time` est décrite dans un format similaire à celui de la classe `Alarm`, avec un bloc de code pour chaque méthode et attribut important. Ce format est à la fois facile à lire et permet de bien organiser l'information.

### Classe `Alarm`

Cette classe hérite de la classe `Time` et permet de gérer l'alarme. Elle inclut des fonctionnalités spécifiques pour activer l'alarme et afficher un message de notification lorsqu'elle se déclenche.

#### Attributs

```plaintext
- **max_display** : Durée maximale (en secondes) pendant laquelle le message de l'alarme reste visible après son déclenchement (par défaut 10 secondes).
- **enabled** : Indique si l'alarme est activée ou non.
```

#### Methodes
- **`__init__(self, hour, minute, second, format, enabled=False)`** : Initialise l'alarme avec l'heure, les minutes, et les secondes, ainsi que le format de l'heure (12h ou 24h). Si l'alarme est activée, l'attribut `enabled` sera `True`.
- **`__str__(self)`** : Affiche l'heure de l'alarme sous forme lisible, mais uniquement si l'alarme est activée.


Dans cet exemple, le texte à l'intérieur des balises ` ```plaintext ` sera affiché avec un fond gris, créant l'effet que vous recherchez.

### Résultat attendu :

- Le titre **Classe `Alarm`** et le texte décrivant la classe sont normaux.
- Les attributs et méthodes de la classe sont affichés avec un fond gris, comme dans un bloc de code.

## Fonctionnalités supplémentaires
+ Gestion de l'alarme : Lorsqu'une alarme est définie, un message "Ring ring! Ring ring!" est affiché à l'écran lorsque l'heure de l'alarme est atteinte.
+ Affichage dynamique : L'interface mise à jour chaque seconde affiche en temps réel l'heure actuelle ainsi que l'alarme (si activée). Le message de l'alarme reste visible pendant 10 secondes.
+ Interaction utilisateur via le clavier : Le programme peut être contrôlé via les touches "A" pour interagir et "B" pour quitter une action spécifique.



## Contributions 
 
Les contributions sont les bienvenues ! Si vous souhaitez contribuer au projet, veuillez suivre ces étapes :

1.Fork le dépôt.  
2.Créez une branche pour votre fonctionnalité (git checkout -b feature/your-feature).  
3.Commit vos changements (git commit -am 'Add new feature').  
4.Push sur la branche (git push origin feature/your-feature).  
5.Ouvrez une pull request.  
_______

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

Si vous avez d'autres questions ou des suggestions pour améliorer ce projet, n'hésitez pas à ouvrir un problème ou une pull request !

Cela peut varier légèrement selon la plateforme qui interprète le Markdown (GitHub, GitLab, etc.).

___

## Fonctionnalites Supplémentaires
+ Gestion de l'alarme : Lorsqu'une alarme est définie, un message "Ring ring! Ring ring!" est affiché à l'écran lorsque l'heure de l'alarme est atteinte.
+ Affichage dynamique : L'interface mise à jour chaque seconde affiche en temps réel l'heure actuelle ainsi que l'alarme (si activée). Le message de l'alarme reste visible pendant 10 secondes.
+ Interaction utilisateur via le clavier : Le programme peut être contrôlé via les touches "A" pour interagir et "B" pour quitter une action spécifique.



## Contributions 
 
Les contributions sont les bienvenues ! Si vous souhaitez contribuer au projet, veuillez suivre ces étapes :

1.Fork le dépôt.
2.Créez une branche pour votre fonctionnalité (git checkout -b feature/your-feature).
3.Commit vos changements (git commit -am 'Add new feature').
4.Push sur la branche (git push origin feature/your-feature).
5.Ouvrez une pull request.
_______

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

Si vous avez d'autres questions ou des suggestions pour améliorer ce projet, n'hésitez pas à ouvrir un problème ou une pull request !
