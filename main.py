from flask import Flask
from routes.account import account
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'welcome to collage project backend'
app.register_blueprint(account, url_prefix='/account')
if __name__ == '__main__':
   app.run()
