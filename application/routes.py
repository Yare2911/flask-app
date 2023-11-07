from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):
    return {
        'id': character.id,
        'name': character.name,
        'age': character.age,
        'catch_phrase': character.catch_phrase
    }

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route('/characters', methods=['POST'])
def create_character():
    #retrieve the body - req.body 
    data = request.json
    character = FriendsCharacter(data['name'], data['age'], data['catch_phrase'])
    # send it to the database
    db.session.add(character)
    # commit it to the database
    db.session.commit()
    # return a response
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route('/characters')
def get_characters():
    characters = FriendsCharacter.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return {'characters': character_list}


@app.route('/characters/<id>')
def get_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route('/characters/<id>', methods=['DELETE'])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return "Character deleted"

@app.route('/characters/<id>', methods=['PATCH'])
def update_character(id):
    character = FriendsCharacter.query.filter_by(id=id)
    data = request.json
    character.update(dict(name=data['name'], age=data['age'], catch_phrase=data['catch_phrase']))
    db.session.commit()
    updateCharacter = FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=updateCharacter.id, name=updateCharacter.name, age=updateCharacter.age, catch_phrase=updateCharacter.catch_phrase)
    
    
    

