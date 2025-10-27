# 🚀 ScrapifyAPI

**ScrapifyAPI** est une API REST légère de web scraping construite avec FastAPI et BeautifulSoup. Elle permet d'extraire des données structurées depuis des sites web (citations, offres d'emploi, produits, etc.) et de les exposer via une API RESTful moderne et performante.

Ce projet démontre comment construire une architecture complète combinant **ingestion de données** et **couche API** — deux compétences essentielles en data engineering.

---

## 📋 Table des matières

- [Fonctionnalités](#-fonctionnalités)
- [Architecture du projet](#-architecture-du-projet)
- [Technologies utilisées](#-technologies-utilisées)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Endpoints de l'API](#-endpoints-de-lapi)
- [Structure des données](#-structure-des-données)
- [Déploiement](#-déploiement)
- [Développement](#-développement)
- [Contribuer](#-contribuer)
- [Licence](#-licence)

---

## ✨ Fonctionnalités

- 🌐 **Web Scraping automatisé** : Extraction de citations depuis [quotes.toscrape.com](https://quotes.toscrape.com/)
- 🔄 **API REST moderne** : Exposition des données via FastAPI avec documentation interactive
- 📊 **Validation des données** : Utilisation de Pydantic pour garantir la cohérence des données
- 🚀 **Performances optimales** : API asynchrone avec FastAPI
- 📖 **Documentation automatique** : Swagger UI et ReDoc intégrés
- ☁️ **Prêt pour le cloud** : Configuration pour déploiement sur Render.com
- 🧹 **Nettoyage des données** : Traitement et normalisation automatique des textes extraits

---

## 🏗️ Architecture du projet

```
ScrapifyAPI/
│
├── app/
│   ├── __init__.py          # Initialisation du package
│   ├── main.py              # Point d'entrée FastAPI et définition des routes
│   ├── models.py            # Modèles Pydantic pour la validation des données
│   ├── scraper.py           # Logique de web scraping avec BeautifulSoup
│   └── utils.py             # Fonctions utilitaires (nettoyage de texte, etc.)
│
├── requirements.txt         # Dépendances Python du projet
├── render.yaml             # Configuration pour déploiement sur Render
└── README.md               # Documentation du projet
```

### Description des modules

#### 📄 `app/main.py`
Fichier principal de l'application contenant :
- Configuration de l'application FastAPI
- Définition des routes et endpoints
- Gestion globale des erreurs
- Métadonnées de l'API (titre, description, version)

#### 📦 `app/models.py`
Définit les modèles de données avec Pydantic :
- **Quote** : Modèle représentant une citation avec validation automatique
  - `quote` (str) : Le texte de la citation
  - `author` (str) : L'auteur de la citation
  - `tags` (List[str]) : Liste des tags associés

#### 🕷️ `app/scraper.py`
Contient la logique de web scraping :
- Connexion HTTP au site cible
- Parsing HTML avec BeautifulSoup
- Extraction des données structurées
- Gestion des erreurs de connexion

#### 🛠️ `app/utils.py`
Fonctions utilitaires pour le traitement des données :
- `clean_text()` : Nettoie et normalise les chaînes de caractères
- Suppression des espaces superflus et des sauts de ligne

---

## 🛠️ Technologies utilisées

- **[FastAPI](https://fastapi.tiangolo.com/)** (v0.100+) - Framework web moderne et rapide pour construire des APIs
- **[Uvicorn](https://www.uvicorn.org/)** - Serveur ASGI haute performance
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** - Bibliothèque de parsing HTML/XML
- **[Requests](https://requests.readthedocs.io/)** - Client HTTP simple et élégant
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Validation des données avec Python type hints

---

## 📦 Prérequis

- **Python** 3.8 ou supérieur
- **pip** (gestionnaire de paquets Python)
- Connexion Internet (pour le scraping)

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/Honkpehedji-Stanley/ScrapifyAPI.git
cd ScrapifyAPI
```

### 2. Créer un environnement virtuel (recommandé)

```bash
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Linux/Mac :
source venv/bin/activate

# Sur Windows :
venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 💻 Utilisation

### Lancer le serveur en local

```bash
uvicorn app.main:app --reload
```

Options disponibles :
- `--reload` : Redémarrage automatique lors de modifications du code (développement)
- `--host 0.0.0.0` : Écoute sur toutes les interfaces réseau
- `--port 8000` : Spécifier un port personnalisé (8000 par défaut)

Le serveur sera accessible à l'adresse : **http://127.0.0.1:8000**

### Accéder à la documentation interactive

Une fois le serveur lancé, vous pouvez accéder à :

- **Swagger UI** : http://127.0.0.1:8000/docs
- **ReDoc** : http://127.0.0.1:8000/redoc

Ces interfaces vous permettent de tester directement les endpoints de l'API.

---

## 🔌 Endpoints de l'API

### 1. Route d'accueil

**GET** `/`

Endpoint de bienvenue pour vérifier que l'API fonctionne.

**Réponse :**
```json
{
  "message": "Welcome to ScrapifyAPI 👋"
}
```

### 2. Récupérer les citations

**GET** `/api/quotes`

Récupère toutes les citations disponibles depuis le site web cible.

**Réponse :**
```json
[
  {
    "quote": "The world as we have created it is a process of our thinking...",
    "author": "Albert Einstein",
    "tags": ["change", "deep-thoughts", "thinking", "world"]
  },
  {
    "quote": "It is our choices, Harry, that show what we truly are...",
    "author": "J.K. Rowling",
    "tags": ["abilities", "choices"]
  }
]
```

**Codes de statut :**
- `200 OK` : Récupération réussie
- `500 Internal Server Error` : Erreur lors du scraping (site inaccessible, parsing échoué, etc.)

---

## 📊 Structure des données

### Modèle Quote

```python
{
  "quote": str,      # Texte de la citation (obligatoire)
  "author": str,     # Nom de l'auteur (obligatoire)
  "tags": List[str]  # Liste des tags associés (obligatoire, peut être vide)
}
```

**Exemple :**
```json
{
  "quote": "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.",
  "author": "Albert Einstein",
  "tags": ["change", "deep-thoughts", "thinking", "world"]
}
```

---

## ☁️ Déploiement

### Déploiement sur Render.com

Le projet inclut un fichier `render.yaml` pour un déploiement simple sur Render.

#### Configuration (`render.yaml`)

```yaml
services:
  - type: web
    name: scrapifyapi
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn app.main:app --host 0.0.0.0 --port 10000"
```

#### Étapes de déploiement :

1. Créez un compte sur [Render.com](https://render.com)
2. Connectez votre dépôt GitHub
3. Créez un nouveau "Web Service"
4. Render détectera automatiquement le fichier `render.yaml`
5. Cliquez sur "Deploy"

Votre API sera accessible via une URL fournie par Render (ex: `https://scrapifyapi.onrender.com`)

### Déploiement sur d'autres plateformes

Le projet peut également être déployé sur :
- **Heroku** : Ajoutez un `Procfile` avec `web: uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- **Railway** : Utilisez la détection automatique
- **Google Cloud Run** : Créez un `Dockerfile`
- **AWS Elastic Beanstalk** : Utilisez la configuration Python

---

## 🔧 Développement

### Tester l'API avec curl

```bash
# Test de la route d'accueil
curl http://127.0.0.1:8000/

# Récupération des citations
curl http://127.0.0.1:8000/api/quotes
```

### Tester avec Python

```python
import requests

# Récupérer les citations
response = requests.get("http://127.0.0.1:8000/api/quotes")
quotes = response.json()

for quote in quotes:
    print(f"📖 {quote['quote']}")
    print(f"✍️  — {quote['author']}")
    print(f"🏷️  Tags: {', '.join(quote['tags'])}\n")
```

### Ajouter un nouveau site à scraper

Pour scraper un nouveau site :

1. Créez une nouvelle fonction dans `app/scraper.py`
2. Définissez un nouveau modèle dans `app/models.py` si nécessaire
3. Ajoutez un nouveau endpoint dans `app/main.py`

**Exemple :**

```python
# Dans app/scraper.py
def scrape_jobs():
    # Votre logique de scraping
    pass

# Dans app/main.py
@app.get("/api/jobs", response_model=List[Job])
def get_jobs():
    try:
        jobs = scrape_jobs()
        return jobs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Voici comment contribuer :

1. **Forkez** le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une **Pull Request**

### Bonnes pratiques

- Suivez les conventions PEP 8 pour le code Python
- Ajoutez des tests pour les nouvelles fonctionnalités
- Documentez les nouvelles fonctions et endpoints
- Mettez à jour le README si nécessaire

---

## 📝 Améliorations futures

- [ ] Ajout d'un cache Redis pour améliorer les performances
- [ ] Pagination des résultats pour les grandes collections
- [ ] Authentification API avec tokens JWT
- [ ] Support de plusieurs sources de données
- [ ] Export des données en CSV/JSON
- [ ] Scraping asynchrone pour de meilleures performances
- [ ] Base de données pour stocker l'historique des données
- [ ] Rate limiting pour éviter la surcharge du serveur
- [ ] Système de logs avancé
- [ ] Tests unitaires et d'intégration

---

## 📄 Licence

Ce projet est un projet éducatif et de démonstration. Libre d'utilisation et de modification.

---

## 👤 Auteur

**Stanley Honkpehedji**

- GitHub: [@Honkpehedji-Stanley](https://github.com/Honkpehedji-Stanley)

---

## ⚠️ Avertissement

Ce projet est à but éducatif. Lors du scraping de sites web :
- Respectez les conditions d'utilisation des sites web
- Vérifiez le fichier `robots.txt` du site cible
- Ne surchargez pas les serveurs avec des requêtes excessives
- Respectez la propriété intellectuelle des données

---

## 📚 Ressources utiles

- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Guide Pydantic](https://pydantic-docs.helpmanual.io/)
- [Web Scraping Best Practices](https://www.scrapingbee.com/blog/web-scraping-best-practices/)

---

<div align="center">
  Fait avec ❤️ et Python 🐍
</div>
