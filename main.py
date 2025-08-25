"""Import"""
import webbrowser
from flask import Flask, render_template,request
from src.load_dataset import df
from src.preprocess import apply_cleaning
from src.similarity import vect_tf_idf, cos_sim, recommend

app= Flask(__name__)
df = apply_cleaning(df)
vect = vect_tf_idf(df)
similarity_matrix = cos_sim(vect)
# title = input("Please entre a song name\n")  # change selon ton dataset
# print("Chansons similaires à", title, ":\n", recommend(df, similarity_matrix, title))
@app.route("/", methods=["GET", "POST"])
def home():
    """ home function"""
    results = []
    if request.method == "POST":
        music_name = request.form.get("title")  # récupère l’input
        if music_name:  # si ce n’est pas vide
            try:
                results = recommend(df, similarity_matrix, music_name, n=5)
            except Exception as e:
                results = [f"Erreur: {str(e)}"]

    return render_template("index.html", results=results)


if __name__ == "__main__":
    url = "http://127.0.0.1:5000"
    webbrowser.open(url)
    app.run(debug=True)
