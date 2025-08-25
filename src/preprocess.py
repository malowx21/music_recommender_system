"""Import """
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('punkt_tab', quiet=True)
except:
    print("Vérification des ressources NLTK.")

# Defining the stopword on the english language
stop = set(stopwords.words("english"))
# Lemmatizer
lemmatizer=WordNetLemmatizer()

def cleaning_lyrics(lyrics):
    """cleaning function"""
    final_lyrics=[]
    lyrics= str(lyrics).lower()
    lyrics=re.sub(r"[^a-z\s]","",lyrics)
    lyrics_token= word_tokenize(lyrics)
    for token in lyrics_token:
        if token not in stop:
            final_lyrics.append(lemmatizer.lemmatize(token))
    return " ".join(final_lyrics)


def apply_cleaning(df):
    """preprocess"""
    df['Clean_lyrics']=df['Lyrics'].apply(cleaning_lyrics)
    return df
