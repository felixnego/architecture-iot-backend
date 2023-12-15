from flask import Flask, jsonify
import time


app = Flask(__name__)

# Function to simulate a delay
def sleep(seconds):
    time.sleep(seconds)

# # Route 1
# @app.route('/route1')
# def route1():
#     sleep(1)
#     return jsonify(message='Response from Route 1')

# # Route 2
# @app.route('/route2')
# def route2():
#     sleep(2)
#     return jsonify(message='Response from Route 2')

# Route 3
@app.route('/route3')
def route3():
    sleep(3)
    return jsonify(message='Response from Route 3')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3003)
