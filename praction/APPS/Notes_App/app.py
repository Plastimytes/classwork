#app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    new_note = Note(title=data['title'], content=data['content'])
    db.session.add(new_note)
    db.session.commit()
    return jsonify(new_note.to_dict()), 201
