from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from agent import agent_chain
from gevent import monkey
monkey.patch_all()

app = Flask(__name__)
socketio = SocketIO(app, async_mode='gevent')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(data):
    msg = data['msg']
    first_message = data['refresh']
    print('Message: ' + msg)
    response = chatbot_response(msg, first_message)  # Your chatbot response function goes here
    emit('response', response, broadcast=True)

def chatbot_response(msg, first_message = False):
    response = agent_chain.run(msg)
    return response

if __name__ == '__main__':
    socketio.run(app)
