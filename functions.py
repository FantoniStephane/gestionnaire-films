import os
import csv
import json
 
# Dossier du fichier .py (trouvé dans la doc Python)
DOSSIER = os.path.dirname(os.path.abspath(__file__))
FICHIER = os.path.join(DOSSIER, "movies.csv")       
MOVIES_JSON = os.path.join(DOSSIER, "movies.json")  
STATS_JSON = os.path.join(DOSSIER, "stats.json")    
COLONNES = ['Titre du film', 'Année de sortie', 'Genre du film', 'Déjà vu']
 
def mettre_a_jour_stats():
    """Régénère movies.json et stats.json après chaque modification."""
    exporter_json()
    creer_stats_json()
 
 
def creer_fichier_si_absent():
    """Crée le fichier CSV s'il n'existe pas."""
    if not os.path.exists(FICHIER):
        with open(FICHIER, 'w', newline='') as f:
            ecriture = csv.DictWriter(f, fieldnames=COLONNES)
            ecriture.writeheader()
    mettre_a_jour_stats()  # Initialise les stats au démarrage
 
def add_film():
    """Demande à l'utilisateur les infos et ajoute un film dans le CSV."""
    titre = input("\nNom du film : ").strip().upper()  
    annee = input("Année du film : ")
    genre = input("Le genre du film : ")
    vu = input("Déjà vu ? oui/non : ")
 
    with open(FICHIER, 'a', newline='') as f:
        ecriture = csv.DictWriter(f, fieldnames=COLONNES)
        ecriture.writerow({
            'Titre du film': titre,
            'Année de sortie': annee,
            'Genre du film': genre,
            'Déjà vu': vu
        })
 
 
def liste_film():
    """Affiche tous les films enregistrés dans le CSV."""
    with open(FICHIER, 'r') as f:
        lecture = csv.DictReader(f)
        for row in lecture:
            print(f"\n{row['Titre du film']} ({row['Année de sortie']}) - {row['Genre du film']} - {row['Déjà vu']}")
 
 
def recherche_film():
    """Recherche un film."""
    titre_recherche = input("\nTitre du film à chercher : ").lower()
    
    with open(FICHIER, 'r') as f:
        lecture = csv.DictReader(f)
        trouve = False
        
        for row in lecture:
            if row['Titre du film'].lower() == titre_recherche:
                print(f"\nTrouvé : {row['Titre du film']} ({row['Année de sortie']}) - {row['Genre du film']} - {row['Déjà vu']}")
                trouve = True
        
        if not trouve:
            print("Film inconnu.")      
 
def supprimer_film():
    """Supprime un film du CSV."""
    titre = input("Titre à supprimer : ").lower()
    
    # Lecture de tous les films
    with open(FICHIER, 'r') as f:
        lecture = csv.DictReader(f)
        liste_films = list(lecture)
    
    # On garde tous les films sauf celui à supprimer
    films_gardes = []
    for film in liste_films:
        if film['Titre du film'].lower() != titre:
            films_gardes.append(film)
    
    # Réécriture complète du fichier sans le film supprimé
    with open(FICHIER, 'w', newline='') as f:
        ecriture = csv.DictWriter(f, fieldnames=COLONNES)
        ecriture.writeheader()
        ecriture.writerows(films_gardes)
 
 
def marque_film_si_deja_vu():
    """Passe le champ 'Déjà vu' à 'oui' pour le film donné."""
    titre = input("Titre du film : ").lower()
    
    # Lecture de tous les films
    with open(FICHIER, 'r') as f:
        lecture = csv.DictReader(f)
        liste_films = list(lecture)
    
    # Modification en mémoire du film concerné
    for film in liste_films:
        if film['Titre du film'].lower() == titre:
            film['Déjà vu'] = 'oui'
    
    # Réécriture du fichier avec la modification
    with open(FICHIER, 'w', newline='') as f:
        ecriture = csv.DictWriter(f, fieldnames=COLONNES)
        ecriture.writeheader()
        ecriture.writerows(liste_films)
  

# EXPORT JSON ET STATISTIQUES
 
def exporter_json():
    """Exporte la liste complète des films du CSV vers movies.json."""
    with open(FICHIER, 'r') as f:
        lecture = csv.DictReader(f)
        liste_films = list(lecture)
        
    with open(MOVIES_JSON, 'w') as f:
        json.dump(liste_films, f, indent=4)
 
def calculer_stats(liste_films):
    """Calcule et retourne un dictionnaire de statistiques à partir de la liste de films."""
    
    total = len(liste_films)
    
    # Comptage des films vus / non vus
    vus = 0
    non_vus = 0
    for film in liste_films:
        if film['Déjà vu'] == 'oui':
            vus += 1
        else:
            non_vus += 1
    
    # Comptage du nombre de films par genre
    genres = {}
    for film in liste_films:
        genre = film['Genre du film']
        if genre in genres:
            genres[genre] += 1
        else:
            genres[genre] = 1
            
    return {
        'Total': total,
        'Vus': vus,
        'Non vus': non_vus,
        'Genres': genres
    }
 
 
def creer_stats_json():
    """Lit le CSV, calcule les stats et les sauvegarde dans stats.json."""
    with open(FICHIER, 'r') as f:
        lecture = csv.DictReader(f)
        liste_films = list(lecture)
 
    stats = calculer_stats(liste_films)
    
    with open(STATS_JSON, 'w') as f:
        json.dump(stats, f, indent=4)
 
 
def afficher_stats():
    """Lit stats.json et affiche les statistiques."""
    with open(STATS_JSON, 'r') as f:
        stats = json.load(f)
    
    print(f"\nTotal de films : {stats['Total']}")
    print(f"Films vus : {stats['Vus']}")
    print(f"Films non vus : {stats['Non vus']}")
    print(f"Genres : ")
    for genre, nb in stats['Genres'].items():
        print(f"  - {genre} : {nb}")
 
 
# MENU PRINCIPAL

def menu():
    """Affiche le menu et gère les choix utilisateur."""
    
    creer_fichier_si_absent()
    
    while True:
        print("\n=== Gestionnaire de films ===\n")
        print("[1]  Ajouter un film")
        print("[2]  Lister les films")
        print("[3]  Recherche un film")
        print("[4]  Supprimer un film")
        print("[5]  Marquer comme vu")
        print("[6]  Afficher les statistiques")
        print("[7]  Quitter")
        
        # Pour une saisie non numérique
        try:
            choix = int(input("\nVotre choix : "))
        except ValueError:
            print("Veuillez saisir un chiffre.")
            continue
        
        if choix == 1:
            add_film()
            mettre_a_jour_stats()
        elif choix == 2:
            liste_film()
        elif choix == 3:
            recherche_film()
        elif choix == 4:
            supprimer_film()
            mettre_a_jour_stats()
        elif choix == 5:
            marque_film_si_deja_vu()
            mettre_a_jour_stats()
        elif choix == 6:
            afficher_stats()
        elif choix == 7:
            exit()
        else:
            print("choix incorrecte. Veuillez resaisir votre choix.")
