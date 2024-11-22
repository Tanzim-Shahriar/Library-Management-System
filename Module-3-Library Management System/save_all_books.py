def save_all_books(all_books):
    with open("all_books.csv","w") as fp:
        for books in all_books:
            line=f"{books['Title']},{books['Author']},{books['ISBN']},{books['Publishing year']},{books['Price']},{books['Quantity']}\n"
            fp.write(line)
