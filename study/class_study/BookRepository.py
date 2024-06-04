import pymysql
import pymysql.cursors

class BookRepository:

    host = "mysql-db.cnuqoeksywyf.ap-northeast-2.rds.amazonaws.com"
    port = 3306
    user = "aws"
    password = "1q2w3e4r!!"
    database = "library_db"

    @classmethod
    def saveBook(cls, book=None):
        connection = pymysql.connect(host=cls.host, port=cls.port, user=cls.user, password=cls.password, database=cls.database)

        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f'''
            insert into book_tb
            values (0,
                %s,
                %s,
                %s,
                %s,
                1, 
                4, 
                "http://test.com/test.png", 
                now(), 
                now()
            )
        '''
        cursor.execute(sql, (book.bookName, book.authorName, book.publisherName, book.isbn ))
        connection.commit()
    
    pass