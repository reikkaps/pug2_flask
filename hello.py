
from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)

##
# flask routing via decorators
@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    if name != None:
        return 'Hello {}'.format(Name)
    return 'Hello World'


@app.route("/")
def index():
    return 'Index page'

##
# main for simple testing
if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True, 
            port=8888,
    )

