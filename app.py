from flask import Flask, request, jsonify
import pandas as pd
import pickle

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# with open("model1.pkl", "rb") as f:
#     movies, cosine_sim = pickle.load(f)

with open("model1.pkl", "rb") as f:
    movies_df,  cosine_sim = pickle.load(f)


#creating a reccomend function.
movies = movies_df.reset_index()
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# def recommend_movies(movie_name, cosine_sim=cosine_sim):
#     if movie_name not in indices.index:
#         return ["Movie not found"]
    
#     idx = indices[movie_name]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
#     movie_indices = [i[0] for i in sim_scores]
    
#     return movies['title'].iloc[movie_indices].tolist()


def recommend_movies(movie_name, num_recommendations=5):
    if movie_name not in movies_df["title"].values:
        return []

    # idx = movies_df[movies_df["title"] == movie_name].index[0]

    movie_name = movie_name.strip().lower()
    movies_df["title_lower"] = movies_df["title"].str.strip().str.lower()
    idx= movies_df[movies_df["title_lower"] == movie_name].index[0]



    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]

    recommended_movie_ids = [movies_df.iloc[i[0]]["movieId"] for i in sim_scores]

    recommended_movies = movies_df[movies_df["movieId"].isin(recommended_movie_ids)][["title", "genres"]]

    if recommended_movies.empty:
        recommended_movies = movies_df.sample(5)  # Return 5 random movies

    
    
    return recommended_movies.to_dict(orient="records")





@app.route('/movies', methods=['GET'])
def get_movies():
    movies_list = movies.to_dict(orient='records')  
    return jsonify(movies_list)
    

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_name = request.args.get('movie', '')
    recommendations = recommend_movies(movie_name)
    return jsonify({"recommended_movies": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
