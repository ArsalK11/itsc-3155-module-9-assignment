from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()

movie_dict = {}
key_list = {}

@app.get('/')
def index():
    return render_template('index.html')


@app.route('/movies')
def list_all_movies():
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.route('/movies', methods = ['POST'])
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    if request.method == 'POST':
            title = request.form['title']
            direc = request.form['director']
            rate = request.form['rating']
            key_list = movie_dict.keys()
            movie_dict.update({title: [direc, rate] })
    return render_template('list_all_movies.html', key_list = key_list, movie_dict = movie_dict)


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    if request.method == 'POST':
        try:
            userResponse = (request.form.get('movie'))
            if userResponse in key_list:
                temp = movie_dict[userResponse]

            else:
                temp = str(userResponse) + ' is odd'
        except Exception:
            temp = 'Movie is not within the List'
        return render_template('search_movies.html', temp2 = temp)

if __name__ == "__main__":
    app.run(debug=True)
