from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/data', methods=["GET"])
def save_data():
    regnumber = request.args['regnumber']
    name = request.args['name']
    classnumber = request.args['classnumber']
    math = request.args['math']
    english = request.args['english']
    science = request.args['science']
    computer = request.args['computer']
    print(regnumber, name, classnumber, math, english, science, computer)

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)

