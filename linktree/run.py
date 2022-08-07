from flask import Flask
from main import run

app = Flask(__name__)

@app.route('/')
def run_command():
    
    return run()

if __name__ == '__main__':
    app.run(debug=False, port=8080)