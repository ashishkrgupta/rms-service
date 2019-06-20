from flask import Flask, jsonify
import datetime
import json

app = Flask(__name__)

@app.route("/")
def getInvoice():
    inv = {
        "date": datetime.datetime.now(),
        "total": 1452.1,
        "items": [{"name": "item1"}, {"name":"item2"}]
    }
    return jsonify(inv)

if __name__ == "__main__":
    app.run()    
