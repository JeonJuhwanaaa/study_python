class Book:

    def __init__(self, bookId=0, bookName="", author="", publisher=""):
        self.bookId = bookId
        self.bookName = bookName
        self.author = author
        self.publisher = publisher

    def __str__(self):
        return f"""Book[
bookId: 1,
bookName: "혼자 공부하는 머신러닝+딥러닝",
author: "박해선",
publisher: "한빛미디어"]"""
    
    
if __name__ == "__main__":
    book = Book()
    print(book)