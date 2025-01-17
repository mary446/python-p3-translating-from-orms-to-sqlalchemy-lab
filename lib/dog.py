from models import Dog

import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    query =  session.query(Dog).filter_by(name=name).first()
    return query
def find_by_id(session, id):
     query = session.query(Dog).get(id)
     return query

def find_by_name_and_breed(session, name, breed):
    query =  session.query(Dog).filter_by(name=name, breed=breed).first()
    return query

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()
