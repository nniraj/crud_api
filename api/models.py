from config import db, ma

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)


class BookSchema(ma.Schema):
  class Meta:
    fields = ('id', 'isbn', 'author', 'title', 'price')

# Init schema
book_schema = BookSchema()
books_schema = BookSchema(many=True)