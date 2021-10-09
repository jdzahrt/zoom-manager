from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def zoom_notification():
    print(type(request.data))
    print(request.data)
    my_json = request.data.decode('utf8')
    print(type(my_json))
    data = json.loads(my_json)
    print(type(data))
    print(data['event'])
    return "<p>Hello, World....NOT!</p>"