from flask import Flask
from vowels import search_for_letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search')
def search_for() -> str:
    return str(search_for_letters('life, the universe, and everything!', 'eiru'))


app.run()
