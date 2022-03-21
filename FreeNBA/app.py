#!/usr/bin/env python  #step 1 import library
import json  # Step1 import libraries
import requests
from flask import Flask, render_template

# Step2 - create instance of Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myverysectretkey'

url = "https://free-nba.p.rapidapi.com/players?rapidapi-key=xxxxxxxxxxxxxxxxxxxx"

querystring = {"page": "0", "per_page": "50"}

headers = {
    'x-rapidapi-host': "free-nba.p.rapidapi.com",
    'x-rapidapi-key': "xxxxxxxxxxxxxxxxxxxx"
}

@app.route('/', methods=['GET'])
def index():
    req = requests.get(url)
    data = json.loads(req.content)
    return render_template('index.html', data=data['data'])



#response = requests.request("GET", url, headers=headers, params=querystring)
#print(response.text)

if __name__ == '__main__':
    host = '127.0.0.1'
    # port = 8080
    app.run(debug=True)
