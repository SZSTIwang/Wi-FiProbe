from flask import Flask, request

app = Flask(__name__)

@app.route('/he/<string:name>/<string:id>')
def hello_world(name, id):
    return 'hello world' + name + id

if __name__ == '__main__':
    app.run(port=8888, debug=True)
