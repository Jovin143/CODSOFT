# Project: MOVIE RECOMMENDATION SYSTEM
# Created by: [NIBSHAN JOVIN JOSEPH]
# Date: [27-07-2025]

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.DataFrame({
    'movie_id': [101, 102, 103, 104, 105],
    'title': ['The Room', 'Cats', 'Movie 43', 'Dragonball Evolution', 'Birdemic'],
    'genre': ['Drama', 'Musical', 'Comedy', 'Action', 'Horror']
})

ratings = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4],
    'movie_id': [101, 102, 103, 102, 104, 103, 105, 105],
    'rating': [3, 2, 1, 2, 2, 1, 1, 2]
})

encoder = OneHotEncoder(sparse_output=False)  
genre_encoded = encoder.fit_transform(movies[['genre']])

movie_similarity = cosine_similarity(genre_encoded)

def recommend_similar_movies(movie_name):
    if movie_name not in movies['title'].values:
        return ["Sorry, movie not found."]
    
    movie_idx = movies[movies['title'] == movie_name].index[0]
    similarity_scores = list(enumerate(movie_similarity[movie_idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:4]
    recommended_titles = [movies.iloc[i[0]]['title'] for i in similarity_scores]
    return recommended_titles

user_movie_matrix = ratings.pivot(index='user_id', columns='movie_id', values='rating').fillna(0)

user_similarity = cosine_similarity(user_movie_matrix)
user_sim_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

def recommend_movies_by_user(user_id):
    if user_id not in user_sim_df.index:
        return ["User ID not found."]
    
    similar_users = user_sim_df[user_id].drop(user_id)
    most_similar_user = similar_users.idxmax()
    
    movies_seen = ratings[ratings['user_id'] == user_id]['movie_id'].tolist()
    candidate_movies = ratings[
        (ratings['user_id'] == most_similar_user) & (~ratings['movie_id'].isin(movies_seen))
    ]
    top_candidates = candidate_movies.sort_values(by='rating', ascending=False).head(3)
    recommended_titles = movies[movies['movie_id'].isin(top_candidates['movie_id'])]['title'].tolist()
    
    if not recommended_titles:
        return ["No new recommendations found based on similar users."]
    return recommended_titles

def show_all_movies():
    print("Here are all the movies in our database:")
    for _, row in movies.iterrows():
        print(f"- {row['title']} ({row['genre']})")
2

def main():
    print("Welcome to the Movie Recommender!")
    print("Choose an option:")
    print("1. Get movie recommendations similar to a movie you like.")
    print("2. Get movie recommendations based on your user ID.")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        show_all_movies()
        movie_choice = input("Type the exact movie name from above: ")
        recommendations = recommend_similar_movies(movie_choice)
        print(f"\nMovies similar to '{movie_choice}' are:")
        for rec in recommendations:
            print("-", rec)
    
    elif choice == '2':
        try:
            user_id = int(input("Enter your user ID (1 to 4): "))
            recommendations = recommend_movies_by_user(user_id)
            print(f"\nMovies recommended for user {user_id}:")
            for rec in recommendations:
                print("-", rec)
        except ValueError:
            print("Invalid input. Please enter a numeric user ID.")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
