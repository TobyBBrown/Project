from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from regex import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Katm2803@localhost:3306/test'
app.config['SQLALCHEMY_BINDS'] = {
    'project' : 'mysql+mysqlconnector://root:Katm2803@localhost:3306/project'}
db = SQLAlchemy(app)


class test(db.Model):
    appid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    min_specs = db.Column(db.Text)
    rec_specs = db.Column(db.Text)


class game_requirements(db.Model):
    __bind_key__ = 'project'
    appid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    min_specs = db.Column(db.Text)
    rec_specs = db.Column(db.Text)
    min_cpu_score = db.Column(db.Integer)
    rec_cpu_score = db.Column(db.Integer)
    min_gpu_score = db.Column(db.Integer)
    rec_gpu_score = db.Column(db.Integer)
    userscore = db.Column(db.Integer)
    price = db.Column(db.Integer)


class cpubenchmarks(db.Model):
    __bind_key__ = 'project'
    cpu_name = db.Column(db.String, primary_key=True)
    benchmark_score = db.Column(db.Integer)


class gpubenchmarks(db.Model):
    __bind_key__ = 'project'
    gpu_name = db.Column(db.String, primary_key=True)
    benchmark_score = db.Column(db.Integer)


store_url = 'https://store.steampowered.com/app/'


@app.route("/input")
def hardware_input():
    return render_template('input.html', cpus=cpubenchmarks.query.all(),
                           gpus=gpubenchmarks.query.all())


@app.route("/hardware_submit", methods=['POST'])
def hardware_submit():
    cpu = cpubenchmarks.query.get(request.form['CPU'])
    gpu = gpubenchmarks.query.get(request.form['GPU'])
    ram = int(request.form['ram_num'])
    os = int(request.form['os_version'])
    rows = game_requirements.query.filter(game_requirements.min_cpu_score < cpu.benchmark_score,
                                          game_requirements.min_gpu_score < gpu.benchmark_score).order_by\
                                          (desc(game_requirements.userscore)).all()
    os_ram_rows = []
    for row in rows:
        if (os_regex(row.min_specs) is None or os >= os_regex(row.min_specs)) and \
                (ram_regex(row.min_specs) is None or ram >= ram_regex(row.min_specs)):
            os_ram_rows.append(row)
    return results(os_ram_rows)


@app.route("/results")
def results(os_ram_rows):
    print(len(os_ram_rows))
    return render_template('results.html', url=store_url, rows=os_ram_rows)


@app.route("/")
def main():
    return results()


if __name__ == '__main__':
    app.run(debug=True)