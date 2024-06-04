class Book:
    # bookId = 100
    # bookName = "테스트 도서"          # 파이썬에서는 멤버변수 사용하지 않는다 / 스테틱변수 / self 안에 정의한다

    def __init__(self, bookId=0, bookName="", authorName="", publisherName="", isbn=""):
        self.bookId = bookId
        self.bookName = bookName
        self.authorName = authorName
        self.publisherName = publisherName
        self.isbn = isbn

    def setAuthor(self, author):
        self.author = author

    def __str__(self):
        return f"""Book[
bookId: {self.bookId},
bookName: {self.bookName},
authorName: {self.authorName},
publisherName: {self.publisherName}]"""
        # return "Book[bookId: {0}, bookName: {1}]".format(self.bookId, self.bookName)
        # return "Book[bookId: {bookId}, bookName: {bookName}]".format(bookId = self.bookId, bookName = self.bookName)
        # print("Book[bookId: %d, bookName: %s", self.bookId, self.bookName)