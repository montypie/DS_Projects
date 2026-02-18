class BookCollection:

    def __init__(self, reverse = False):
        self.books = []
        self.reverse = reverse
    
    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.books):
            raise StopIteration
        if self.reverse:
            # yield from the end when reverse=True
            return self.books[len(self.books) - 1 - self.__index]
        return self.books[self.__index]

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]

    def add_book(self, book):
        self.books.append(book)
        
    def sort_by_title(self, reverse=False):
        """Sort the collection in-place by book.title (ascending by default)."""
        self.books.sort(key=lambda x: x.title, reverse=reverse)


if __name__ == "__main__":
    # Test code voor dit specifieke module
    print("Testing book_collection module...")