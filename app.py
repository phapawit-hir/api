from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/webhook',methods=['GET','POST'])
def webhook():
    print('Connection')
    return 'Connection'

if __name__ == '__main__':
   app.run(debug=True)