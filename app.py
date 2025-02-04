from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from pass_utils import generate_pass, check_pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Define the Word model
class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)

# Define the Leaderboard model
class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    word_list = Word.query.all()
    return render_template("index.html", word_list=word_list)

@app.route('/add', methods=['POST'])
def add():
    word = request.form.get('word')
    if word:
        new_word = Word(word=word)
        db.session.add(new_word)
        db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:word_id>')
def delete(word_id):
    word = Word.query.get_or_404(word_id)
    db.session.delete(word)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/generate', methods=['POST'])
def generate():
    words = Word.query.all()
    pass_length = request.form.get('typeNumber')
    name = request.form.get("name")
    if not (name and pass_length.isdigit()):
        return redirect(url_for("index"))
    pass_length = int(pass_length)
    password = generate_pass(words, pass_length)
    score = check_pass(password)
    new_leaderboard = Leaderboard(name=name, password=password, score=score)
    db.session.add(new_leaderboard)
    db.session.commit()
    return redirect(url_for("leaderboard"))

@app.route('/leaderboard')
def leaderboard():
    leader = Leaderboard.query.order_by(Leaderboard.score.desc()).all()
    return render_template("leaderboard.html", leader=leader)

@app.route('/whatsthis')
def whatsthis():
    return render_template("whatsthis.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
