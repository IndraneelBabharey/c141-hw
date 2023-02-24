from flask import Flask,jsonify,request
import csv

all_movies = []
liked_movies = []
not_liked_movies = []
did_not_watch = []

with open("movies.csv",encoding="utf-8")as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

app = Flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data":all_movies[0],
        "status":"success"

    })

@app.route("/liked-movie", methods = ["POST"])  
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/unliked-movie", methods = ["POST"])  
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status" : "success"
    }),201    

@app.route("/did-not-watch", methods = ["POST"])  
def didnot_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status" : "success"
    }),201 

if __name__ == "__main__":
    app.run()