import pandas as pd
import re

# 1. Load the dataset
df = pd.read_csv("data/final_mountain_nature_reviews.csv")

# 2. Remove duplicate reviews
df = df.drop_duplicates(subset=["Review"])

# 3. Function to clean the review
def clean_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

# 4. Apply cleaning to every review
df["Clean_Review"] = df["Review"].apply(clean_text)

# 5. Remove reviews that became empty
df = df[df["Clean_Review"].str.strip() != ""]

# 6. Save the processed dataset
df.to_csv(
    "data/processed_travel_reviews.csv",
    index=False
)

print("Preprocessing completed!")
print("Number of reviews:", len(df))
print("Saved as: data/processed_travel_reviews.csv")