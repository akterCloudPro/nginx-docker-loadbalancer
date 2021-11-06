from flask import Flask
import socket
container_id = socket.gethostname()

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, from akterCloudPro. This application is running on the container -  ' + container_id
