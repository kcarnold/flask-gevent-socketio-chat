I couldn't find a minimal example of using [Flask](http://flask.pocoo.org/) (a small web framework) with [gevent-socketio](https://github.com/abourget/gevent-socketio) (a simple way to get websockets). So this is a straight-up port of the [chat example](https://github.com/abourget/gevent-socketio/blob/master/examples/chat.py) from gevent-socketio to Flask.

You'll need Flask and gevent-socketio installed. Then just run `python server.py`.


# What is this about ?

This is a fix and doc completion from original sample located at https://github.com/kcarnold/flask-gevent-socketio-chat.

I forked the project because of missing instruction in doc and original project lauching with a server error.


As mentionned in the top paragraph from _kcarnold_, this is a basic sample realtime chat based on gevent-socketio written in Flask.

It works with no database and aims to remain very basic.


# Installation


## Installing gevent

You might be required to have gevent installed on your machine

On a Mac OS using brew :

    brew install gevent

On a Debian/Ubuntu computer :

    sudo aptitude install gevent

## Preparing the project with virtualenv

If you use virtualenv (very much encouraged though not mandatory)

    virtualenv venv
    . venv/bin/activate

## Install the project and its dependencies

    git clone git@github.com:vinyll/flask-gevent-socketio-chat.git
    cd flask-gevent-socketio-chat
    pip install -r requirements.pip


# How to run

    python server.py


Now open a browser and enter http://localhost:8080 in your address bar.

Open another browser (on another tab/window) and chat between windows.


