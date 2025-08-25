## Music Recommender System
This project is a music recommendation system based on song lyrics. It uses basic Natural Language Processing (NLP) techniques to analyze and compare song lyrics to recommend similar tracks.

## Project Structure
```bash
music_recommender_system/
│
├── data/ 
│   └── songs.csv
├── src/ 
│   ├── preprocess.py
│   ├── similarity.py 
│   └── load_dataset.py
├── templates/ 
│   └── index.html
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used
-Python for data processing and recommendation logic

-Pandas for CSV dataset manipulation

-NLTK for NLP (lyrics cleaning, tokenization, lemmatization, stopword removal)

-Scikit-learn for TF-IDF vectorization of lyrics and Cosine similarity calculation

-Flask for creating a simple web interface

-HTML/CSS for the search form web page

## How to Use
Clone the project:

```bash
git clone <repo-url>
cd music_recommender_system
Install dependencies:
```
```bash
pip install -r requirements.txt
Run the application:
```
```bash
python main.py
```
The browser will open automatically and you can enter a song name to see recommendations.

## How It Works
-Lyrics are cleaned (lowercase conversion, special character removal, stopword removal, and lemmatization) in preprocess.py

-Cleaned lyrics are transformed into TF-IDF vectors

-Cosine similarity is calculated between all songs in similarity.py

When a user enters a song name in the web interface, the system returns the 5 most similar songs

## Educational Purpose
This project aims to teach and practice:

-Basic NLP techniques applied to song lyrics

-Using TF-IDF and cosine similarity

-Creating simple web applications with Flask

-Organizing Python projects with src, templates, and data directories

## Notes
-Ensure that entered song names exist exactly in the dataset (case-sensitive and space-sensitive)

-This project can be enhanced by adding features such as:

Recommendations based on artist or genre

Similarity visualization

Improved NLP preprocessing

Error handling for song names not found in dataset
    