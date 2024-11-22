import Add_book
import View_all_books

all_books=[]

while True:
    print("Welcome To Library Management System---\n0. Exit\n1. Add books\n2. View all books\n")

    menu=input("Select any number: ")

    if menu=="0":
        print("Thanks for using library management system.")
        break
    elif menu=="1":
        all_books=Add_book.add_book(all_books)
    elif menu=="2":
        View_all_books.view_all_books(all_books)

    else:
        print("Enter any valid option.")

