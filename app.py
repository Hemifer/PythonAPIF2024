from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    return "HOME"

client = MongoClient('mongodb+srv://pistillityler:qn6U8A5qBvfAg0rY@cluster0.axcu3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['LS3FALL2024']
users_collection = db['Users']

print(users_collection)

@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in users_collection.find():
        user['_id'] - str(user['_id'])
        users.append(user)
    return jsomify(users)
if __name__ == '__main__':
    app.run(debug=True)