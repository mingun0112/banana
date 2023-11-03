import json
import cv2
import os
from flask import Flask, send_from_directory, request, jsonify, session
import base64
import random
from draw_object import DrawObject

app = Flask(__name__)


app.secret_key = "your_secret_key_here"  # 세션에 사용할 비밀 키 설정

# @app.before_request
# def before_request():
#     g.filter_value = True  # 초기 필터 값 설정

@app.route("/")
def base():
    return send_from_directory('build', 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory('build', path)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

@app.route("/filter", methods=['POST'])
def filterFunc():
    if request.method == 'POST':
        try:
            data = request.data.decode("utf-8")
            data = json.loads(data)
            # g.filter_value = data["filter"]
            # print(g.filter_value)
            session['filter_value'] = data["filter"]  # 세션에 필터 값을 저장
            #print(session['filter_value'])
            return jsonify({"filter": session['filter_value']})
        except Exception as e:
            return jsonify({"error": str(e)})

@app.route("/post", methods=['POST'])
def image():
    if request.method == 'POST':
        try:
            body_data = request.data.decode("utf-8")
            json_data = json.loads(body_data)

            file_name = json_data["filepath"]
            directory_path = "/mnt/pose/images"
            image_path = os.path.join(directory_path, file_name)
            
            filter_value_local = session.get('filter_value', True)
            print(filter_value_local)
            if os.path.isfile(image_path):
                base64_string = DrawObject(image_path, json_data, filter_value_local)

                return jsonify({"message": str(base64_string)})
        except Exception as e:
            return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host='192.168.0.160', port=9900, debug=True)
