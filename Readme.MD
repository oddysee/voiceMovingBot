# Setup

## The easy way

`docker-compose up --build`

## The hard way

1. Install [Flask](http://flask.pocoo.org/docs/0.12/installation/#virtualenv).

    For windows - `.\Scripts\activate`

2. Continue with following instructions [here](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application).

3. 
    ```bash
    $env:FLASK_APP = 'start.py'
    flask run
   ```