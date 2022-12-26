
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Bot Running, Made By <a href='https://telegram.me/Rushidhar1999'>Rushidhar1999</a></h1>"

if __name__ == "__main__":
    app.run()
