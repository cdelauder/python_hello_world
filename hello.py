import os
from flask import Flask
from flask import render_template, redirect, session

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html', name=session['name'])


@app.route('/wat')
def wat():
    return render_template('wat.html')

@app.route('/name', methods=['POST'])
def name():
    print 'VICTORY!'
    session['name'] = name #figure out how to retrieve the form data and put it here
    print session
    return redirect('/')


if __name__=='__main__':
    app.secret_key = '5fsdjfjew490j43igjerpogrspg-=greife'
    app.run(debug = True, use_reloader = True)

