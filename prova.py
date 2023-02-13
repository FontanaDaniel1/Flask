from flask import Flask, render_template
app = Flask(__name__) #sempre

@app.route('/', methods=['GET'])
def hello_world():
    return ('<h1>Hello, world!</h1>')

@app.route('/it')
def ciao_mondo():
    return ('<h1>ciao mondo!</h1>')

@app.route('/benvenuto')
def benvenuto():
    return render_template('benvenuto.html')


if __name__ == '__main__': #sempre
  app.run(host='0.0.0.0', port=3245, debug=True) #sempre