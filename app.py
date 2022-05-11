from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.rg2sr.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/savepost", methods=["POST"])
def save_post():
<<<<<<< HEAD
    url_receive = request.form["url_give"]
=======
    img = request.files["file_give"]
    extension = img.filename.split('.')[-1]
    filename = f'img'
    save_to = f'static/{filename}.{extension}'
    img.save(save_to)
>>>>>>> 5cb92abb044a48fa63d5b0d7dd451edb74128a93
    title_receive = request.form["title_give"]
    category_receive = request.form["category_give"]
    price_receive = request.form["price_give"]
    starpoints_receive = request.form["starPoints_give"]
    comment_receive = request.form["comment_give"]

    post_list = list(db.savepost.find({}, {'_id:False'}))
    count = len(post_list) + 1

    doc = {
        'num': count,
<<<<<<< HEAD
        'url' : url_receive,
=======
        'img': f'{filename}.{extension}',
>>>>>>> 5cb92abb044a48fa63d5b0d7dd451edb74128a93
        'title' :title_receive,
        'category' : category_receive,
        'price' : price_receive,
        'starpoints': starpoints_receive,
        'comment': comment_receive
    }

    db.savepost.insert_one(doc)

    return jsonify({'msg':'등록 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)