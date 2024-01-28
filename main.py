def main():
    
    try:
    #initialize  books list
        book_list = []
        
        infile =open("theBookslist.txt", "r")
        line=infile.readline()
        while line:
            book_list.append(line.rstrip("\n").split(","))
            line=infile.readline()
        infile.close()
        
    except FileNotFoundError:
        print("The bookslist.txt   file is not found")
        print("Starting a new book list...") 
        book_list = []
        
        
        
        
    choice = 0
    
    while choice != 4:
        print("*** Books manager ***")
        print("1) Add a book")
        print("2) Look up a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())
        
        if choice == 1:
            
            print("Adding a  book .....")
            nBook=input('Enter the name of the book  >>> ')
            nAuthor=input('Enter the name of the name of the author >>> ')
            npages=input('Enter the number of pages >>> ')

            book_list.append([nBook,nAuthor,npages])
            
    
        elif choice == 2:
            
            print("Looking up a book.....")
            keyword= input('Enter search term:   ')
            
            for book in book_list:
                if keyword in book:
                    print(book)
                    
        elif choice == 3:
            
            print("Displaying all books.....")
            
            for i in range(len(book_list)):
                
                print(book_list[i])
                
    
    
        elif choice == 4:
            
            print(" Quiting the Program.....")
            break
    print("Program terminated")
    
    # savings to external database
    
    outfile=open("theBookslist.txt",'w')
    for book in book_list:
        outfile.write(" ".join(book) + "\n")
        
    outfile.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
        main()

        