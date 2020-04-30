from flask import Flask, render_template, request, redirect, url_for
from utils import *
import json
from generate import get_generated_song

app = Flask(__name__)

genres = get_genres()

@app.route("/")
def index():
    errs = json.loads(request.args.get('err_data')) if request.args.get('err_data') else None
    return render_template('index.html', genres=genres, errs=errs)


@app.route("/process_generate", methods=['GET'])
def process_generate():
    errs, genre, rhyme_freq, max_length, num_lines = validate_input(request)
    if errs != '[]':
        return redirect(url_for("index", err_data=errs))
    else:
        song = get_generated_song(genre, num_lines, max_length, rhyme_freq)
        return render_template("display.html", song=song)

if __name__ == "__main__":
    app.run()
