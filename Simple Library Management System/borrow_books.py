def borrow_a_book(list_of_books, borrowed_books):
    book_item = input("Enter the name of the book you want to borrow: ")
    if book_item in list_of_books:
        list_of_books.remove(book_item)
        borrowed_books.append(book_item)
        print(f"You have borrowed {book_item}")
    else:
        print(f"{book_item} is not available at the moment.")