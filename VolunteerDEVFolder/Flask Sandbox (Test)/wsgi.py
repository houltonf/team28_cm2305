#from flask import Flask, render_template, url_for
#app = Flask(__name__)

#if __name__ == '__main__':
#    application.run(debug=True)

"""@app.route("/")
def home():
    return "Hello, Flask"
print("ok")"""

from volunteer import app as application

if __name__ == '__main__':
    application.run(debug=True)
