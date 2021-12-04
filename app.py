"""A simple Pyjamas API
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    """
        **Create API**
        This creates an instance of the Flask API and runs it
    """
    return jsonify({"hello": "world"})


if __name__ == "__main__":
    app.run(debug=True)
