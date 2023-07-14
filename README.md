# String To Cut

This is a small web application that accepts a POST request and returns a JSON object with a string containing
every third letter of the original string.

[Here](https://rosita-flask-app.glitch.me/){target="_blank"} is the link to the web app.

Web application uses
- HTML
- Python
- Flask


Open terminal and run this curl command (be sure to change the text "your string here"):

```bash
curl -d '{"string_to_cut": "your string here"}' -H "Content-Type: application/json" -X POST http://rosita-flask-app.glitch.me/test
```


## Test locally using Flask


### Installation
- Flask
- Python 3.7 or newer

### Mac/Linux 
```bash
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
pip install Flask 
export FLAK_APP=<your_app_name>
Flask run
```

### Windows 
```bash
pip install virtualenv
virtualenv <your-env>
source <your-env>\Scripts\activate
set FLASK_APP= <your_app_name>


### Terminal will show

```bash
Running on http://127.0.0.1:5000/
```

Learn more about Flask [here](https://flask.palletsprojects.com/en/2.1.x/)
