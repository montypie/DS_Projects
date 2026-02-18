from datetime import datetime
from abc import ABC, abstractmethod
from interfaces import Searchable

class LibraryItem(ABC):

    @abstractmethod
    def display_info(self):
        """ Library item info """
        pass

    @abstractmethod
    def get_type(self):
        """ Type of a library item """
        pass

    @abstractmethod
    def borrow(self):
        """ Borrowing logic """
        pass

    @abstractmethod
    def return_item(self):
        """ Returning logic """
        pass

    def get_id(self):
        return getattr(self, "isbn", None)
    

class Book(LibraryItem, Searchable):

    def __init__(self, title, author, isbn, publication_year):
        super().__init__()
        self.__isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.__available = True
    
    @property
    def isbn(self):
        return self.__isbn

    @property
    def publication_year(self):
        return self.__publication_year
    
    @property
    def available(self):
        return self.__available
    
    @available.setter
    def available(self, status):
        if isinstance(status, bool):
            self.__available = status
        else:
            print(f"Error: availability status must be True or False")
    
    @publication_year.setter
    def publication_year(self, year):
        today = datetime.today()
        if year >= 1000 and year <= today.year:
            self.__publication_year = year
        else:
            self.__publication_year = None
            print(f"Error: year must be between 1000 and {today.year}")

    def display_info(self):
        info = f"Book: '{self.title}' by {self.author}, id: {super().get_id()}, published in {self.publication_year}"
        print(info)

    def borrow(self):
        if self.__available == True:
            self.__available = False
        else:
            print("Warning: the book is unavailable")

    def return_item(self):
        self.__available = True

    def get_search_keywords(self):
        return [self.title, self.author, self.get_id()]
    
    def matches_search(self, search_term: str) -> bool:
        term = search_term.casefold()
        for kw in self.get_search_keywords():
            if kw and term in str(kw).casefold():
                return True
        return False


class EBook(Book):
    def __init__(self, title, author, isbn, publication_year, file_size, format):
        super().__init__(title, author, isbn, publication_year)
        self.file_size = file_size
        self.format = format
        self.download_count = 0

    def display_info(self):
        super().display_info()
        print(f"{' '*6}file_size: {self.file_size}, format: {self.format}")

    def download(self):
        print(f"'{self.title}' had been downloaded")

    def borrow(self):
        super().borrow()
        self.download_count += 1

    def get_type(self):
        return "EBook"
    
        
class AudioBook(Book):
    def __init__(self, title, author, isbn, publication_year, narrator, duration_minutes):
        super().__init__(title, author, isbn, publication_year)
        self.narrator = narrator
        self.duration_minutes = duration_minutes
        self.play_count = 0

    def display_info(self):
        super().display_info()
        print(f"{' '*6}narrator: {self.narrator}, duration: {self.duration_minutes}")

    def play(self):
        print(f"'{self.title}' is playing now")

    def borrow(self):
        super().borrow()
        self.play_count += 1
    
    def get_type(self):
        return "AudioBook"
    
    
class PhysicalBook(Book):
    def __init__(self, title, author, isbn, publication_year, shelf_location, condition):
        super().__init__(title, author, isbn, publication_year)
        self.shelf_location = shelf_location
        self.condition = condition

    def display_info(self):
        super().display_info()
        print(f"{' '*6}location: {self.shelf_location}, condition: {self.condition}")

    def get_type(self):
        return "PhysicalBook"
     

if __name__ == "__main__":
    # Test code voor dit specifieke module
    print("Testing library_items module...")