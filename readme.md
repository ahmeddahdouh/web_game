# README

## Instructions

### 1. Créer un environnement virtuel Python
```bash
python -m venv venv
```

Activez l'environnement virtuel :
- **Windows** :
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux** :
  ```bash
  source venv/bin/activate
  ```

### 2. Installer Poetry
```bash
pip install poetry
```

### 3. Installer les dépendances
Assurez-vous d'avoir un fichier `pyproject.toml` dans votre projet, puis exécutez :
```bash
poetry install
```

### 4. Créer un fichier `.env`
Dans la racine du projet, créez un fichier nommé `.env` et ajoutez les variables suivantes :
```
DB_USER=postgres
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
SECRET_KEY=
```
Renseignez les valeurs appropriées pour chaque variable.

### 5. Appliquer les migrations de base de données
Exécutez la commande suivante pour appliquer les migrations avec Alembic :
```bash
alembic upgrade head
```

### 6. Lancer l'application FastAPI
Exécutez la commande suivante pour démarrer l'application avec Uvicorn sur le port 8090 :
```bash
uvicorn app.main:app --reload --port 8090
```
Remplacez `app.main:app` par le chemin correct vers votre instance FastAPI si nécessaire.
