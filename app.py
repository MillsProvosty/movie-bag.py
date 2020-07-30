from flask import Flask, jsonify

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


if __name__ == '__main__':
    app.run()
