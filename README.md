# MachineLearning_2
Projet de ML

#### Projet de Recommandation de Films Basé sur le Filtrage Collaboratif

# Description
Ce projet implémente un système de recommandation de films en utilisant le filtrage collaboratif basé sur les items (films). Le système utilise des informations telles que le genre, la durée, la note IMDb et les recettes pour calculer des similarités entre films et proposer des recommandations personnalisées.

# Fonctionnalités
Calcul de similarité entre films : Utilise la similarité cosinus pour mesurer la ressemblance entre les films.
Génération de recommandations : Propose les films les plus similaires en fonction d'un film de référence.
Analyse exploratoire des données (EDA) : Inclut des visualisations pour mieux comprendre la répartition des genres, des notes, des durées et des budgets.

## Installation
Cloner le dépôt GitHub : git clone https://github.com/...

## Installer les dépendances :
Assurez-vous d'avoir Python installé (version 3.6 ou supérieure).
Installez les packages requis :
pip install pandas scikit-learn matplotlib

## Lancer le Notebook Jupyter :

Ouvrez le notebook Jupyter pour explorer le code et les visualisations : jupyter notebook

# Utilisation

## Calcul de la Matrice de Similarité :
Assurez-vous d'avoir exécuté la cellule de calcul de la matrice de similarité dans le notebook.
Exemple d'Appel de la Fonction de Recommandation :
Utilisez la fonction get_recommendations() pour obtenir des recommandations de films :
film_reference = "Avengers: Endgame"
recommendations = get_recommendations(film_reference, movie_data_encoded, similarity_matrix)
print("Films recommandés : ", recommendations)

La fonction retourne une liste de films similaires au film de référence donné.

# Structure des Dossiers
├── Projet_Perso/                  # Dossier
├── data/                          # Dossier pour le dataset
├── notebook/                      # Jupyter Notebook avec le code principal
├── README.md                      # Documentation du projet
└── requirements.txt               # Fichier des dépendances (optionnel)

# Exemple de Résultats
Pour le film de référence "Avengers: Endgame", les recommandations peuvent inclure des films avec des genres et des notes similaires.


