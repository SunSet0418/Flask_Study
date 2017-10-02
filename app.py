from flask import Flask, request, render_template, redirect
from routes import auth
import db



app = Flask(__name__)
app.register_blueprint(auth.blueprint, url_prefix='/auth')

@app.route('/', methods=['GET'])
def TOP():
    return redirect('/main')


@app.route('/main', methods=['GET'])
def Main():
    return "<h1>Hello</h1>"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
