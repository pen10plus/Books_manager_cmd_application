def main():
    try:
        # Initialize books list
        bookList = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print("The <theBooksList.txt> file is not found")
        print("Starting a new books list!")
        bookList = []

    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book:\n>>> ")
            nAuthor = input("Enter the name of the author:\n>>> ")
            nPages = input("Enter the number of pages:\n>>> ")
            bookList.append([nBook, nAuthor, nPages])

        elif choice == 2:
            print("Looking up a book...")
            keyword = input("Enter search term:\n>>> ")
            for book in bookList:
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("Displaying all books...")
            for book in bookList:
                print(book)

        elif choice == 4:
            print("Quitting Program")

    print("Program Terminated!")
    # Saving to external txt file
    outfile = open("theBooksList.txt", 'w')
    for book in bookList:
        outfile.write(",".join(book) + "\n")
    outfile.close()

if __name__ == "__main__":
    main()
