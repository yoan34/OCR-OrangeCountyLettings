### Créer l'environnement virtuel

- `python -m venv venv`
- `apt-get install python3-venv`
- Activer l'environnement `source venv/bin/activate` pour window ou `. venv/bin/activate` pour linux.

### Exécuter le site

Pour lancer le site en locale:
- `source venv/bin/activate` ou `. venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.

### Linting

Pour lancer le linting, activer l'environnement de travail:
- `source venv/bin/activate` ou `. venv/bin/activate`
- `flake8`

### Tests unitaires

Pour lancer les tests, activer l'environnement de travail:
- `source venv/bin/activate` ou `. venv/bin/activate`
- `pytest`


### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Déploiement
Le déploiement se déroule en plusieurs étapes à partir d'un **push** sur la branche **main** qui va déclencher les processus de CI/CD à l'aide de CircleCI:
- L'application est compilé/analysé et testé avec la commande `python3 manage.py test`
- Création d'une image à l'aide de docker et ajouté au Dockerhub.
- Connexion, ajout et mise en ligne de l'application conteneurisée avec Heroku

Son URL: **https://oc-lettings-20.herokuapp.com/**

Pour que le déploiement fonctionne correctement il faut:
- que le code source n'est pas d'erreur
- que tous les tests se valide.
- la création de l'image de l'ajout au Dockerhub sans erreur.
- la connexion est l'ajout de l'image au registre de Heroku et sa mise en ligne.
