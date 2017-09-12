class LibraryView(object):
    def print_author(self, book_list, author):
        print("###### printing authors books ######")
        print(author, "books")
        for row in book_list:
            print(row['title'], row['author'])
        print("####### end printing authors books ######")
