from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "name": "The Shawshank Redemption",
        "cast": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
        "name": "The Godfather",
        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
        "genres": ["Crime", "Drama"]
    },
    {
        "name": "The Hobbit",
        "casts": ["Martin Freeman", "Richard Armitage", "Ian McKellen", "PeterJackson"],
        "genres": ["Fantasy", "Drama"]
    }
]


@app.route('/movies')
def return_movies():
    return jsonify(movies)


@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200


@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    get_movie = request.get_data(index)
    movies.__delitem__(get_movie)
    return movies, 200


if __name__ == '__main__':
    app.run()
