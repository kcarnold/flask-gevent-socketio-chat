from gevent import monkey; monkey.patch_all()
from flask import Flask, request, send_file

from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin

# The socket.io namespace
class ChatNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):
    def on_nickname(self, nickname):
        self.environ.setdefault('nicknames', []).append(nickname)
        self.socket.session['nickname'] = nickname
        self.broadcast_event('announcement', '%s has connected' % nickname)
        self.broadcast_event('nicknames', self.environ['nicknames'])
        # Just have them join a default-named room
        self.join('main_room')

    def on_user_message(self, msg):
        self.emit_to_room('main_room', 'msg_to_room', self.socket.session['nickname'], msg)

    def recv_message(self, message):
        print "PING!!!", message


# Flask routes
app = Flask(__name__)
@app.route('/')
def index():
    return send_file('chat.html')

@app.route('/socket.io.js')
@app.route('/stylesheets/style.css')
@app.route('/WebSocketMain.swf')
def static_file():
    return send_file(request.path[1:])

@app.route("/socket.io/<path:path>")
def run_socketio(path):
    socketio_manage(request.environ, {'': ChatNamespace})


if __name__ == '__main__':
    print 'Listening on http://localhost:8080'
    app.debug = True
    from socketio.server import SocketIOServer
    SocketIOServer(('0.0.0.0', 8080), app,
        namespace="socket.io", policy_server=False).serve_forever()
    
