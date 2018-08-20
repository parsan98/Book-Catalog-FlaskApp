from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Genre, Book

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/genre/')
@app.route('/book/')
def showAllGenres():
    return "This page will show list of all my genres"


@app.route('/genre/<int:genre_id>/')
def showGenreItems(genre_id):
    return "This page will display all books in genre %s" %genre_id


@app.route('/book/new/')
def addBook():
    return "This page will provide a form to add new books"


@app.route('/book/<int:book_id>/')
def showBook(book_id):
    return "This page will display details of book %s" %book_id


@app.route('/book/<int:book_id>/edit/')
def editBook(book_id):
    return "This page will provide a form to edit details of book %s" %book_id


@app.route('/book/<int:book_id>/delete/')
def deleteBook(book_id):
    return "This page will provide a form to confirm deletion of book %s" %book_id



if __name__ == '__main__':
    app.debug = True;
    app.run(host='0.0.0.0', port=5000)
