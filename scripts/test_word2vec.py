from gensim.models import Word2Vec

# Load the trained Word2Vec model
model = Word2Vec.load("models/travel_word2vec.model")

# Words we want to test
words = ["mountain", "nature", "lake", "forest", "beach"]

for word in words:

    print("\n--------------------------------")
    print("Similar words to:", word)
    print("--------------------------------")

    if word in model.wv:

        results = model.wv.most_similar(word, topn=5)

        for similar_word, score in results:
            print(similar_word, "->", round(score, 4))

    else:
        print("Word not found in the model.")