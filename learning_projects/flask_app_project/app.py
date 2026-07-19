from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # This will render templates/index.html
    return render_template("index.html", title="Welcome to My Portfolio")

@app.route("/about")
def about():
    return render_template("about.html", title="About This App")

if __name__ == "__main__":
    # debug=True is fine for local development
    app.run(debug=True)