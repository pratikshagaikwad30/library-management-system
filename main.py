import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT,
    book_name TEXT           
               
)
""")
conn.commit()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. View Issued Book")
    print("8. Book ID")
    print("9. exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")

        cursor.execute(
            "INSERT INTO books (name) VALUES (?)",
            (book,)
        )
        conn.commit()

        print("Book added successfully!")

    elif choice == "2":
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        print("\nBooks in Library:")
        for book in books:
            print(book[0], "-", book[1])

    elif choice == "3":
        search = input("Enter book name to search: ")

        cursor.execute(
            "SELECT * FROM books WHERE name = ?",
            (search,)
        )

        book = cursor.fetchone()

        if book:
            print("Book Found!")
        else:
            print("Book Not Found!")

    elif choice == "4":
        delete_book = input("Enter book name to delete: ")

        cursor.execute(
            "DELETE FROM books WHERE name = ?",
            (delete_book,)
        )
        conn.commit()

        print("Book deleted successfully!")

    elif choice == "5":
        student = input("Enter student name: ")
        book = input("Enter book name: ")

        cursor.execute(
             "SELECT * FROM books WHERE name = ?",
             (book,)
        )

        result = cursor.fetchone()

        if result:
            cursor.execute(
               "INSERT INTO issued_books (student_name, book_name) VALUES (?, ?)",
               (student, book)
            )

            cursor.execute(
              "DELETE FROM books WHERE id = ?",
              (result[0],)
            )

            conn.commit()
            print("Book issued successfully!")

        else:
            print("Book not available!")

    elif choice == "6":
        book = input("Enter book name to return: ")

        cursor.execute(
           "SELECT * FROM issued_books WHERE book_name = ?",
           (book,)
        )

        result = cursor.fetchone()

        if result:
            cursor.execute(
               "INSERT INTO books (name) VALUES (?)",
               (book,)
            )

            cursor.execute(
               "DELETE FROM issued_books WHERE book_name = ?",
               (book,)
            )

            conn.commit()
            print("Book returned successfully!")

        else:
            print("This book was not issued!")

    elif choice == "7":
        cursor.execute("SELECT * FROM issued_books")
        books = cursor.fetchall()
        if books:
            print("\nIssued Books:")
            for issued_book in books:
                print(issued_book[0],"-",issued_book[1],"-",issued_book[2])
        else:
            print("No books are currently issued")
        
    
    elif choice == "8":
        search = input("Enter your book id: ")
        cursor.execute(
            "SELECT * FROM books WHERE id = ?",
            (search,)
        )

        book = cursor.fetchone()

        if book:
            print(book[0], "-", book[1])
        else:
            print("Book Not Found!")

    elif choice == "9":
        "SELECT * FROM books WHERE name = ?",
    
    elif choice == "10":
        print("Thank You!")
        conn.close()
        break
    

