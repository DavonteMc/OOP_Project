'''
OOP Final Project: Classes 
Descritption: This program will read a Books csv file containing a book's Isbn, Title, Author's name, Genre, Availability
    The user will be given several options to acccess and alter various entries of the file
    Options include: 
        Searching for books in the existing library 
        Borrowing books from the library, affecting their availability
        Returning books to the library affetcing their availability 
        Adding books to the existing library 
        Removing books from the existing library 
        Prinitng out a list of books that are present in the library 
    The program contains basic checks to maintain formatting and ranges
Program was made by Davonte Mclean, Devin Wheatley and Warren Fernandes 
'''
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
        self.__availability = 'False'
    # set method for returning a book - Availability == True
    def return_it(self):
        self.__availability = 'True'
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

def borrow_book():
    borrow_isbn = input('Enter ISBN : ')

    counter = 0
    flag = False
    for book in bookshelf:
        if borrow_isbn == bookshelf[counter].get_isbn():
            bookshelf[counter].borrow_it()
            flag = True
        counter+=1
    if flag == False:
        print(f'No book with ISBN {borrow_isbn} found')
    
def return_book():
    return_isbn = input('Enter ISBN : ')

    counter = 0
    flag = False
    for book in bookshelf:
        if return_isbn == bookshelf[counter].get_isbn():
            bookshelf[counter].return_it()
            flag = True
        counter+=1
    if flag == False:
        print(f'No book with ISBN {return_isbn} found')

def find_book_by_isbn():
    find_isbn = input('Enter ISBN : ')

    counter = 0
    flag = False
    # stops when ISBN matches or when every book has been iterated through
    while flag == False and counter <  len(bookshelf):
        for book in bookshelf:
            if find_isbn == bookshelf[counter].get_isbn():
                flag = True
                # returns index of matching book
                return counter
            counter+=1
    # returns -1 if not found
    if flag == False:
        print(f'No book with ISBN {find_isbn} found')
        return '-1'

def add_books():
    add_isbn = input('Enter ISBN : ')
    add_title = input('Enter Title : ')
    add_author = input('Enter Author : ')

    while True:
        add_genre = input('Enter Genre : ')

        match add_genre:
            case 'Romance':
                add_genre = 0
                break
            case 'Mystery':
                add_genre = 1
                break
            case 'Science Fiction':
                add_genre = 2
                break
            case 'Thriller':
                add_genre = 3
                break
            case 'Young Adult':
                add_genre = 4
                break
            case 'Children\'s Fiction':
                add_genre = 5
                break
            case 'Self-help':
                add_genre = 6
                break
            case 'Fantasy':
                add_genre = 7
                break
            case 'Historical Fiction':
                add_genre = 8
                break
            case 'Poetry':
                add_genre = 9
                break
            case _:
                print('Invalid Input')

    book = Book(add_isbn,add_title,add_author,add_genre,'True')
    bookshelf.append(book)

'''
Function name: Remove_book()
Description: Receives book list. Searches for the book via isbn in the bookshelf. If isbn exists, book is removed from the booshelf
Parameters: Find_book_by_isbn(): Receives an isbn number and searches through the bookshelf to see if book is present
Outcome: Removes book from bookshelf
'''
def remove_book():
    remove_isbn = find_book_by_isbn()
    if remove_isbn != -1:
        del bookshelf[remove_isbn]
'''
Function name: print_books()
Description: Prints out book information such as ISBN, Title, Author, Genre and Availability in string format
Outcome: Searches for the book in bookshelf and if present will print out all information in a string format
'''
def print_books():
    print('{:<15}{:<26}{:<26}{:<21}{:<10}'.format('ISBN','Title','Author','Genre','Availability'))
    for book in bookshelf:
        print(book)
'''
Function name: save_books()
Description: Receives a book list and pathname to boooks.csv. Iterates over the list, formatting a comma separated string containing each book's attribute values
             writes each string as a separate line to the file and returns number of books saved to the file
Outcome: Overwrites existsing file in bookshelf with the new information
'''
def save_books():
    with open('books.csv','r+') as file:
        saved_text = ''
        for book in bookshelf:
            saved_text = f'{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{book.get_availability_t_or_f()}'
            file.write(saved_text)




