from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import sys
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
def api():
    result = reg.regression("./data.csv",50,2000)
    print(result)
    return result


if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8050)
