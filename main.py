from datetime import datetime as dt

from flask import Flask, render_template


app = Flask(__name__)

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
    pass

@app.route('/portfolio')
def portfolio():
    pass

@app.route('/about')
def about():
    pass

@app.route('/contact')
def contact():
    pass

@app.route('/privacy-policy')
def privacy_policy():
    pass

@app.route('/imprint')
def imprint():
    pass

@app.route('/upload')
def upload():
    pass

if __name__ == '__main__':
    app.run(debug=True)