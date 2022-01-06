from flask import Flask, jsonify, make_response, render_template, request
import cv2


app = Flask(__name__)

@app.route('/')
def index() -> str:
    info = "index"
    return render_template('index.html', info = info)


@app.route('/picture', methods=["POST"])
def process_picture():
    print(request)
    response = make_response(jsonify({"result": 1, "status": 200}))
    return response

if __name__ == '__main__':
    app.run(debug=True)
