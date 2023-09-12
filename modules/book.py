from modules.library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, upc, subject, isbn, authors, dds_number):
        super().__init__(title, upc, subject)
        self.isbn = isbn
        self.authors = authors
        self.dds_number = dds_number