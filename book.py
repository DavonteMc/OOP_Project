class Book():
    def __init__(self, isbn, title, author, genre, availability) -> None:
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__availability = availability
        self.__GENRE = {
            0:'Romance',
            1:'Mystery',
            2:'Science Fiction',
            3:'Thriller',
            4:'Young Adult',
            5:'Children\'s Fiction',
            6:'Self-help',
            7:'Fantasy',
            8:'Historical Fiction',
            9:'Poetry'}
    
    # get methods
    def get_isbn(self):
        return self.__isbn
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_genre(self):
        return self.__genre
    # get method returning genre name as a string
    def get_genre_name(self):
        return self.__GENRE[self.__genre]
    # get method returning availability (True = Available / False = Borrowed)
    def get_availability(self):
        return 'Available' if 'True' in self.__availability else 'Borrowed'
    
    # set methods
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn
    def set_title(self, new_title):
        self.__title = new_title
    def set_author(self, new_author):
        self.__author = new_author
    def set_genre(self, new_genre):
        self.__genre = new_genre
    # set method for borrowing a book - Availability == False
    def borrow_it(self):
        self.__availability = False
    # set method for returning a book - Availability == True
    def return_it(self):
        self.__availability = True
    # returns a formatted string - ISBN, Title, Author, Genre, Availability
    def __str__(self):
        return '{:<15}{:<26}{:<26}{:<21}{:<10}'.format(self.get_isbn(),self.get_title(),self.get_author(),self.get_genre_name(),self.get_availability())
    
def load_books():
    with open('books.csv','r+') as file:
        # creates a list with each item containing a book - [ISBN,Title,Author,Genre,Availability]
        file_contents_list = file.readlines()

        global bookshelf
        bookshelf = []
        
        book_number = 0
        # iterates over the list and adds each book as an object into the bookshelf list
        for book in file_contents_list:
            # splits the book elements into seperate values
            file_contents_list[book_number] = file_contents_list[book_number].split(',')
            book = Book(file_contents_list[book_number][0],file_contents_list[book_number][1],file_contents_list[book_number][2],file_contents_list[book_number][3],file_contents_list[book_number][4])
            bookshelf.append(book)
            book_number+=1
        return(book_number)
