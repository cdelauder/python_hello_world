import os
from flask import Flask
from flask import render_template, redirect, session

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/wat')
def wat():
    return render_template('wat.html')

@app.route('/name', methods=['POST'])
def name():
    session['name'] = name
    return redirect('/')


if __name__=='__main__':
    app.run(debug = True, use_reloader = True)