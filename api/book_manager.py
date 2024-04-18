from flask import Flask, request, jsonify
from config import db, app
from models import Book, BookSchema, book_schema, books_schema


@app.route("/", methods=['GET'])
def get_books():
    query = Book.query.all()
    result = books_schema.dump(query)
    return result

@app.route("/book/<int:id>", methods=['GET'])
def get_book(id):
    query = Book.query.get(id)
    result = book_schema.dump(query)
    return result

@app.route("/delete/<int:id>", methods=['DELETE'])
def delete_book(id):
    message = {}
    delete_query = Book.query.filter_by(id=id).first()
    db.session.delete(delete_query)
    db.session.commit()
    message.update({
          'status': 204,
          'message': 'user record delete successfully!!! '
          })
    return jsonify(message)

@app.route("/update/<int:id>", methods=['PUT'])
def update_book(id):
    update_query = Book.query.filter_by(id=id).first()
    return "Book got update."

@app.route("/create", methods=['POST'])
def create_book():
    isbn =  request.json.get('isbn')
    author = request.json.get('author')
    title =  request.json.get('title')
    price =  request.json.get('price')
    data = Book(isbn=isbn, author=author, title=title, price=price)
    db.session.add(data)
    db.session.commit()
    return book_schema.dump(data), 201

if __name__=="__main__":   
    app.run(host='0.0.0.0', debug=True, port=1234)