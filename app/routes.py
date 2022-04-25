from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
    
books = [
    Book(1,"Title1","Action"),
    Book(2,"Title2","Self-Improvement"),
    Book(3,"Title3","Comedy")
]
books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    book_response = []
    for book in books:
        book_response.append({
        "id": book.id,
        "title": book.title,
        "description": book.description
        })
    return jsonify(book_response)