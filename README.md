I couldn't find a minimal example of using [Flask](http://flask.pocoo.org/) (a small web framework) with [gevent-socketio](https://github.com/abourget/gevent-socketio) (a simple way to get websockets). So this is a straight-up port of the [chat example](https://github.com/abourget/gevent-socketio/blob/master/examples/simple_chat/chat.py) from gevent-socketio to Flask.


You'll need Flask and gevent-socketio installed. Then just run `python server.py`.

You can use virtualenv too, just type:

    mkvirtualenv flask-chat
    pip install -r requirements.txt
    python server.py
