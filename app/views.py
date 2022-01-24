from app import app
from flask import render_template, url_for
import os

from app.form import ContactForm


@app.route('/')
def landing_page():
    form = ContactForm()
    return render_template('landing_page.html', form=form, form_action=url_for('landing_page'))

