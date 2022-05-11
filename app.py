from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, Me!</h1>"

@app.route("/test")
def string_to_cut():
    string_to_cut = "iamyourlyftdriver"

    string_value = {
        "string_to_cut": string_to_cut
    }

    return json.dumps(string_to_cut)
 

if __name__ == "__main__":
    app.run(debug=True)