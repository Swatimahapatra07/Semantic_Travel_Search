import pandas as pd

# Load the dataset
df = pd.read_csv("data/final_mountain_nature_reviews.csv")

# Show first 5 rows
print(df.head())

# Show number of rows and columns
print("Dataset shape:", df.shape)

# Show column names
print("Columns:")
print(df.columns)

# Number of reviews
print("Number of reviews:", len(df))

# Number of unique destinations
print("Number of destinations:", df["Destination"].nunique())

# Show categories
print("\nCategories:")
print(df["Category"].value_counts())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate reviews
print("\nDuplicate reviews:")
print(df["Review"].duplicated().sum())