from datetime import datetime
import config

class Transaction:
    def __init__(self, transaction_id, member, book, borrow_date="", return_date=""):
        self.transaction_id = transaction_id
        self.member = member
        self.book = book
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.is_returned = False

    def complete_return(self, return_date):
        self.return_date = return_date
        self.is_returned = True

    def display_transaction(self):
        info = f"Book {self.book.title} by {self.book.author} is"
        if self.is_returned == True:
            info += f" returned on {self.return_date}"
        else:
            info += f" borrowed on {self.borrow_date}"
        return info

    def calculate_days(self):
        date_format = "%Y-%m-%d"
        borrowed = datetime.strptime(self.borrow_date, date_format)
        returned = datetime.strptime(self.return_date, date_format)
        return returned - borrowed
    
    def calculate_late_fee(self):
        days_borrowed = self.calculate_days().days
        if days_borrowed > config.MAX_BORROW_DAYS:
            late_days = days_borrowed - config.MAX_BORROW_DAYS
            return late_days * config.LATE_FEE_PER_DAY
        else:
            return 0


if __name__ == "__main__":
    # Test code voor dit specifieke module
    print("Testing transactions module...")