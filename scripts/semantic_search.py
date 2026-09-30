import pandas as pd
import numpy as np
import re

from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity


# ==================================================
# 1. LOAD DATASET
# ==================================================

df = pd.read_csv("data/processed_travel_reviews.csv")

print("Dataset loaded successfully!")
print("Number of reviews:", len(df))
print("Number of destinations:", df["Destination"].nunique())


# ==================================================
# 2. LOAD WORD2VEC MODEL
# ==================================================

model = Word2Vec.load("models/travel_word2vec.model")

print("Word2Vec model loaded successfully!")


# ==================================================
# 3. CLEAN TEXT
# ==================================================

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


# ==================================================
# 4. CONVERT TEXT INTO VECTOR
# ==================================================

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


# ==================================================
# 5. CREATE DESTINATION VECTORS
# ==================================================

destination_vectors = {}

print("\nCreating destination vectors...")

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

        destination_vector = np.mean(
            vectors,
            axis=0
        )

        destination_vectors[destination] = destination_vector


print(
    "Destination vectors created:",
    len(destination_vectors)
)


# ==================================================
# 6. SEMANTIC SEARCH
# ==================================================

def semantic_search(query, top_n=5):

    query_vector = get_text_vector(query)

    if query_vector is None:

        print("\nNo words from your query were found.")
        print("Please try another travel description.")

        return

    scores = []

    for destination, destination_vector in destination_vectors.items():

        similarity = cosine_similarity(
            [query_vector],
            [destination_vector]
        )[0][0]

        scores.append(
            (destination, similarity)
        )

    # Sort from highest to lowest similarity
    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\n======================================")
    print("       SEMANTIC TRAVEL SEARCH")
    print("======================================")

    print("\nYour query:")
    print(query)

    print("\nTop", top_n, "matching destinations:\n")

    # Display results
    for rank, (destination, score) in enumerate(
        scores[:top_n],
        start=1
    ):

        # Get information about destination
        destination_info = df[
            df["Destination"] == destination
        ].iloc[0]

        state = destination_info["State"]
        category = destination_info["Category"]

        print("--------------------------------------")

        print(f"{rank}. {destination}")

        print(f"   State: {state}")

        print(f"   Category: {category}")

        print(
            f"   Similarity: {score:.4f}"
        )

    print("--------------------------------------")


# ==================================================
# 7. USER INPUT
# ==================================================

query = input(
    "\nEnter your travel requirement: "
)


# ==================================================
# 8. RUN SEARCH
# ==================================================

semantic_search(
    query,
    top_n=5
)