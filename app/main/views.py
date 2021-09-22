from flask import render_template
from . import main
from flask import Flask

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/Entry_form/')
def Entry_form ():
    Entry_form = Entry_form()

    '''
    View movie page function that returns the form entry page for user login and its data
    '''
    return render_template('Entry_form.html', Entry_form =Entry_form  )
