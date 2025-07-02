from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return render_template("success.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)
