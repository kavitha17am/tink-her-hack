from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to get book recommendations
def get_books_by_genre(genre):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, author FROM books WHERE genre=?", (genre,))
    books = cursor.fetchall()
    conn.close()
    return books

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.json.get("genre")
    books = get_books_by_genre(genre)
    
    print("Books fetched from database:", books)  # Debugging line
    
    return jsonify(books)


if __name__ == '__main__':
    app.run(debug=True)
