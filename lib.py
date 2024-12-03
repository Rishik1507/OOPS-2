class library():
    def __init__(self,books):
        self.books=books

    def show_books(self):
        print("The available books are:-")
        for book in self.books:
            print(book)
        print()
    def lend_books(self,book_lend):
        if isinstance(book_lend,list):
            for book in book_lend:
                if book in self.books:
                    self.books.remove(book)
                    print(f'You have successfully borrowed {book}')

                else:
                
                    print("The book is not available")
        else:
             if book_lend in self.books:
                    self.books.remove(book_lend)
                    print(f'You have successfully borrowed {book_lend}')
             else:

         
        
                
                print("The book is not available")

    def return_books(self,book):
        if book in self.books:
            print("The book is already available")
        else:
            self.books.append(book)
            print(f'You have successfully returned {book}')
    def add_books(self,book):
        self.books.append(book)
        print(f'You have added {book} in the collection')
    def __del__(self):
        print("Library closed")
lib=library(["sherlock holmes","percy jackson","harry potter"])
lib.lend_books(["harry potter","sherlock holmes"])
lib.show_books()

            
        
        
    
    
        