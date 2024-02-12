import json
from dataclasses import dataclass

@dataclass()
class Book:
    title: str
    author:str
    status:str

class LibraryDataBase:
    def __init__(self,file_path):
        self.file_path = file_path

    def __enter__(self):
        try:
            with open(self.file_path,"r") as file:
                self.data = json.load()
        except FileNotFoundError:
            self.data = {}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_path,"w") as file:
            json.dump(self.data,file,indent=4)

    def add_book(self,book):
        self.data['books'].append(book.__dict__)


book_to_add = Book("The NameSake","Jumpa Lahiri","avialable")

with LibraryDataBase("Library.json") as Library:
    Library.add_book(book_to_add)
