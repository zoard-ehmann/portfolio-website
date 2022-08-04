from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, URLField, PasswordField
from wtforms.validators import InputRequired, Length, Email, URL


class ContactForm(FlaskForm):
    """Contact form template with FlaskForm.

    Args:
        FlaskForm (class): Parent class.
    """
    name = StringField('Name', validators=[InputRequired()], render_kw={'placeholder': 'Your Name'})
    email = EmailField('Email', validators=[InputRequired(), Email(message='This is not a valid email address.')], render_kw={'placeholder': 'your@email.com'})
    message = TextAreaField('Message', validators=[InputRequired(), Length(min=100, message='Message is too short. Type at least 100 characters.')], render_kw={'placeholder': 'Your message - at least 100 characters'})
    submit = SubmitField('Send')


class PortfolioForm(FlaskForm):
    """CMS for portfolio items with FlaskForm.

    Args:
        FlaskForm (class): Parent class.
    """
    title = StringField('Title', validators=[InputRequired()], render_kw={'placeholder': 'Project Name'})
    description = TextAreaField('Description', validators=[InputRequired()], render_kw={'placeholder': 'Detailed description about the project...'})
    url = URLField('Code Repository', validators=[InputRequired(), URL(message='This is not a valid URL.')], render_kw={'placeholder': 'https://github.com/zoard-ehmann'})
    submit = SubmitField('Done')


class AdminLogin(FlaskForm):
    """Login page template with FlaskForm.

    Args:
        FlaskForm (class): Parent class.
    """
    email = EmailField('Email', validators=[InputRequired(), Email(message='This is not a valid email address.')], render_kw={'placeholder': 'your@email.com'})
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')