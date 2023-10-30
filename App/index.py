from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/test")
def test():
    return "Test con cac"


#path params
@app.route("/hello/<name>")
def hello(name):
    return render_template("index.html",
                           message="Xin chao %s" % name)

if __name__ == "__main__":
    app.run(debug=True)