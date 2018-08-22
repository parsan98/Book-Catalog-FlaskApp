from flask import Flask, render_template, url_for, request, redirect, jsonify, make_response
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Genre, Book
import json, random, string, httplib2, requests
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = json.loads(
    open('client_secret.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog"

# Antiforgery token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

# Connect
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    #See if user exists, if not make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    return output


# User helper functions
def getUserID(email):
    try:
        user = session.query(User).filter_by(email = email).one()
        return user.id
    except:
        return None

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session['email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# DISCONNECT - Revoke a current user token and reset login_session
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session['access_token']
    # Only disconnect a connected user
    if access_token is None:
    	response = make_response(json.dumps('Current user not connected.'), 401)
    	response.headers['Content-Type'] = 'application/json'
    	return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        #Reset user's session
	    del login_session['access_token']
	    del login_session['gplus_id']
	    del login_session['username']
	    del login_session['email']
	    del login_session['picture']
	    response = make_response(json.dumps('Successfully disconnected.'), 200)
	    response.headers['Content-Type'] = 'application/json'
	    return response
    else:
	    # Invalid token
	    response = make_response(json.dumps('Failed to revoke token for given user.', 400))
	    response.headers['Content-Type'] = 'application/json'
	    return response


# CRUD

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


@app.route('/book/<int:book_id>/')
def showBook(book_id):
    #return "This page will display details of book %s" %book_id
    book = session.query(Book).filter_by(id=book_id).one()
    genre = session.query(Genre).filter_by(id=book.genre_id).one()
    creator = session.query(User).filter_by(id=book.user_id).one()
    return render_template('book.html', book=book, genre=genre, creator=creator)


@app.route('/book/new/', methods=['GET', 'POST'])
def addBook():
    #return "This page will provide a form to add new books"
    if request.method == 'POST':
        genre = session.query(Genre).filter_by(id=request.form['genre']).one()
        user = session.query(User).filter_by(id=1).one()
        description = '{}'.format(request.form['description'])
        book = Book(name=request.form['name'],
                        author=request.form['author'],
                        description=description,
                        cover=request.form['cover'],
                        genre=genre,
                        user=user)
        session.add(book)
        session.commit()
        return redirect(url_for('showGenreItems', genre_id=genre.id))
    else:
        return render_template('createBook.html')


@app.route('/book/<int:book_id>/edit/', methods=['GET', 'POST'])
def editBook(book_id):
    #return "This page will provide a form to edit details of book %s" %book_id
    book = session.query(Book).filter_by(id=book_id).one()
    genre = session.query(Genre).filter_by(id=book.genre_id).one()
    creator = session.query(User).filter_by(id=book.user_id).one()
    if request.method == 'POST':
        book.name = request.form['name']
        book.author = request.form['author']
        book.description = '{}'.format(request.form['description'])
        book.genre = session.query(Genre).filter_by(id=request.form['genre']).one()
        book.cover = request.form['cover']
        return redirect(url_for('showBook', book_id=book.id))
    else:
        return render_template('editBook.html', book=book, genre=genre, creator=creator)


@app.route('/book/<int:book_id>/delete/', methods=['GET', 'POST'])
def deleteBook(book_id):
    #return "This page will provide a form to confirm deletion of book %s" %book_id
    book = session.query(Book).filter_by(id=book_id).one()
    creator = session.query(User).filter_by(id=book.user_id).one()
    if request.method == 'POST':
        # Delete function
        session.delete(book)
        session.commit()
        return redirect(url_for('showAllGenres'))
    else:
        return render_template('deleteBook.html', book=book, creator=creator)



#JSON API Endpoints

@app.route('/JSON/')
@app.route('/genre/JSON/')
@app.route('/book/JSON/')
def showAllGenresJSON():
    genres = session.query(Genre).order_by(Genre.name)
    return jsonify(genres=[x.serialize for x in genres])

@app.route('/genre/<int:genre_id>/JSON/')
def showGenreItemsJSON(genre_id):
    books = session.query(Book).filter_by(genre_id=genre_id)
    return jsonify(books=[x.serialize for x in books])

@app.route('/book/<int:book_id>/JSON/')
def showGenreItemsJSON(book_id):
    book = session.query(Book).filter_by(id=book_id).one()
    return jsonify(book=book.serialize)



if __name__ == '__main__':
    app.debug = True;
    app.secret_key = 'this_secret_key'
    app.run(host='0.0.0.0', port=5000)
