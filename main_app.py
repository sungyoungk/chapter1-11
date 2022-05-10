from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('mongodb+srv://test:sparta@cluster0.zaev4.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAfile=ca)
db = client.dbsparta_plus_week1


@app.route('/main')
def home():
    return render_template('main.html')

@app.route('/diary', methods=['POST'])
def save_diary():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST 요청 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)