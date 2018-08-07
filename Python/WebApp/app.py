from flask import Flask, render_template
from mysql.connector import MySQLConnection, Error

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()