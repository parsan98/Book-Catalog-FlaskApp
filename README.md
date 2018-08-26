# Book Catalog Flask App

This is a web application with CRUD functions which uses Google Oauth2 Login for user authentication and authorization to add, delete and edit books in the various genres provided in the category.

## Requirements

* Linux System with the following requirements satisfied:

  ```shell
  apt-get -qqy install python
  apt-get -qqy update
  apt-get -qqy install postgresql python-psycopg2
  apt-get -qqy install python-sqlalchemy
  apt-get -qqy install python-pip
  pip install --upgrade pip
  pip install werkzeug==0.8.3
  pip install flask==0.9
  pip install Flask-Login==0.1.3
  pip install oauth2client
  pip install requests
  pip install httplib2
  
  ```

* You can either use your Linux system or you can download the vagrant configuration provided here:  <https://github.com/udacity/fullstack-nanodegree-vm>

## Getting started

* Download the repository and transfer the contents into an empty folder (if you are using the vagrant system provided, then transfer the contents into the empty folder named catalog).
* Make sure your system has the above mentioned libraries installed by running the shell script lines given in the Requirements section.
* Using your system's shell terminal, navigate into the folder you have stored the repository in. Run ```ls``` command to make sure the following files are available in it:
  * static
    * styles.css
    * headerStyleLarge.css
    * headerStyleSmall.css
  * templates (11 html files)
  * client_secret.json
  * database_setup.py
  * database_init.py
  * application.py
* Run ```python database_setup.py``` on the terminal and then confirm that in the file, a new database file has been added.
* Run ```python database_init.py``` on the terminal to populate the database with values. Notice that once this is done, a message gets printed on the terminal saying that the database has been initialized.
* Run ```python application.py``` to run the app - the app runs on <https://localhost:5000>



### JSON Endpoints:

To access the JSON endpoints:

* Use the URL <https://localhost:5000/JSON> to access the list of all genres with their details.
* Use the URL <https://localhost:5000/genre/1/JSON> replacing 1 with the id of any genre you wish to see to access all the books of that genre.
* Use the URL <https://localhost:5000/book/1/JSON replacing 1 with the id of the book you wish to see to access all the details of that book.



## Features

* Web Application written in Python
* Uses Flask micro web framework
* CRUD functions with restricted access  for authenticated and authorized users
* Google Oauth2 login has been provided as the means to log in
* Responsively designed - the site can be viewed on all screen sizes from mobile to pc.
* This project has been released with UNLICENSE.

**Note:** This is a project for Udacity Full Stack Web Development Nanodegree.