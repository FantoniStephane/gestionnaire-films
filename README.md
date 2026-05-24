# 🎬 Gestionnaire de films

> Mini-application console pour gérer une collection de films stockée dans un fichier CSV — Python, csv, menu interactif.

---

## 🚀 Ce que fait ce programme

- Ajouter un film à la collection
- Afficher tous les films enregistrés
- Rechercher un film par titre (insensible à la casse)
- Supprimer un film de la liste
- Marquer un film comme vu
- Sauvegarde automatique après chaque modification

---

## 📦 Technologies utilisées

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- `csv` — lecture et écriture des données (module intégré Python)
- `os` — gestion des fichiers (module intégré Python)

---

## 🖥️ Exemple de déroulé

```
=== Gestionnaire de films ===

[1]  Ajouter un film
[2]  Lister les films
[3]  Recherche un film
[4]  Supprimer un film
[5]  Marquer comme vu
[6]  Afficher les statistiques
[7]  Quitter

Votre choix : 2

INCEPTION (2010) - SF - oui
TITANIC (1997) - Romance - oui
```

---

## ⚙️ Installation

```bash
# 1. Cloner le repo
git clone https://github.com/FantoniStephane/gestionnaire-films.git
cd gestionnaire-films

# 2. Créer et activer l'environnement virtuel
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

Aucune dépendance externe — modules intégrés Python uniquement.

---

## ▶️ Lancement

```bash
python main.py
```

---

## 📁 Structure du projet

```
gestionnaire-films/
├── main.py          ← programme principal
├── functions.py     ← fonctions métier
├── movies.csv       ← base de données films
├── movies.json      ← export JSON de la collection
├── stats.json       ← statistiques de la collection
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🎓 Contexte

Projet réalisé dans le cadre de la formation **CD2IA** à la Metz Numeric School.  
Notions mobilisées : fonctions, lecture/écriture CSV, menu interactif, gestion de fichiers.

---

*Une collection bien rangée, c'est une soirée bien choisie. 🍿*
