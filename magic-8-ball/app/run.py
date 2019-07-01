from flask import Flask, render_template
import datetime
from magic8ball import responses

app = Flask(__name__)

@app.route("/")
def magic8ball():
    return render_template('index.html', options=responses)

if __name__ == '__main__':
    app.run(debug=True)
