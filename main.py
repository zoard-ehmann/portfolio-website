import os
from datetime import datetime as dt

from flask import Flask, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
from form import ContactForm, PortfolioForm, AdminLogin
from mailer import Mailer


load_dotenv()

app = Flask(__name__)
login_manager = LoginManager()

app.secret_key = os.getenv('APP_SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager.init_app(app)


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


@login_manager.user_loader
def load_user(uid):
    return db.session.query(User).get(uid)


@app.context_processor
def inject_now():
    return {
        'now': dt.utcnow()
    }


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/portfolio')
def portfolio():
    portfolio = db.session.query(Work).all()
    return render_template('portfolio.html', works=portfolio)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    mailer = Mailer()

    if form.validate_on_submit():
        mailer.send_mail(s_name=form.name.data, s_email=form.email.data, s_msg=form.message.data)
        return render_template('contact.html', form=form, submitted=True)

    return render_template('contact.html', form=form, submitted=False)


@app.route('/privacy-policy')
def privacy_policy():
    pass


@app.route('/imprint')
def imprint():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = AdminLogin()

    if current_user.is_authenticated:
        return redirect(url_for('portfolio'))

    if form.validate_on_submit():
        user = db.session.query(User).filter_by(email=form.email.data).first()

        if user and check_password_hash(pwhash=user.password, password=form.password.data):
            login_user(user)
            return redirect(url_for('portfolio'))
        flash('Invalid credentials, please try again.')

    return render_template('login.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = PortfolioForm()

    if form.validate_on_submit():
        new_work = Work(
            title = form.title.data,
            description = form.description.data,
            url = form.url.data
        )
        db.session.add(new_work)
        db.session.commit()
        return redirect(url_for('portfolio'))

    return render_template('portfolio_item.html', form=form)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id:int):
    work = db.session.query(Work).get(id)
    form = PortfolioForm(obj=work)

    # FIXME: duplicates shouldn't be allowed after edit
    if form.validate_on_submit():
        work.title = form.title.data
        work.description = form.description.data
        work.url = form.url.data
        db.session.commit()
        return redirect(url_for('portfolio'))

    return render_template('portfolio_item.html', form=form)


@app.route('/remove/<int:id>', methods=['GET'])
@login_required
def remove(id:int):
    work = db.session.query(Work).get(id)
    db.session.delete(work)
    db.session.commit()
    return redirect(url_for('portfolio'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)