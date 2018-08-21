from flask import Flask, render_template, url_for
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
    #return "This page will show list of all my genres"
    genres = session.query(Genre).order_by(Genre.name)
    return render_template('allGenres.html', genres=genres)



@app.route('/genre/<int:genre_id>/')
def showGenreItems(genre_id):
    #return "This page will display all books in genre %s" %genre_id
    genre = session.query(Genre).filter_by(id=genre_id).one()
    books = session.query(Book).filter_by(genre_id=genre_id).all()
    return render_template('allBooks.html', genre=genre, books=books)



@app.route('/book/new/')
def addBook():
    #return "This page will provide a form to add new books"
    return render_template('createBook.html')


@app.route('/book/<int:book_id>/')
def showBook(book_id):
    #return "This page will display details of book %s" %book_id
    book = session.query(Book).filter_by(id=book_id).one()
    genre = session.query(Genre).filter_by(id=book.genre_id).one()
    creator = session.query(User).filter_by(id=book.user_id).one()
    return render_template('book.html', book=book, genre=genre, creator=creator)


@app.route('/book/<int:book_id>/edit/')
def editBook(book_id):
    #return "This page will provide a form to edit details of book %s" %book_id
    book = session.query(Book).filter_by(id=book_id).one()
    genre = session.query(Genre).filter_by(id=book.genre_id).one()
    creator = session.query(User).filter_by(id=book.user_id).one()
    return render_template('editBook.html', book=book, genre=genre, creator=creator)


@app.route('/book/<int:book_id>/delete/')
def deleteBook(book_id):
    #return "This page will provide a form to confirm deletion of book %s" %book_id
    book = session.query(Book).filter_by(id=book_id).one()
    creator = session.query(User).filter_by(id=book.user_id).one()
    return render_template('deleteBook.html', book=book, creator=creator)



if __name__ == '__main__':
    app.debug = True;
    app.run(host='0.0.0.0', port=5000)
