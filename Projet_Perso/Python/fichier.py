# Import des bibliothèques nécessaires pour la manipulation des données, le calcul des similarités et la visualisation
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Charger le dataset contenant les informations sur les films
# Ce fichier doit inclure des colonnes telles que le titre du film, la date de production, le genre, etc.
new_movie_data = pd.read_csv('path/to/movie_statistic_dataset.csv', encoding='ISO-8859-1')


# Convertir la colonne 'production_date' en format datetime pour des analyses basées sur la date
new_movie_data['production_date'] = pd.to_datetime(new_movie_data['production_date'], errors='coerce')

# Appliquer un encodage OneHot sur la colonne des genres pour transformer chaque genre en une colonne binaire
genres_expanded = new_movie_data['genres'].str.get_dummies(sep=',')

# Fusionner les colonnes encodées avec le dataset initial pour obtenir le dataset final prêt pour la similarité
movie_data_encoded = pd.concat([new_movie_data, genres_expanded], axis=1)


# Calculer la matrice de similarité cosinus entre les films en utilisant les caractéristiques sélectionnées
similarity_features = movie_data_encoded.drop(columns=['movie_title', 'production_date', 'genres', 'director_name',
                                                       'director_professions', 'director_birthYear', 'director_deathYear'])
similarity_matrix = cosine_similarity(similarity_features)

# Cette fonction génère les recommandations de films similaires en utilisant la matrice de similarité
def get_recommendations(movie_title, movie_data, similarity_matrix, top_n=5):
    # Trouver l'index du film de référence
    try:
        movie_idx = movie_data[movie_data['movie_title'] == movie_title].index[0]
    except IndexError:
        return f"Le film '{movie_title}' n'existe pas dans le dataset."
    
    # Calculer les scores de similarité et sélectionner les films les plus similaires
    similarity_scores = list(enumerate(similarity_matrix[movie_idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_similar_movies = similarity_scores[1:top_n+1]  # Exclure le film lui-même
    recommended_movies = [movie_data['movie_title'].iloc[i[0]] for i in top_similar_movies]
    
    return recommended_movies
