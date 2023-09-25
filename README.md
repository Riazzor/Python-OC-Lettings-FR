[![Riazzor](https://circleci.com/gh/Riazzor/Python-OC-Lettings-FR.svg?style=shield)](https://app.circleci.com/pipelines/github/Riazzor/Python-OC-Lettings-FR)
[![Documentation Status](https://readthedocs.org/projects/python-orange-county-lettings/badge/?version=latest)](https://python-orange-county-lettings.readthedocs.io/fr/latest/?badge=latest)


## Résumé :

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Pour voir la couverture de test :  
- 'pytest --cov .'

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement :

### Image Docker :

- Pour créer l'image une fois vos modification effectuée :  
> docker build -t oc_lettings:<TAG> .  

- Pour créer le tag de l'image :  
> docker tag oc_lettings:<TAG> <REPO>/oc_lettings:<TAG>  

- Pour se logger sur docker hub depuis le terminal : (définir les variables d'environnement au préalable)
> echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin

- Pour pousser manuellement l'image sur docker hub :  (condition : être logger sur docker hub depuis votre terminal)  
> docker push <REPO>/oc_lettings:<TAG>

- Lancer l'application en local avec docker :  
> docker run --name oc_lettings -p 8000:8000 <REPO>/oc_lettings:<TAG>  
Puis aller sur l'adresse : http://localhost:8000/


### CI/CD :

L'intégration continue fonctionne de la façon suivante :  
- d'abord les tests sont lancés  
- puis si pas de soucis, l'image docker est créer puis poussé sur docker hub,  
- si la branche actuelle est master, l'application est déployé sur Render.

Cette méthode permet un déploiement continue automatique.  
Les différentes nouvelles features sont mergé à la branche develop, puis lorsque tout est mergé,
la branche develop est mergé à la branche master pour activer le déploiement.
