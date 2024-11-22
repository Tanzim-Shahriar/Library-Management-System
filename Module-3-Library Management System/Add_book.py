from save_all_books import save_all_books


def add_book(all_books):
    title=input("Enter Book title:")
    author=input("Enter the author name:")
    ISBN=int(input("Enter the ISBN number:"))
    publishing_year=int(input("Enter the publishing year:"))
    price=int(input("Enter Book price:"))
    quantity=int(input("Enter how mane quantity are available:"))

    book = {
        "Title": title,
        "Author": author,
        "ISBN": ISBN,
        "Publishing year": publishing_year,
        "Price": price,
        "Quantity": quantity,
    }

    all_books.append(book)
    save_all_books(all_books)
    print("Book added successfully.")
    return all_books