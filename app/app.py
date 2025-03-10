from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """Hello, Welcome To Up The Chelsea Tech!  
This is a Flask app running on AWS EC2!    
Deployed using GitHub Actions!
Learning Docker is fun!"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
