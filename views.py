from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/Entry_form/')
def Entry_form ():
    Entry_form = Entry_form()

    '''
    View movie page function that returns the form entry page for user login and its data
    '''
    return render_template('Entry_form.html' Entry_form =Entry_form  )
