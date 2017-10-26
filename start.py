import json


from flask import Flask, request

app = Flask(__name__)

@app.route('/move', methods=['POST'])
def move():
    movementRequests=request.get_json()
    
    print(movementRequests)

    return 'h'