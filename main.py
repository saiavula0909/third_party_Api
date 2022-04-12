from django.test import tag
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/api/ping",methods=['GET'])
def tech():
    url = 'https://api.hatchways.io/assessment/blog/posts'
    data = requests.get(url)
    return data.json()

@app.route("/api/posts/<name>",methods=['GET'])
def health(name):
    url = 'https://api.hatchways.io/assessment/blog/posts?tag=' + str(name) 
    print(url)
    data = requests.get(url)
    return data.json() 
if __name__ == '__main__':
  
    app.run(debug=True)
