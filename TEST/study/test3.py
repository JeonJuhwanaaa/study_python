class BookDict:

    host = "localhost"
    port = 3306
    user = "admin"
    password = "1234"
    database = "book_db"

    @classmethod
    def saveBook(cls, book=None):
        connection = pymysql.connect(host=cls.host, port=cls.port, user=cls.user, password=cls.password, database=cls.database)

        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f'''
            insert into book_tb(book_id, book_name, author, publisher)
            values (0, "Hey, 파이썬! 생성형 AI 활용 앱 만들어 줘", "김한호, 최태온, 윤택한", "성안당")
        '''
        cursor.execute(sql, (book.bookName, book.author, book.publisher))
        connection.commit()
    
    pass