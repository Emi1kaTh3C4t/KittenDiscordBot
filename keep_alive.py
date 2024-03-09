""
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Мур мяу! Всё в порядке!"

def run():
    app.run(host="00.0.3", port=800)

def keep_alive():
    server = Thread(target=run)
    server.start()