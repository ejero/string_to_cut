from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify



app = Flask(__name__)

@app.route("/")
def home():
  return render_template('test.html')

# accepts only a post request
@app.route("/test", methods= ['POST'])
def cutting_string():
  data = request.get_json()  
  string_to_cut = data['string_to_cut']
  
  
  # every third letter in the string  
  returned_string = jsonify({"return_string": string_to_cut[2::3]})
  
  return returned_string


  
if __name__ == "__main__":
  app.run()
