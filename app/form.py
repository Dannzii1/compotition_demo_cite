from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Email


class ContactForm(FlaskForm):
    full_name = StringField('Full Name', validators=[InputRequired(message="Your First Name is Required")])
    contestant = StringField('Favorite Contestant and mix drink they made:', validators=[InputRequired(
        message="Tell us your favorite contestant's name and mix drink")])
    versus = StringField('Favorite face off moment between two contestants:', validators=[InputRequired(
        message="Tell us your favorite moment")])
    email = StringField('Email', validators=[InputRequired(message="Email is Required"),
                                             Email(message="Your Email is not a valid Email address")])
