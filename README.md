# 🌄 Semantic Travel Search

A Word2Vec-based semantic search system that recommends travel destinations based on the meaning of a user's travel requirement and user reviews of mountainous regions, nature reserves, and natural attractions.

Instead of requiring an exact destination name, the system understands natural-language requirements such as:

> peaceful mountain with greenery

and returns destinations whose reviews have semantically similar content.

---

## 📌 Project Overview

### Problem Statement

**Train a Word2Vec model to find semantically similar travel destinations based on user reviews of mountainous regions and nature reserves.**

Traditional keyword-based search requires users to enter exact keywords or destination names. This project uses Natural Language Processing (NLP) and Word2Vec embeddings to understand relationships between words and recommend destinations based on semantic similarity.

### Example

User enters:

```text
peaceful mountain with greenery
```

The system converts the query into a vector representation and compares it with vectors generated for travel destinations.

The system then returns the most semantically similar destinations.

---

## 🎯 Objectives

1. Collect and prepare travel review data.
2. Filter the dataset for relevant nature, mountain, hill, trekking, and wildlife/nature-reserve destinations.
3. Clean and preprocess user reviews.
4. Tokenize the reviews.
5. Train a Word2Vec model using the processed reviews.
6. Generate vector representations for travel destinations.
7. Convert a user's natural-language travel requirement into a vector.
8. Calculate semantic similarity between the query and destinations.
9. Return the top matching destinations.
10. Provide a web-based interface for users.
11. Expose the semantic-search functionality through a FastAPI REST API.

---

## 🧠 Technologies Used

### Programming Language
- Python 3.11

### Machine Learning / NLP
- Word2Vec
- Gensim
- NumPy
- Scikit-learn

### Data Processing
- Pandas
- Regular Expressions

### Backend
- FastAPI
- Uvicorn
- Pydantic

### Frontend
- HTML
- CSS
- JavaScript

### Development Tools
- VS Code
- PowerShell
- Git
- GitHub

---

## 🏗️ System Architecture

```text
                    USER
                      │
                      ▼
             ┌─────────────────┐
             │    Frontend     │
             │ HTML/CSS/JS     │
             └────────┬────────┘
                      │
                      │ Travel Query
                      ▼
             ┌─────────────────┐
             │     FastAPI     │
             │     Backend     │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Text Processing │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │    Word2Vec     │
             │      Model      │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Destination     │
             │    Vectors      │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Cosine          │
             │ Similarity      │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │   Top-N Travel  │
             │   Destinations  │
             └────────┬────────┘
                      │
                      ▼
                    USER
```

---

## 📂 Project Structure

```text
Semantic_Travel_Search/
│
├── backend/
│   └── main.py
│
├── data/
│   ├── final_mountain_nature_reviews.csv
│   └── processed_travel_reviews.csv
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
│   └── travel_word2vec.model
│
├── notebooks/
│
├── scripts/
│   ├── eda.py
│   ├── preprocess.py
│   ├── tokenize.py
│   ├── train_word2vec.py
│   ├── test_word2vec.py
│   └── semantic_search.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The project uses travel review data containing destination information and user reviews.

The final project dataset contains:

| Column | Description |
|---|---|
| `Destination` | Name of the travel destination |
| `State` | State/region where the destination is located |
| `Category` | Destination category |
| `Review` | User review text |

The dataset is filtered to focus on destinations relevant to the project, including:

- Nature
- Wildlife/Nature Reserve
- Mountain/Hill/Trekking

### Dataset statistics

The processed dataset used during development contains approximately:

- **14,521 reviews**
- **74 destinations**
- **9,081 Nature reviews**
- **3,585 Wildlife/Nature Reserve reviews**
- **1,855 Mountain/Hill/Trekking reviews**

After duplicate removal, approximately **14,519 reviews** are used for subsequent processing.

---

## 🔄 Data Processing Pipeline

```text
Raw Dataset
     │
     ▼
Filter Relevant Destinations
     │
     ▼
Remove Missing Values
     │
     ▼
Remove Duplicate Reviews
     │
     ▼
Clean Review Text
     │
     ▼
Tokenization
     │
     ▼
Word2Vec Training
```

---

## 🧹 Text Preprocessing

The review text is cleaned before training.

The preprocessing includes:

1. Converting text to lowercase.
2. Removing unnecessary characters.
3. Removing extra spaces.
4. Tokenizing the reviews.
5. Preparing tokenized sentences for Word2Vec.

Example:

Original review:

```text
The lake is very beautiful and surrounded by green mountains!
```

Processed review:

```text
lake beautiful surrounded green mountains
```

Tokenized review:

```python
[
    "lake",
    "beautiful",
    "surrounded",
    "green",
    "mountains"
]
```

---

## 🤖 Word2Vec Model

The project uses **Word2Vec** to learn semantic relationships between words from the travel reviews.

For example, after training, words related to `mountain` may include terms such as:

```text
panoramic
viewpoint
capped
clad
```

Similarly, `forest` may be associated with terms such as:

```text
jungle
dense
bamboo
reserve
```

The model learns these relationships from the context in the travel reviews.

---

## 📍 Destination Vector Generation

A destination can have many reviews.

Each review is converted into a vector using Word2Vec. The vectors of all reviews belonging to a destination are then averaged.

```text
Review 1 → Vector
Review 2 → Vector
Review 3 → Vector
Review 4 → Vector
       ↓
Average vectors
       ↓
Destination Vector
```

This produces one vector representing each destination.

The project currently generates vectors for approximately **74 destinations**.

---

## 🔎 Semantic Search

When the user enters a query such as:

```text
peaceful mountain with greenery
```

the query is converted into a vector using the trained Word2Vec model.

The system then calculates the similarity between the query and destination vectors using **Cosine Similarity**.

The destinations are sorted by similarity score and the top results are returned.

---

## 🌐 FastAPI Backend

The backend provides a REST API for semantic search.

### Start the backend

From the project root:

```powershell
.\venv\Scripts\activate
uvicorn backend.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

### API documentation

FastAPI provides interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

---

## 🔌 API Endpoint

### POST `/search`

The endpoint accepts a travel requirement and the number of results.

Request:

```json
{
    "query": "peaceful mountain with greenery",
    "top_n": 5
}
```

Example response:

```json
{
    "success": true,
    "query": "peaceful mountain with greenery",
    "results": [
        {
            "destination": "Khajjiar Lake",
            "state": "Himachal Pradesh",
            "category": "Nature",
            "similarity": 0.886
        },
        {
            "destination": "Betaab Valley",
            "state": "Jammu & Kashmir",
            "category": "Mountain/Hill/Trekking",
            "similarity": 0.8708
        }
    ]
}
```

---

## 💻 Frontend

The frontend is implemented using:

- HTML
- CSS
- JavaScript

The user enters a natural-language travel requirement.

Example:

```text
peaceful place with mountains and waterfalls
```

The JavaScript frontend sends the request to:

```text
POST /search
```

The returned destinations are displayed as result cards.

Each result displays:

- Destination
- State
- Category
- Similarity Score

---

## ▶️ How to Run the Complete Project

### Step 1 — Open the project

```powershell
cd "C:\Users\swati\OneDrive\Desktop\Semantic_Travel_Search"
```

### Step 2 — Activate virtual environment

```powershell
.\venv\Scripts\activate
```

### Step 3 — Start backend

```powershell
uvicorn backend.main:app --reload
```

Keep this terminal running.

### Step 4 — Open another terminal

Navigate to the frontend:

```powershell
cd "C:\Users\swati\OneDrive\Desktop\Semantic_Travel_Search\frontend"
```

Open the website:

```powershell
start index.html
```

### Step 5 — Search

Enter a query such as:

```text
peaceful mountain surrounded by greenery
```

Click **Search**.

---

## 🧪 Example Queries

```text
peaceful mountain surrounded by greenery
```

```text
snow covered mountains and scenic views
```

```text
quiet place for trekking and nature
```

```text
peaceful lake surrounded by mountains
```

```text
dense forest with wildlife
```

```text
wildlife sanctuary with animals and forest
```

```text
beautiful natural place with greenery
```

---

## 🧪 Model Testing

The Word2Vec model can be tested independently:

```powershell
python scripts/test_word2vec.py
```

This checks semantic relationships between words such as:

```text
mountain
nature
lake
forest
beach
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Semantic_Travel_Search.git
```

Enter the project:

```bash
cd Semantic_Travel_Search
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Machine Learning Workflow

```text
Travel Review Dataset
        ↓
Data Filtering
        ↓
Exploratory Data Analysis
        ↓
Text Cleaning
        ↓
Tokenization
        ↓
Word2Vec Training
        ↓
Word Embeddings
        ↓
Destination Embeddings
        ↓
User Query Embedding
        ↓
Cosine Similarity
        ↓
Rank Destinations
        ↓
Top-N Recommendations
```

---

## 🔬 Why Word2Vec?

Word2Vec learns relationships between words based on their surrounding context.

Travel reviews containing words such as:

```text
mountain
hill
trekking
valley
snow
scenic
```

allow the model to learn relationships between these concepts.

Therefore, a query does not necessarily have to contain the exact destination name to retrieve relevant destinations.

---

## ⚙️ Key Features

- Natural-language travel search
- Semantic rather than exact keyword matching
- Word2Vec-based NLP
- Destination-level vector representations
- Cosine similarity ranking
- Top-N destination recommendations
- FastAPI REST API
- Interactive frontend
- Filtered travel review dataset
- Interactive API documentation through FastAPI

---

## 🚀 Future Enhancements

1. Transformer-based embeddings such as Sentence-BERT.
2. Destination images.
3. User ratings.
4. Budget-based filtering.
5. Weather information.
6. Distance-based filtering.
7. Personalized recommendations.
8. Location-based recommendations.
9. Hybrid keyword + semantic search.
10. Deployment using Docker and cloud services.
11. Database integration.
12. Advanced recommendation ranking.

---

## 👨‍💻 Project Goal

The goal of this project is to demonstrate how **Natural Language Processing, Word Embeddings, Semantic Similarity, REST APIs, and Web Development** can be combined to create an intelligent travel-search application.

---

## 📄 License

This project is intended for educational and academic purposes.
