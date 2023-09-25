Procédure de déploiement :
**************************

Configuration de Render :
=========================

La platforme choisi est Render.

a. Paramétrage :

Avec votre compte Render, depuis la page d'accueil :
- Cliquez sur "Add New" (Ajouter un nouveau) puis sélectionnez "Web Service" (Service web).

- Dans la section "Repository" (Dépôt), sélectionnez votre service de contrôle de version (par exemple, GitHub, GitLab ou Bitbucket) et connectez votre compte.

- Sélectionnez le dépôt qui contient votre projet Django.

- Ajouter le nom de votre site, le répertoire parent, et le "runtime"(docker)
  Choisissez votre plan de paiement.

- Cliquez sur Create Web Service(Creez le service web)

- Dans la section "Environment" (Environnement), vous pouvez spécifier les variables d'environnement nécessaires pour votre projet. Par exemple, vous pouvez définir la variable SECRET_KEY, SENTRY_DSN ou d'autres variables personnalisées.
