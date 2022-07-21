


class Book:
    def __init__(self,b_name,b_author,b_number):
        self.b_name = b_name
        self.b_author = b_author
        self.b_number = b_number
        self.available = True

    def find_book(self, target, book_lst):
        for book in book_lst:
            if target == book[0]:
                print(book)
                return True
        return False





def main():
    choice = 0
    try:
        # initialize books list "file name. r"
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
            book_name = raw_input("Enter the name of the book >>>")
            author_name = raw_input("Enter the name of the author >>>")
            page_num = raw_input("Enter the number of pages >>>")
            new_book = Book(book_name, author_name, page_num)
            books_App.append([book_name, author_name, page_num])

        elif choice == 2:
            placeholder_book = Book("", "", "")
            print("Looking up for a book...")
            keyword = raw_input("Enter name of the book: ")
            book_found = placeholder_book.find_book(keyword, books_App)
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




