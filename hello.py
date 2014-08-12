import os
from flask import Flask
from flask import render_template, redirect, session, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html', name=session['name'])


@app.route('/wat')
def wat():
    return render_template('wat.html')

@app.route('/name', methods=['POST'])
def name():
    session['name'] = request.form['name']
    return redirect('/')


if __name__=='__main__':
    app.secret_key = '5'
    app.run(debug = True, use_reloader = True)

