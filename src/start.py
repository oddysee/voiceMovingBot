import json


from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/move', methods=['POST'])
def move():
    movementRequests=request.get_json()

    print(movementRequests)

    return 'h'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')