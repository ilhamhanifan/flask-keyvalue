from flask import Flask, jsonify, request
import redis

app = Flask(__name__)
rc = redis.Redis(host='app_redis', port='6379', db=0)

keyvalue = {}

@app.route("/set/", methods=['POST'])
def set_key_value():
    data = request.get_json()
    key, value = data['key'], data['value']
    
    existing_value = rc.get(key)

    if existing_value is not None:
        existing_value = existing_value.decode('utf-8')
        if existing_value == value:
            return jsonify({"message": "Key with this value already exist"})
        else:
            rc.set(key, value)
            return jsonify({"message": "Overwriting key with a new value"})
    else:
        rc.set(key, value)
        return jsonify({"message":"Key Value write success"})



