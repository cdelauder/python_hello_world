import os
from flask import Flask
from flask import render_template, redirect, session, request

app = Flask(__name__)


@app.route('/')
def hello():
    if session:
        return render_template('hello.html', name=session['name'])
    else:
        return render_template('hello.html', name='')


@app.route('/wat')
def wat():
    return render_template('wat.html')

@app.route('/name', methods=['POST'])
def name():
    if session:
        session.pop('name', None)
        session['name'] = request.form['name']
    else:
        session['name'] = request.form['name']
    return redirect('/'), 302


if __name__=='__main__':
    app.secret_key = '5'
    app.run(debug = True, use_reloader = True)

