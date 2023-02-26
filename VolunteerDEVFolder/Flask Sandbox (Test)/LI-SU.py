from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "This will be the login page"
print("Flask App 'LI-SU', should be running. ")