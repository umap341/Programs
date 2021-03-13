from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'print('Welcome to Google App Engine! Thank you Prof Gao for teaching Cloud Technologies')
 #print('Thank you Prof.Gao for teaching Cloud Technologies')'
