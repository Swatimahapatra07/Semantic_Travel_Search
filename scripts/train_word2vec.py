import pandas as pd
from gensim.models import Word2Vec

# 1. Load the processed dataset
df = pd.read_csv("data/processed_travel_reviews.csv")

# 2. Convert reviews into lists of words
sentences = df["Clean_Review"].apply(lambda x: x.split()).tolist()

# 3. Train the Word2Vec model
model = Word2Vec(
    sentences=sentences,
    vector_size=100,
    window=5,
    min_count=2,
    workers=4,
    sg=1
)

# 4. Save the trained model
model.save("models/travel_word2vec.model")

print("Word2Vec model trained successfully!")
print("Model saved at: models/travel_word2vec.model")