# APP NAME

### Instagram Clone

## AUTHOR

Kipngetich Ngeno

## DESCRIPTION

This is an application more or less like the popular social media platform Instagram where users can sign up, post pictures
view pictures posted by others comment on them as well as like or dislike the pictures


## User stories
As a user can do the following:
* Sign in to the application to start using
* Upload pictures to the application.
* View their profiles containing all their pictures
* A user can Follow other users and see their the users  timeline.
* Like a picture and leave a comment on it.

## Set Up and Installation

#### Prerequisites

* Python 3.6.2
* Virtual environment
* Postgres Database
* Reliable Internet Connection

## Installation Process

* Copy repolink

in your terminal run the following commands

* $ git clone REPO-URL in your terminal
* $ cd Instagram_clone
* $ python3.6 -m venv virtual
* $ touch .env ( to the file add :
        SECRET_KEY=<your secret key>
        DEBUG=True)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt
* $ psql ; CREATE DATABASE instagram ;

In the settings.py module of the project make the following changes

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gram',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}

* $ python3.6 manage.py runserver (this command runs the application of port http://127.0.0.1/8000 )
 
## Known Bugs

No known bugs

## CREDITS

Moringa School,Python Documentation, StackOverflow.com and W3 schools

## Technologies Used

This project uses major technologies which are :

* HTML5/CSS
* Bootstrap
* Python3.6
* Django Frane Work

## Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through khalifngeno@gmail.com or leave a commit here on github.

## License

MIT License
Copyright (c) 2017 Kipngetich Ngeno

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.*

Copyright (c) 2017 ** Kipngetich Ngeno **