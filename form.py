from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()], render_kw={'placeholder': 'Your Name'})
    email = EmailField('Email', validators=[InputRequired(), Email(message='This is not a valid email address.')], render_kw={'placeholder': 'your@email.com'})
    message = TextAreaField('Message', validators=[InputRequired(), Length(min=100, message='Message is too short. Type at least 100 characters.')], render_kw={'placeholder': 'Your message - at least 100 characters'})
    submit = SubmitField('Send')