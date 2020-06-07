from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_output():
    a=5
    b=6
    c=a+b
    return str(c)

@app.route('/welcome',methods=['GET'])
def get_welcome():
    return "welocme"

if __name__ == '__main__':
    app.run(debug=True)