# multi-factor-auth
Implementation of an electronic authentication method in which a user is granted access to a website only after successfully presenting two or more pieces of evidence (or factors).

Here are the prerequisites in order to run the project:

First of all, make sure you have a rather recent version of Python on your PC (starting from Python 3.10.11). Here is a link to download it : https://www.python.org/downloads/ .
If you are using Visual Studio, after cloning the project, open a cmd terminal and check if you already have Python installed with: python --version
Otherwise, install Python directly with the following command: pip install python .

It is possible that an error will be returned if you have not installed pip beforehand, and for the continuation it is important to obtain pip. If this is the case, go to the following link https://pip.pypa.io/en/stable/installation/ to download pip. Follow the steps (enter the two necessary commands) and download the 'get-pip' script from the link https://bootstrap.pypa.io/get-pip.py. Once these actions are done.

Install MySQL from your search engine or directly from the command line in vscode with: pip install mysqlclient

For any other errors related to the use of functionality and errors related to the non-recognition of commands from your Windows terminal (for example: python or mysql), take the time to apply access to your PATH environment variables. In "Environment Variables" and under "System Variables", search for the "Path" variable and click "Edit". Click "New" and add the path to python or mysql, for example.

Here are the commands to download the necessary packages for the project to function properly with pip:

pip install Django
pip install Django-widget-tweaks
pip install qrcode
pip install pyotp

Once this is done, create the MySQL database by referring to the information in the settings.py file.
Open a MySQL terminal session using the following command: mysql -u root -p
This will prompt you for the root user's password.

Create a new database using the following command:
CREATE DATABASE multifactor_auth_db
or manually from MySql Workbench using the same command.

Once the database is created, make sure that the configuration ports for the created database and the project are the same (3306) by default.
Once this is done, you can apply the necessary migrations to update the database with the command: python manage.py migrate
Finally, you can launch the server with the command: python manage.py runserver




-----------------------------------------------
Traduction en Français : 

Authentification multi-facteurs.
Mise en œuvre d'une méthode d'authentification électronique dans laquelle un utilisateur n'est autorisé à accéder à un site Web qu'après avoir présenté avec succès deux ou plusieurs éléments de preuve (ou facteurs).

Voici les prérequis afin de pouvoir lancer le projet :

Tout d'abord, assurez-vous d'avoir une version plutôt récente de Python sur votre PC (à partir de Python 3.10.11). Voici un lien pour vous permettre de le télécharger : https://www.python.org/downloads/
Si vous utilisez Visual Studio, après avoir cloné le projet, en ouvrant un terminal CMD, vérifiez si vous avez déjà Python installé avec la commande : python --version
Sinon, vous pouvez aussi installez Python directement avec la commande suivante : pip install python

Il est possible qu'une erreur soit renvoyée si vous n'avez pas installé pip au préalable, et pour la suite il est important d'obtenir pip. Si c'est le cas, rendez-vous sur le lien suivant https://pip.pypa.io/en/stable/installation/ afin de le télécharger. Suivez les étapes (entrez les deux commandes nécessaires) puis téléchargez le script "get-pip" depuis le lien https://bootstrap.pypa.io/get-pip.py. Une fois ces actions réalisées,

Installez MySQL depuis votre moteur de recherche ou bien directement en ligne de commande depuis VSCode avec : pip install mysqlclient

Pour toute autre erreur survenant concernant l'utilisation des fonctionnalités et des erreurs relatives à la non-reconnaissance des commandes depuis votre terminal Windows (exemple: python ou mysql), prenez le temps d'appliquer des accès à vos variables d'environnement PATH. Dans "Variables d'environnement" et sous "Variables système", cherchez la variable "Path" et cliquez sur "Modifier". Cliquez sur "Nouveau" et ajoutez le chemin d'accès à Python ou MySQL, par exemple.

Voici maintenant les commandes permettant de télécharger les packages nécessaires pour le bon fonctionnement du projet à installer avec pip :

pip install Django
pip install Django-widget-tweaks
pip install qrcode
pip install pyotp

Une fois cela réalisé, créez la base de données MySQL en vous reportant aux informations du fichier settings.py.
Ouvrez une session de terminal MySQL en utilisant la commande suivante : mysql -u root -p
Cela vous demandera le mot de passe de l'utilisateur root.

Créez une nouvelle base de données en utilisant la commande suivante :
CREATE DATABASE multifactor_auth_db;
ou manuellement depuis MySql Workbench avec la même commande.

Une fois la base de données créée, vérifiez bien que les ports de configuration de la base créée et du projet sont les mêmes (3306) par défaut.
Une fois cela réalisé, vous pouvez appliquer les migrations nécessaires à la mise à jour de la base de données avec la commande : python manage.py migrate
Enfin, vous pouvez lancer le serveur avec la commande : python manage.py runserver