# SaveBrowser
Browser Backup App

Une application graphique simple pour sauvegarder et restaurer les profils de navigateur pour les navigateurs Firefox et Edge sur le système d'exploitation Windows. L'application crée un fichier zip du dossier du profil du navigateur pour la sauvegarde et extrait le fichier de sauvegarde dans le dossier du profil du navigateur pour la restauration. Commencer
Getting Started

Pour utiliser cette application, suivez ces étapes:

    Clonez le référentiel sur votre ordinateur local.
    Installez les bibliothèques requises à l'aide de pip install -r requirements.txt.
    Exécutez le script browser_backup.py pour démarrer l'application.
    Sélectionnez les navigateurs à sauvegarder/restaurer, le dossier d'exportation des fichiers de sauvegarde et cliquez sur le bouton Sauvegarder/Restaurer pour effectuer l'opération.


Prerequisites

    Python 3.x
    PySimpleGUI
    zipfile
    shutil

Usage

Lorsque vous exécutez le script browser_backup.py, la fenêtre GUI apparaît. Vous pouvez sélectionner les navigateurs à sauvegarder/restaurer en cochant les cases de Firefox et/ou Edge. Vous pouvez également sélectionner le dossier d'exportation pour les fichiers de sauvegarde en cliquant sur le bouton "..." à côté du champ de saisie.

Pour effectuer une sauvegarde, cliquez sur le bouton Sauvegarder. L'application créera un nouveau dossier avec le nom du navigateur dans le dossier d'exportation, copiera le dossier du profil du navigateur dans le nouveau dossier, créera un fichier zip du nouveau dossier et supprimera le nouveau dossier.

Pour effectuer une restauration, cliquez sur le bouton Restaurer. L'application vous demandera de sélectionner le fichier de sauvegarde à restaurer. Une fois que vous avez sélectionné le fichier de sauvegarde, l'application extraira le fichier de sauvegarde dans le dossier du profil du navigateur.

Contributing

Les contributions à ce projet sont les bienvenues. Vous pouvez contribuer en :

    Ajout de la prise en charge d'autres navigateurs et plates-formes.
    Ajout de fonctionnalités supplémentaires à l'application.
    Correction de bogues et de problèmes.

License

This project is licensed under the MIT License - see the LICENSE file for details.
