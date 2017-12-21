from flask import Flask, render_template
from vowels import search_for_letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search')
def search_for() -> str:
    return str(search_for_letters('life, the universe, and everything!', 'eiru'))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search for letters on the web!')


app.run()