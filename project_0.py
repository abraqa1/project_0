def find_book(target, book_lst):
    for book in book_lst:
        if target == book[0]:
            print(book)
            return True
    return False




def main():

    try:
        # initialize books list
        books_App = []
        infile = open("book_App.csv", "r")
        line = infile.readline()
        while line:
            books_App.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("the <book_App.csv> file is not found")
        print("Starting a new books list!")
    choice: int = 0
    while (choice != 4):
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) give book name")
        print("4) Quit")
        choice = int(input())
        print(choice)
        if choice == 1:
            print("Adding a book...")
            book_Name = input("Enter the name of the book >>>")
            author_Name = input("Enter the name of the author >>>")
            page_Num = input("Enter the number of pages >>>")
            books_App.append([book_Name, author_Name, page_Num])

        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter name of the book: ")
            book_found = find_book(keyword, books_App)
            if book_found is False:
                print("Book Is Not Found")



        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(books_App)):
                print(books_App[i])

        elif choice == 4:
            print()
            print("Quitting The Program")
        print("Program Terminated!")

        # Saving to external file
        outfile = open("book_App.csv", "w")
        for book in books_App:
            outfile.write(",".join(book) + "\n")
        outfile.close()


if __name__ == "__main__":
    main()

