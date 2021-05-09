from flask import Flask                 # using flask webserver
from threading import Thread            # imorting thread to run it simultaneously

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():                       # funtion to start thread
    t = Thread(target=run)
    t.start()