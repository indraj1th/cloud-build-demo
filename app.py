from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "hello world new"


if __name__ == "__main__":
    app.run(debug=False,host = '0.0.0.0', port = 8000 )