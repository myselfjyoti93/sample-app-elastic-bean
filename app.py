from flask import Flask

app = Flask(__name__)

@app.route('/get_sample', methods=['GET'])
def get_sample():
    return "Hello World"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)