from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! Welcome to my Flask app."

@app.route('/about')
def about():
    return "This is a simple Flask application."

@app.route('/contact')
def contact():
    return "Contact us at contact@example.com."

if __name__ == '__main__':
    app.run(debug=True)
