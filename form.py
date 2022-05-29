from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, URLField, PasswordField
from wtforms.validators import InputRequired, Length, Email, URL


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()], render_kw={'placeholder': 'Your Name'})
    email = EmailField('Email', validators=[InputRequired(), Email(message='This is not a valid email address.')], render_kw={'placeholder': 'your@email.com'})
    message = TextAreaField('Message', validators=[InputRequired(), Length(min=100, message='Message is too short. Type at least 100 characters.')], render_kw={'placeholder': 'Your message - at least 100 characters'})
    submit = SubmitField('Send')


class AddPortfolioItem(FlaskForm):
    title = StringField('Title', validators=[InputRequired()], render_kw={'placeholder': 'Project Name'})
    description = TextAreaField('Description', validators=[InputRequired()], render_kw={'placeholder': 'Detailed description about the project...'})
    url = URLField('Code Repository', validators=[InputRequired(), URL(message='This is not a valid URL.')], render_kw={'placeholder': 'https://github.com/zoard-ehmann'})
    submit = SubmitField('Add')


class AdminLogin(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(), Email(message='This is not a valid email address.')], render_kw={'placeholder': 'your@email.com'})
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')