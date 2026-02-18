from copy import deepcopy
from datetime import datetime
from interfaces import Searchable
import config


class Member(Searchable):
    def __init__(self, name, memeber_id, email):
        self.name = name
        self.member_id = memeber_id
        self.email = email
        self.__borrowed_books = []

    @property
    def max_books(self):
        return config.DEFAULT_MAX_BOOKS

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self.__email = new_email
        else:
            print(f"Error: email must contain @")

    @property
    def borrowed_books(self):
        return deepcopy(self.__borrowed_books)

    def display_info(self):
        info = f"Member: {self.name}, id: {self.member_id}, email: {self.email}"
        print(info)

    def get_borrowed_count(self):
        return len(self.borrowed_books)
    
    def can_borrow(self):
        if len(self.borrowed_books) < self.max_books:
            return True
        else:
            return False
        
    def get_search_keywords(self):
        return [self.name, self.member_id, self.email]

    def matches_search(self, search_term: str) -> bool:
        term = search_term.casefold()
        for kw in self.get_search_keywords():
            if kw and term in str(kw).casefold():
                return True
        return False

    
class StudentMember(Member):
    def __init__(self, name, member_id, email, student_id, university):
        super().__init__(name, member_id, email)
        self.student_id = student_id
        self.university = university

    @property
    def max_books(self):
        return config.STUDENT_MAX_BOOKS

    def display_info(self):
        super().display_info()
        print(f"{' '*8}student_id: {self.student_id}, university: {self.university}")


class PremiumMember(Member):
    def __init__(self, name, member_id, email, membership_expiry):
        super().__init__(name, member_id, email)
        self.membership_expiry = membership_expiry

    @property
    def max_books(self):
        return config.PREMIUM_MAX_BOOKS

    def is_expired(self):
        today = datetime.today().strftime('%Y-%m-%d')
        if self.membership_expiry <= today:
            return True
        else:
            return False

    def display_info(self):
        super().display_info()
        print(f"{' '*8}premium membership until: {self.membership_expiry}")

    def can_borrow(self):
        if self.get_borrowed_count() < self.max_books and not self.is_expired():
            return True
        else:
            return False


if __name__ == "__main__":
    # Test code voor dit specifieke module
    print("Testing members module...")