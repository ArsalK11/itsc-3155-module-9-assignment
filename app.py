from flask import Flask, render_template, request

app = Flask(__name__)

movies = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        movie = request.form['movie']
        rating = request.form['rating']
        if not rating.isdigit() or int(rating) < 1 or int(rating) > 10:
            message = 'Rating must be an integer between 1 and 10.'
        else:
            movie_rating = (movie, int(rating))
            if movie_rating not in movies:
                movies.append(movie_rating)
                message = f'{movie} has been added to the list of movies with a rating of {rating}.'
            else:
                message = f'{movie} with a rating of {rating} is already in the list of movies.'
        return render_template('index.html', movies=movies, message=message)
    else:
        return render_template('index.html', movies=movies)

@app.route('/movies')
def list_all_movies():
    return render_template('list_all_movies.html', list_movies_active=True, movies=movies)

if __name__ == '__main__':
    app.run(debug=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
