
# import pandas as pd
# import re
# import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# print("starting here")

# import pandas as pd

# # Load datasets
# movies_df = pd.read_csv("datasets/movie.csv")
# ratings_df = pd.read_csv("datasets/rating.csv")
# tags_df = pd.read_csv("datasets/tag.csv")
# links_df = pd.read_csv("datasets/link.csv")
# genome_scores_df = pd.read_csv("datasets/genome_scores.csv")
# genome_tags_df = pd.read_csv("datasets/genome_tags.csv")

# # Preview datasets
# print(movies_df.head())
# print(ratings_df.head())
# print(tags_df.head())
# print(links_df.head())
# print(genome_scores_df.head())
# print(genome_tags_df.head())


# # preprocessing
# movies = movies_df[['movieId', 'title', 'genres']]
# movies.dropna(inplace=True)  # Remove missing values
# print("this done")
# # Function to remove the year (or any text within parentheses)
# def remove_year(title):
#     return re.sub(r'\(.*\)', '', title).strip()  # Removes everything inside parentheses and strips leading/trailing spaces

# # Apply the function to the 'title' column
# movies['title'] = movies['title'].apply(remove_year)
# print("then this")
# # Convert genres into a list format
# movies['genres'] = movies['genres'].apply(lambda x: x.replace('|', ' '))

# # 🔹 Merge tags data for better recommendations
# tags_df = tags_df.groupby("movieId")["tag"].apply(lambda x: " ".join(x.dropna().astype(str))).reset_index()
# movies_df = pd.merge(movies_df, tags_df, on="movieId", how="left")

# # 🔹 Use TF-IDF Vectorizer on movie genres + tags
# movies_df["combined_features"] = movies_df["genres"] + " " + movies_df["tag"].fillna("")
# vectorizer = TfidfVectorizer(stop_words="english")
# tfidf_matrix = vectorizer.fit_transform(movies_df["combined_features"])

# # 🔹 Compute similarity
# cosine_sim = cosine_similarity(tfidf_matrix)

# # #tf-idf vectorization
# # this was only using genre. now we are addignd oher as well.

# # tfidf = TfidfVectorizer(stop_words='english')
# # tfidf_matrix = tfidf.fit_transform(movies['genres'])
# # print("abcdfskldhfesjkglefvksen")

# # cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# print("Saving model...")
# with open("model1.pkl", "wb") as f:
#     pickle.dump((movies, cosine_sim), f)

# print("Model saved successfully as model.pkl")



import pandas as pd
import re
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Starting Movie Recommendation Model...")

# Load datasets
movies_df = pd.read_csv("datasets/movie.csv")
ratings_df = pd.read_csv("datasets/rating.csv")
tags_df = pd.read_csv("datasets/tag.csv")
links_df = pd.read_csv("datasets/link.csv")
genome_scores_df = pd.read_csv("datasets/genome_scores.csv")
genome_tags_df = pd.read_csv("datasets/genome_tags.csv")

# Remove missing values
movies = movies_df[['movieId', 'title', 'genres']].dropna()

# Function to remove the year from title
def remove_year(title):
    return re.sub(r'\(.*\)', '', title).strip()

movies['title'] = movies['title'].apply(remove_year)

# Convert genres into a space-separated string
movies['genres'] = movies['genres'].apply(lambda x: x.replace('|', ' '))

# 🔹 Merge tags data
tags_df = tags_df.groupby("movieId")["tag"].apply(lambda x: " ".join(x.dropna().astype(str))).reset_index()
movies_df = movies_df[['movieId', 'title', 'genres']].copy()
movies_df = pd.merge(movies_df, tags_df, on="movieId", how="left")
movies_df["tag"] = movies_df["tag"].fillna("")  # Ensure no NaN values

# 🔹 Combine features for vectorization
movies["combined_features"] = movies["genres"] + " " + movies_df["tag"]

# 🔹 TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(movies["combined_features"])

# 🔹 Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix)

print(f"Cosine Similarity Matrix Shape: {cosine_sim.shape}")

# 🔹 Save model
print("Saving model...")
with open("model1.pkl", "wb") as f:
    pickle.dump((movies[["movieId", "title", "genres"]], cosine_sim), f)
print("Model saved successfully as model1.pkl")
