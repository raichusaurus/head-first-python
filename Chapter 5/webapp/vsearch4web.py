from flask import Flask, render_template, request
from vowels import search_for_letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4', methods=['POST'])
def search_for() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search_for_letters(phrase, letters))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search for letters on the web!')


app.run()
