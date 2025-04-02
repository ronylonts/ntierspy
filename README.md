

1.Introduction : Ce projet est une application de gestion de projets conçue pour aider les équipes à mieux collaborer, suivre les tâches et gérer les ressources de manière efficace.
Contexte : Dans un environnement de travail dynamique, il est essentiel d'avoir un système qui permet de centraliser la gestion des projets, d'améliorer la communication entre les membres de l'équipe et d'assurer un suivi précis des progrès.

2. Fonctionnalités détaillées :
   Gestion des projets et de leur cycle de vie : Créez, modifiez et suivez l'avancement des projets.
   Gestion des tâches : Assignez des tâches aux membres de l'équipe et suivez leur progression.
   Suivi du temps et des ressources : Enregistrez le temps passé sur chaque tâche et gérez les ressources allouées.
   Tableau de bord : Consultez un aperçu des projets en cours, des tâches et des indicateurs de performance.
  Système de notifications : Recevez des alertes concernant les échéances et les mises à jour des tâches.

3. Architecture du Projet :
   L'application est structurée selon l'architecture N-tiers, comprenant trois couches principales : 
     - **Couche de Présentation** : Interface utilisateur pour interagir avec l'application.
     - **Couche Métier** : Contient la logique d'affaires et les services.
     - **Couche de Données** : Gère l'accès aux données et la persistance.

4. **Technologies Utilisées :**
   - **Django** : Cadre de développement web rapide qui facilite la création d'applications.
   - **Django REST Framework** : Utilisé pour construire l'API REST de l'application.
   - **PostgreSQL** : Base de données relationnelle pour stocker les données de manière sécurisée et efficace.
   - **JWT (JSON Web Token)** : Système d'authentification pour sécuriser les accès aux API.

5. **Instructions d'Installation :**
   - Clonez le dépôt : `git clone https://github.com/votre_nom_utilisateur/nom_du_depot.git`
   - Accédez au répertoire du projet : `cd nom_du_depot`
   - Installez les dépendances : `pip install -r requirements.txt`
   - Configurez votre base de données dans le fichier `settings.py`.
   - Démarrez le serveur : `python manage.py runserver`

6. **Exemples d'Utilisation de l'API :**
   - Pour créer un projet :
     ```
     POST /api/projects
     {
       "title": "Nouveau Projet",
       "description": "Description du projet"
     }
     ```
   - Exemple de réponse :
     ```
     {
       "id": 1,
       "title": "Nouveau Projet",
       "description": "Description du projet",
       "status": "en cours"
     }
     ```

7. **Tests :**
   - Pour exécuter les tests unitaires, utilisez la commande :
     ```
     python manage.py test
     ```
   - Vous pouvez également voir des exemples de tests dans le répertoire `tests/`.

8. **Contributions :**
   - Les contributions sont les bienvenues ! Pour contribuer, veuillez créer un fork du projet, apporter vos modifications et soumettre une pull request avec une description claire de vos changements.

9. **Difficultés Rencontrées et Solutions :**
   - L'un des principaux défis a été la gestion des dépendances entre les tâches. Nous avons résolu cela en implémentant un système de priorités qui permet d'assigner des dépendances et des dates d'échéance claires.

10. **Contact :**
    - Pour toute question ou retour, veuillez contacter l'équipe à l'adresse email suivante : rolandlontsie604@gmail.com

