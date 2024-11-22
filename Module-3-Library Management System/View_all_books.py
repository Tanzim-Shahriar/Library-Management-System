def view_all_books(all_books):
    if all_books!=[]:
        for books in all_books:
            print(f"Title: {books['Title']} | Author: {books['Author']} | ISBN: {books['ISBN']} | Publishing Year: {books['Publishing year']} | Price: {books['Price']} | Quantity: {books['Quantity']}")
    else:
        print("No book found in the list.")