from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import sys
import requests
sys.path.append('./lib')
import regression as reg



app = Flask(__name__)
CORS(app)
resources = {r"/api/*": {"origins": "*"}}
app.config["CORS_HEADERS"] = "Content-Type"
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def home():
    return jsonify({"Message":"This is your flask app with docker"})

@app.route('/api')
def api(target=1000):
    url = "https://storageapi.fleek.co/987b8a92-ce10-4962-babf-e958d970ddac-bucket/sensor_data/data.csv"
    r = requests.get(url)
    open('data.csv', 'wb').write(r.content)
    result = reg.regression("./data.csv",50,target)
    print(result)
    return result


if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8050)
