# Part 1

class Book:
    def __init__(self, isbn, title, author, genre, avail):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__avail = bool(avail)
        self.__GENRES = {
                0 : 'Romance',
                1 : 'Mystery',
                2 : 'Science Fiction',
                3 : 'Thriller',
                4 : 'Young Adult',
                5 : "Children's Fiction",
                6 : 'Self-help',
                7 : 'Fantasy',
                8 : 'Historical Fiction',
                9 : 'Poetry'}

    def get_isbn(self):
        return self.__isbn
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_genre(self):
        return self.__genre
    def get_avail(self):
        return self.__avail
    def get_genre_name(self):
        return self.__GENRES[self.__genre]
    

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn
    
    def set_title(self, new_title):
        self.__title = new_title
    
    def set_author(self, new_author):
        self.__author = new_author
    
    def set_genre(self, new_genre):
        self.__genre = new_genre
    
    def get_availability(self):
        if self.__avail == True:
            return 'Available'
        else:
            return 'Borrowed'
        
    def borrow_it(self):
        self.__avail = False

    def return_it(self):
        self.__avail = True

    def __str__(self):
        return '{:<15}{:<26}{:<26}{:<21}{:<10}'.format(Book.get_isbn(self),Book.get_title(self),Book.get_author(self),Book.get_genre_name(self),Book.get_availability(self))

MENU_HEADING = "Reader's Guild Library - Main Menu"
MENU_OPTIONS = {1 : 'Search for Books',
                2 : 'Borrow a book',
                3 : 'Return a book',
                0 : 'Exit the system'}

def print_menu(MENU_HEADING, MENU_OPTIONS):
    print(MENU_HEADING + '\n' + ('=' * 34))
    for k,v in MENU_OPTIONS.items():
        print(f'{k}. {v}')
    check = True
    while check == True:
        uSelection = int(input('Enter your selection: ')) 
        if uSelection > 3 or uSelection < 0:
            check = True
        else: 
            check = False
            return uSelection
