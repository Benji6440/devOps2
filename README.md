# TP DevOps - Pipelining avec GitHub Actions

| Exercice | Workflow | Déclencheur |
|---|---|---|
| 1. Hello World | `.github/workflows/01-hello-world.yml` | push, manuel |
| 2. Nom / prénom / email (3 jobs) | `.github/workflows/02-identite.yml` | push, manuel |
| 3. Script Python "Commit success!" | `.github/workflows/03-commit-success.yml` + `scripts/commit_success.py` | chaque push |
| 4. Nom de la branche | `.github/workflows/04-branch-name.yml` | push sur `Dev`, `Val`, `Prod` |
| 5. Division Dev / Val / Prod | `.github/workflows/05-division.yml` + `scripts/divide.py` | push, manuel (avec un nombre) |
| Avancé. GitHub Pages | `.github/workflows/06-github-pages.yml` + `site/index.html` | push sur `main` |

## Mise en place

1. Pousser le repo sur GitHub avec toutes les branches :
   ```bash
   git remote add origin https://github.com/<user>/<repo>.git
   git push -u origin main Dev Val Prod
   ```
2. Exercice 2 : créer les variables `NOM`, `PRENOM`, `EMAIL` dans
   *Settings > Secrets and variables > Actions > Variables*
   (ou `gh variable set NOM --body "..."`). On utilise des variables et pas des
   secrets, sinon GitHub masque les valeurs (`***`) dans les logs.
3. Exercice avancé : *Settings > Pages > Build and deployment > Source* = **GitHub Actions**,
   puis relancer le workflow 06. Le site est publié sur `https://<user>.github.io/<repo>/`.

## Exercice 5 : fonctionnement

Trois jobs enchaînés avec `needs` : `Dev` (÷2) → `Val` (÷4) → `Prod` (÷8).
Chaque job vérifie que le nombre qu'il reçoit est pair. Sinon il échoue et les jobs
suivants ne sont pas lancés. Le résultat passe d'un job à l'autre par les `outputs`.

- `128` : 64 → 16 → 2 ✅
- `12` : 6 → 1.5 → arrêt en Prod ❌
- `7` : arrêt dès Dev ❌

Lancement manuel : *Actions > 05 - Division Dev Val Prod > Run workflow* et saisir le nombre.
