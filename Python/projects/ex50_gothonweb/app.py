from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="templates/")
app.debug=True
@app.route("/")
def index():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run(threaded=True)
