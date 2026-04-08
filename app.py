from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # This tells Flask to look in the /templates folder for index.html
    return render_template('index.html')

@app.route('/api')
def api():
    return jsonify({"message": "Hello World"})

if __name__ == "__main__":
    app.run(debug=True)
