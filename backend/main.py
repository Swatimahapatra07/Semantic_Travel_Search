from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from gensim.models import Word2Vec
import pandas as pd
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity


# =========================================================
# CREATE FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="Semantic Travel Search API",
    description="Travel destination search using Word2Vec",
    version="1.0"
)


# =========================================================
# CORS CONFIGURATION
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# LOAD DATASET
# =========================================================

df = pd.read_csv("data/processed_travel_reviews.csv")

print("Dataset loaded successfully!")
print("Number of reviews:", len(df))
print("Number of destinations:", df["Destination"].nunique())


# =========================================================
# LOAD WORD2VEC MODEL
# =========================================================

model = Word2Vec.load("models/travel_word2vec.model")

print("Word2Vec model loaded successfully!")


# =========================================================
# TEXT CLEANING FUNCTION
# =========================================================

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


# =========================================================
# CREATE TEXT VECTOR
# =========================================================

def get_text_vector(text):

    text = clean_text(text)

    words = text.split()

    word_vectors = []

    for word in words:

        if word in model.wv:

            word_vectors.append(model.wv[word])

    if len(word_vectors) == 0:

        return None

    return np.mean(word_vectors, axis=0)


# =========================================================
# CREATE DESTINATION VECTORS
# =========================================================

destination_vectors = {}

print("Creating destination vectors...")

for destination in df["Destination"].unique():

    destination_reviews = df[
        df["Destination"] == destination
    ]["Clean_Review"]

    vectors = []

    for review in destination_reviews:

        vector = get_text_vector(review)

        if vector is not None:

            vectors.append(vector)

    if len(vectors) > 0:

        destination_vector = np.mean(vectors, axis=0)

        destination_vectors[destination] = destination_vector


print(
    "Destination vectors created:",
    len(destination_vectors)
)


# =========================================================
# HOME API
# =========================================================

@app.get("/")
def home():

    return {
        "message": "Semantic Travel Search API is running!"
    }


# =========================================================
# SEARCH REQUEST MODEL
# =========================================================

class SearchRequest(BaseModel):

    query: str

    top_n: int = 5


# =========================================================
# SEARCH API
# =========================================================

@app.post("/search")
def search(request: SearchRequest):

    query = request.query

    query_vector = get_text_vector(query)

    # If no words from query exist in Word2Vec vocabulary
    if query_vector is None:

        return {
            "success": False,
            "message": "No words from the query were found.",
            "results": []
        }


    scores = []


    # Compare query with every destination
    for destination, destination_vector in destination_vectors.items():

        similarity = cosine_similarity(
            [query_vector],
            [destination_vector]
        )[0][0]


        destination_info = df[
            df["Destination"] == destination
        ].iloc[0]


        scores.append({

            "destination": destination,

            "state": destination_info["State"],

            "category": destination_info["Category"],

            "similarity": round(
                float(similarity),
                4
            )

        })


    # Sort according to similarity
    scores.sort(
        key=lambda x: x["similarity"],
        reverse=True
    )


    # Return top results
    return {

        "success": True,

        "query": query,

        "results": scores[:request.top_n]

    }