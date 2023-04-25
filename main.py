from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from pass_utils import generate_pass, check_pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100))
    
@app.route('/')
def index():
    word_list = Word.query.all()
    return render_template("index.html", word_list=word_list)

@app.route('/add', methods=['POST'])
def add():
    word = request.form.get('word')
    new_word = Word(word=word)
    db.session.add(new_word)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:word_id>')
def delete(word_id):
    word = Word.query.filter_by(id = word_id).first()
    db.session.delete(word)
    db.session.commit()
    return redirect(url_for("index"))


class Leaderboard(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60))
    password = db.Column(db.String(100))
    score = db.Column(db.Integer())


@app.route('/generate', methods=['POST'])
def generate():
    words = Word.query.all()
    pass_length = request.form.get('typeNumber')
    name = request.form.get("name")
    password = generate_pass(words, pass_length)
    score = check_pass(password)
    new_learderboard = Leaderboard(name=name,password=password,score=score)
    db.session.add(new_learderboard)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/leaderboard')
def leaderboard():
    leader = Leaderboard.query.order_by(Leaderboard.score.desc())
    return render_template("leaderboard.html", leader=leader)

@app.route('/whatsthis')
def whatsthis():
    return render_template("whatsthis.html")

if __name__ == '__main__':
    app.run(debug=True)
