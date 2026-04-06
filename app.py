from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def home():
    return "Welocome to my To-Do App!"
@app.route('/api')
def api():
    return jsonify({"message": "Hello World"})

if __name__ == "__main__":
    app.run(debug=True)
