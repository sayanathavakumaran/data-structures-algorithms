class LibraryBook():
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True

    def get_title(self):
            return self.title
    def get_author(self):
            return self.author
    def set_is_available(self,is_available):
            self.is_available = is_available
    def get_is_available(self):
           return self.is_available

    def borrow_book(self,title):
            if self.is_available == True:
                self.is_available = False
                print(f"You borrowed {title}")
            else:
                print(f"Sorry {title} is already borrowed")

    def return_book(self,title):
          self.is_available = True

hp = LibraryBook("harry potter","jk rowling")
twi = LibraryBook("twilight","author")
twi.borrow_book("twilight")
twi.borrow_book("twilight")
twi.return_book("twilight")
twi.borrow_book("twilight")