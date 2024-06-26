# Multi-Django

Un même projet Django relativement simple (Gestion de Tâches aussi appelée _ToDo List_), décliné en différentes versions.

Chaque branche représente une version différente.

**_Attention!_**  
Le but n'est pas de proposer un projet prêt à être déployé en production. Les settings, par exemple, sont partagés ici à titre **pédagogique** mais c'est fortement déconseillé en production ou alors avec beaucoup de précautions ! 

Ce n'est qu'un exemple pour montrer "certains" aspects de Django.  
Ca me permet aussi d'avoir rapidement un projet Django de "test" ou des "snippets".


## Les branches


### Branche "main"

C'est la branche qui contient ce ReadMe: seulement les explications du dépôt !


### Branche "django"

C'est la version la plus "minimaliste" du projet. Juste un modèle et une interface front en HTML pur pour gérer le CRUD.  

En d'autres termes, on peut voir la liste des tâches, ajouter, modifier ou supprimer une tâche.  
On peut aussi clôturer une tâche.

[Lien vers cette branche](https://github.com/GeraldB69/Multi-Django/tree/django)


### Branche "django-bootstrap"

Seul changement avec la version "django" précédente: l'ajout de Bootstrap pour rendre l'interface HTML plus sympa !

[Lien vers cette branche](https://github.com/GeraldB69/Multi-Django/tree/django-bootstrap)


### Branche "django-drf"

Mise en place de [Django Rest Framework](https://www.django-rest-framework.org/) pour gérer les tâches sous forme d'API.   
Ajout de tests plus poussés et suppression de toute la partie front créée précédemment.

[Lien vers cette branche](https://github.com/GeraldB69/Multi-Django/tree/django-drf)


### Branche "django-drf-js"

Comment utiliser notre API DRF depuis le front...

_Work in progress..._
