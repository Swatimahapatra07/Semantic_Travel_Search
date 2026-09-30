import pandas as pd

# Load the processed dataset
df = pd.read_csv("data/processed_travel_reviews.csv")

# Convert each review into a list of words
sentences = df["Clean_Review"].apply(lambda x: x.split()).tolist()

# Print first 5 tokenized reviews
print("First 5 tokenized reviews:\n")

for sentence in sentences[:5]:
    print(sentence)

print("\nTotal reviews:", len(sentences))