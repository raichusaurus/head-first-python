from flask import Flask, render_template, request, redirect
from vowels import search_for_letters

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search_for_letters(phrase, letters))

    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search for letters on the web!')


if __name__ == '__main__':
    app.run()
