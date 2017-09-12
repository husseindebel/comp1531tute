import sqlite3

class LibraryModel(object):
    
    def search_author(self, author):
        query = "SELECT title, author, genre from Book where author = ?"
        payload = (author,)
        book_list = self._dbselect(query, payload)
        return book_list

    def search_all(self):
        query = "SELECT title, author from Book;"
        list_everything = self._dbselect(query)
        return list_everything
    

    def _dbselect(self, query, payload=()):
        connection = sqlite3.connect('library.db')
        con = connection.cursor()
        con.row_factory = sqlite3.Row

        cur = con.execute(query, payload)
        results = cur.fetchall()
        return results
