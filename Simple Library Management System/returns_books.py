def return_a_book(list_of_books, borrowed_books):
    book_item = input("Enter the name of the book you want to return: ")
    if book_item in borrowed_books:
        list_of_books.append(book_item)
        borrowed_books.remove(book_item)
        print(f"You have returned {book_item}")
    else:
        print(f"{book_item} is not available at the moment.")
