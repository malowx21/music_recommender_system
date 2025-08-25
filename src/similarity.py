"""Import"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def vect_tf_idf(df):
    """transform lyrics into a vectors TF-IDF  """
    vect= TfidfVectorizer(max_features=6000)
    vect_transf= vect.fit_transform(df['Clean_lyrics'])
    return vect_transf

def cos_sim(vect):
    """Compute cosine similarity"""
    sim= cosine_similarity(vect)
    return sim

def recommend(df, sim, music_name,n=5):
    """recommend list of n songs"""
    try:
        # take the index of the music in the dataset
        idx= df[df['Title'].str.lower()==music_name.lower()].index[0]
    except IndexError:
        print("Title not in the dataset")    
    list_sim= list(enumerate(sim[idx]))
    list_sim= sorted(list_sim, key=lambda x: x[1], reverse=True)[1:n+1]
    similar_songs= [df.iloc[ind[0]]['Title'] for ind in list_sim]
    return similar_songs
