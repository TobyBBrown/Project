from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from regex import *
from models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Katm2803@localhost:3306/project'
db = SQLAlchemy(app)


store_url = 'https://store.steampowered.com/app/'


@app.route("/input")
def hardware_input():
    return render_template('input.html', cpus=db.session.query(cpubenchmarks).all(),
                           gpus=db.session.query(gpubenchmarks).all())


@app.route("/hardware_submit", methods=['POST'])
def hardware_submit():
    cpu = db.session.query(cpubenchmarks).get(request.form['CPU'])
    gpu = db.session.query(gpubenchmarks).get(request.form['GPU'])
    ram = int(request.form['ram_num'])
    os = int(request.form['os_version'])
    order = request.form['order_by']
    rows = db.session.query(game_requirements).filter(game_requirements.min_cpu_score < cpu.benchmark_score,
                                          game_requirements.min_gpu_score < gpu.benchmark_score).order_by\
                                          (desc(order)).all()
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