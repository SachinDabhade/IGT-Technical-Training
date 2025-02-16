from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')

def home():

   return "Hello, Flask Server!"

@app.route('/contact')

def contact():

   return "Hello, Lets connect!"

@app.route('/about')

def about():

   return "Hello, I am Sachin!"
 
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
 
