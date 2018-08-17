"""Flask web application for 'What Can I Run?'."""


from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from regex import *
from models import *
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Katm2803@localhost:3306/project'
db = SQLAlchemy(app)


#def performance_rank(user_cpu, user_gpu, ):


@app.route("/")
@app.route("/input")
def input():
    """Returns the home input page containing the form to input the user's hardware information."""

    return render_template('input.html', cpus=db.session.query(cpubenchmarks).all(),
                           gpus=db.session.query(gpubenchmarks).all(), tags=db.session.query(tags).all())


@app.route("/results", methods=['POST'])
def results():
    """Gets input data from the form and formulates the game row results by querying databases using received data.
    Performs additional comparisons to OS and RAM and matches games with the provided tag search.
    Orders resulting rows based upon ordering option selected by user.
    Returns the results containing the final list of matching results.
    """

    cpu = db.session.query(cpubenchmarks).get(request.form['CPU'])
    gpu = db.session.query(gpubenchmarks).get(request.form['GPU'])
    #TODO if cpu or gpu are not selected properly, return page saying input correctly
    ram = int(request.form['ram_num'])
    os = int(request.form['os_version'])
    order = request.form['order_by']
    tag = request.form['tag_search']
    if order == 'performance':
        rows = db.session.query(game_requirements).filter(game_requirements.min_cpu_score < cpu.benchmark_score,
                                        game_requirements.min_gpu_score < gpu.benchmark_score).all()
    else:
        rows = db.session.query(game_requirements).filter(game_requirements.min_cpu_score < cpu.benchmark_score,
                                          game_requirements.min_gpu_score < gpu.benchmark_score).order_by\
                                          (desc(order)).all()
    rows = os_ram_comparison(rows, os, ram)
    if tag != '':
        url_tag = re.sub(r' ', r'+', tag.strip())  # standardise tags to include '+' for whitespace for api call
        print(url_tag)
        url = 'http://steamspy.com/api.php?request=tag&tag=' + url_tag
        tag_games = requests.get(url).json()

        if db.session.query(tags).filter(tags.tag == tag).all():  # check if given tag exists in db table
            rows = tag_search(tag_games, rows)
            #return redirect(url_for('input'))
        #TODO invalid input page that redirects after timer
        #THINK don't redirect just tret incorrect tag as empty tag
    print(len(rows))
    store_url = 'https://store.steampowered.com/app/'
    return render_template('results.html', url=store_url, rows=rows)


def os_ram_comparison(rows, os, ram):
    """Compares the user's OS version and RAM to each game in the given list of rows.
    Returns a new list containing all games with OS and RAM lower than the user.
    """

    os_ram_rows = []
    for row in rows:
        if (os_regex(row.min_specs) is None or os >= os_regex(row.min_specs)) and \
                (ram_regex(row.min_specs) is None or ram >= ram_regex(row.min_specs)):
            os_ram_rows.append(row)
    return os_ram_rows
#TODO write test


def tag_search(tag_games, rows):
    """Matches the appids of games provided in rows to the appids of games in tag_games.
    tag_games is a list of all games that have the given steam tag.
    Returns a new list of all game rows that are in both lists.
    """

    tag_match_rows = []
    for row in rows:
        if str(row.appid) in tag_games:
            tag_match_rows.append(row)
    return tag_match_rows
#TODO write test


if __name__ == '__main__':
    app.run(debug=True)