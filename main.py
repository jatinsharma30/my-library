#my library
class Library:
    def __init__(self,library,books):
        self.library=library
        self.books=books
        self.lbooks=dict()
        
        
    def displaybooks(self):
        print(f"books in {self.library} are:")
        for book in self.books:
            print(book)
        if self.lbooks!={}:
            for key in self.lbooks:
                print(f"Book {key} is lended by {self.lbooks[key]} ")
    
    def lendbooks(self,bookname,name):
        
        if bookname.lower() in self.books:
            self.lbooks[bookname]=name
            self.books.remove(bookname)
            return "done"
        
        elif bookname in self.lbooks:
            return f"this books has already taken by {self.lbooks[bookname]}"
       
        else:
            return f"book not found available books are: {self.books}"
    
    
    def addbook(self,bookname,name):
        self.books.append(bookname.lower())
        return f"thank you {name} for {bookname}"
    
    
    def returnbook(self,bookname):
        if self.lbooks=={}:
            return "there is no book to be returned"
        
        elif bookname.lower() in self.lbooks: 
            del self.lbooks[bookname]
            self.books.append(bookname)
            return f"book returned"
        
        else:
            return f"{bookname} not found"
        
jatin=Library("jatin",["harry potter","inception","dark knight"])   
def main():
    ch="y"            
    while ch.lower()=="y":
        n=int(input("enter 1 to display book, 2 to lendbooks, 3 to add a book to library, 4 to return book "))
        
        if n==1:
            jatin.displaybooks()
    
        elif n==2:
            name=input("enter your name ")
            bookname=input("enter book name ")
            print(jatin.lendbooks(bookname,name))
    
        elif n==3:
            name=input("enter your name ")
            bookname=input("enter book name ")
            print(jatin.addbook(bookname,name))
    
        elif n==4:
            bookname=input("enter book name ")
            print(jatin.returnbook(bookname))
        
        else:
            print("enter valid option")
            continue
        
        ch=input("enter y to continue and enter any key to exit")
        
if __name__=="__main__":
    main()
