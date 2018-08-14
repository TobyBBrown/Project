from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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


@app.route("/results")
def results():
    return render_template('results.html', url=store_url, rows=test.query.all())


@app.route("/")
def main():
    return results()


if __name__ == '__main__':
    app.run(debug=True)