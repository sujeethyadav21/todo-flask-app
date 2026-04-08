<<<<<<< HEAD
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # This tells Flask to look in the /templates folder for index.html
    return render_template('index.html')

@app.route('/api')
def api():
    return jsonify({"message": "Hello World"})
=======
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.items

@app.route('/')
def home():
    return render_template('index.html')

# This is the "Door" that fixes your 404 error!
@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the HTML form
    name = request.form.get("itemName")
    description = request.form.get("itemDescription")
    
    # Save it to MongoDB
    collection.insert_one({
        "itemName": name,
        "itemDescription": description
    })
    
    return "Success! Item added to the database."
>>>>>>> master_2

if __name__ == "__main__":
    app.run(debug=True)
