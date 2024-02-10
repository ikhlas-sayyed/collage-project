from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/hello')
def f():
    return 'hii'

if __name__ == '__main__':
   app.run()
