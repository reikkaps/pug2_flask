
from flask import Flask, render_template, url_for

app = Flask(__name__)

##
# flask routing via decorators
@app.route("/hello/")
# can hold variable parts
@app.route("/hello/<name>")
def hello(name=None):
    if name != None:
        headline = 'Hello {}'.format(name)
    else:
        headline = 'Hello World'
    return render_template('hello.html', headline=headline)

@app.route("/")
@app.route("/set/<action>")
def index(action=None):
    return render_template('index.html', action=action)

##
# main for simple testing
if __name__ == "__main__":
    # http://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key#22463969
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True, 
            port=8888,
    )

