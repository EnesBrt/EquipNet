  
README.md

CMBD - Configuration Management Database

![License](https://img.shields.io/badge/License-MIT-blue.svg) (LICENSE)


Overview

CMBD (Configuration Management Database) est une application web conçue pour la gestion des équipements réseau. Cette application permet aux utilisateurs d'ajouter, de supprimer, ou de modifier des informations sur les équipements réseau, et vérifie si ces équipements sont opérationnels (actif) ou non (inactif).

  

Fonctionnalités

-   Ajout d'équipements : Permet d'ajouter de nouveaux équipements réseau au système.
    
-   Suppression d'équipements : Supprime les équipements qui ne sont plus en service ou pertinents.
    
-   Modification d'équipements : Update les informations des équipements existants.
    
-   Vérification de l'état : Vérifie et met à jour l'état de chaque équipement (actif ou inactif).
    

  

Technologies Utilisées

-   Backend : Python, Django, Netmiko
    
-   Frontend : HTML, CSS, Bulma
    
-   Base de données : PostgreSQL
    

  

Installation

1.  Cloner le dépôt :
    
    bash
    
    ```bash
    git clone https://github.com/EnesBrt/CMBD.git
    ```
    
2.  Installer les dépendances :
    
    -   Naviguez vers le dossier du projet.
        
    -   Installez les dépendances via pip, npm, ou autre gestionnaire de paquets selon ce qui est utilisé.
        
3.  Configurer la base de données :
    
    -   Assurez-vous que votre environnement de base de données est configuré correctement.
        
    -   Migrez la base de données si nécessaire.
        
4.  Lancer l'application :
    
    -   Exécutez le script de démarrage ou la commande spécifique pour votre environnement.
        

  

Utilisation

-   Accédez à l'application via une interface web après avoir lancé le serveur.
    
-   Utilisez les formulaires ou les interfaces graphiques pour gérer les équipements réseau.
    

  

Contribution

Toute contribution est la bienvenue ! Pour contribuer :

  

1.  Fork le référentiel
    
2.  Créez votre branche de fonctionnalité (git checkout -b feature/AmazingFeature)
    
3.  Committez vos changements (git commit -m 'Add some AmazingFeature')
    
4.  Poussez vers la branche (git push origin feature/AmazingFeature)
    
5.  Ouvrez une Pull Request
