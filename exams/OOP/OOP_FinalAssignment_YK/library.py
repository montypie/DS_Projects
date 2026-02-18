from library_items import Book, EBook, AudioBook, PhysicalBook
from members import Member
from transactions import Transaction
import config
from utils import generate_id


class Library:
    def __init__ (self, name):
        self.name = name
        self.books = []
        self.members = []
        self.transactions = []

    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.books):
            raise StopIteration
        return self.books[self.__index]
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} has been added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member {member.name} has been added to the library.")

    def remove_book(self, isbn):
        for b in self.books:
            if b.get_id() == isbn:
                btitle = b.title
                self.books.remove(b)
                print(f"Book {btitle} has been removed from the library.")

    def remove_member(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                mname = m.name
                self.members.remove(m)
                print(f"Member {mname} has been removed from the library.")

    def find_book(self, isbn):
        """ Find and return book by ISBN (or None) """
        for b in self.books:
            if b.get_id() == isbn:
                return b

    def find_member(self, member_id):
        """ Find and return member by ID (or None) """
        for m in self.members:
            if m.member_id == member_id:
                return m

    def display_all_books(self):
        for b in self.books:
            b.display_info()

    def display_all_members(self):
        for m in self.members:
            m.display_info()

    def borrow_book(self, member_id, isbn, borrow_date):
        """ Borrowing actions """
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if not member or not member.can_borrow():
            print("No such member or the member cannot borrow!")
            return
        if not book or not book.available:
            print("No such book or the book is anavailable!")
            return
        t_id = generate_id("T")
        transaction = Transaction(t_id, member, book, borrow_date)
        self.transactions.append(transaction)
        member._Member__borrowed_books.append(book)
        book.borrow()
        print(f"The book {book.title} has been successfully borrowed by {member.name}")
        
    def return_book(self, member_id, isbn, return_date):
        """ Returning actions """
        for t in self.get_member_transactions(member_id):
            book = t.book
            if book.get_id() == isbn and not t.return_date:
                t.complete_return(return_date)
        member = self.find_member(member_id)
        member._Member__borrowed_books.remove(book)
        book.return_item()
        print(f"The book {book.title} has been successfully returned by {member.name}")

    def get_member_transactions(self, member_id):
        """ Returns the list of all transactions of a member """
        m_transactions = []
        for t in self.transactions:
            mem = t.member
            if mem.member_id == member_id:
                m_transactions.append(t)
        return m_transactions

    def get_active_transactions(self):
        """ Returns the list of all borrowed and not yet returned items """
        a_transactions = []
        for t in self.transactions:
            if not t.return_date:
                a_transactions.append(t)
        return a_transactions
    
    def available_books(self):
      for book in self.books:
          if book.available:
              yield book

    def books_by_author(self, author_name):
        for book in self.books:
            if book.author == author_name:
                yield book

    def books_by_type(self, book_type):
        for book in self.books:
            if book.__class__.__name__ == book_type:
                yield book

    def active_members(self):
        """ Members with borrowed books """
        for m in self.members:
            if m.borrowed_books:
                yield m



if __name__ == "__main__":
    # Test code voor dit specifieke module
    print("Testing library module...")