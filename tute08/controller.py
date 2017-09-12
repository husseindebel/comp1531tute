from model import LibraryModel
from view import LibraryView

class LibraryController(object):
    def __init__(self):
        self.model = LibraryModel()
        self.view = LibraryView()

    def search_author(self, author):
        book_list = self.model.search_author(author)
        return self.view.print_author(book_list, author)
