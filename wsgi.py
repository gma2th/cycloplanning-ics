from flask import Flask, send_file

app = Flask(__name__)


@app.route("/cycloplanning.ics")
def calendar():
    return send_file("cycloplanning.ics", mimetype="text/calendar")


if __name__ == "__main__":
    app.run(debug=True)
