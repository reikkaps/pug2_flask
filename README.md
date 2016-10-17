# pug2_flask
Kleine Einführung in das Microframework flask
<http://flask.pocoo.org/>

- Entwicklungsserver und Debugger
- Unit-Test-Unterstützung
- Jinja2 Templates
- secure cookies
- 100% WSGI 1.0 kompatibel
- Unicode
- gut dokumentiert

## Installation

### Voraussetzungen

1. python (2.7 oder 3.x)
2. virtualenv

`apt-get install python3 virtualenv`

### Einrichten

1. Virtuelle Umgebung anlegen ... `$> virtualenv -p /usr/bin/python3 venv`

2. Ins Virtualenv wechseln ... `$> . venv/bin/activate`

3. Flask installieren und einrichten ... `$ [venv] > pip install Flask`

## Hello Flask

**Ganz einfache Flask-App ohne Magie:**

~~~~~ {.python}
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

~~~~~


