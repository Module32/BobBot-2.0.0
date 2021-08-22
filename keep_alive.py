from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "This is a simple webpage designed to keep Bob Bot 2.0.0 running.\n\nIf you reached this page by accident, don't worry! Simply close this page out and carry on with what you were doing before.\n\nVisit the official website here: https://Bob-Bot-100.mrnames.repl.co"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()