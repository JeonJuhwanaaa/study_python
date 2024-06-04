from BookService import BookService
from BookEntity import Book

 # 파이썬 생성자 / 함수의 매개변수 첫번째는 항상 self 가 들어간다 고정 / 두번째 매개변수부터가 실제 사용 매개변수 / # self = this
class BookController:
        
        @classmethod
        def addBookRequest(cls):
            book = Book(bookName="테스트 도서명", authorName="테스트 저자명", publisherName="테스트 출판사명", isbn="1234")
            BookService.addBook(book)