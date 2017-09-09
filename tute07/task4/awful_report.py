from abc import abstractmethod
"""
Bad SRP: All responsibilities together
Bad OCP: Close for extention, require for modification
"""

class Reporter(object):

    def read_db(self, db, type):
        if type == "MySQL":
            print("Reading db MySQL Now")
        elif type == "SQLite":
            print("Reading db SQLite Now")
        elif type == "CSV":
            print("Reading db CSV Now")
        elif type == "SQLAlchemy":
            print("Reading db SQLAlchemy Now")
        else: print("DB type not recognised")

    def format_report(self, data, type):
        if type == "PDF":
            print("Writing data into PDF format")
        elif type == "HTML":
            print("Writing data into HTML format")
        elif type == "Word":
            print("Writing data into Word format")
        elif type == "TXT":
            print("Writing data into TXT format")
        else: print("Format type not recognised")
