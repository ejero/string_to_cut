# String To Cut

[here](https://rosita-flask-app.glitch.me/) is the link to the web app.

This is a small web application that accepts a POST request and returns a JSON object with a string containing
every third letter of the original string.

#### In a terminal of your choice run the below command:

```
curl -d '{"string_to_cut": "your-string"}' -H "Content-Type: application/json" -X POST http://rosita-flask-app.glitch.me/test
```
