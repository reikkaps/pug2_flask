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

Zuerst importiert das Skript die Flask-Klasse, anschließend erzeugt es
eine Instanz (app) dieser Klasse.  Das erste Argument dieses Aufrufs
setzt den Namen der Instanz - hier __name__. Über diese Bezeichnung findet
Flask weitere Dateien - etwas Templates. Dazu später mehr.

Die Zeile `@app.route(...` ist eine Decorator, mit dem man dem Skript
vorgibt, über welche URL die nachfolgenen Anweisungen aufgerufen werden.

Im Beispiel ist das die Funktion *hello*, die den String "Hello World" an die
Flask-App zurückgibt.

**Speichere dieses Beispiel nicht unter dem Namen flask.py**


