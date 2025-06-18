from flask import Flask, jsonify
import os

app = Flask(__name__)
#s

@app.route('/api/data')
def get_data():
    data = {
        "status": "success",
        "timestamp": "2025-06-18T06:25:48Z", 
        "items": [
            {"id": 1, "name": "Item A"},
            {"id": 2, "name": "Item B"},
            {"id": 3, "name": "Item C"}
        ]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
