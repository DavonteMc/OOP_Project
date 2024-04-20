'''
Final Project: Classes
Description : This program will take a csv file - chosen by user - containing 
information on books within a libraries inventory.
    The user will be given options to view the libraries current inventory 
        Options include : 
            -Searching for a book
            -Borrowing a book
            -Returning a book
    The Librarian can modify the file by inputting a unique code into the standard options menu
        Librarian Opitons include :
            -Adding a book to the system
            -Removing a book from the system
            -Printing an inventory list
    The program contains basic checks to maintain value formatting and ranges
Made by : Devin Wheatley, Davonte Mclean, Warren Fernandez
'''

import os

MENU_HEADING = "Reader's Guild Library - Main Menu"
MENU_OPTIONS = {1 : 'Search for Books',
                2 : 'Borrow a book',
                3 : 'Return a book',
                0 : 'Exit the system'}
LIBR_MENU = "Reader's Guild Library - Librarian Menu"
LIBR_OPTIONS = {1 : 'Search for Books',
                2 : 'Borrow a book',
                3 : 'Return a book',
                4 : 'Add a book',
                5 : 'Remove a book',
                6 : 'Print catalog',
                0 : 'Exit the system'}

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
    
    '''
    Getter Methods : 
    Description : Method used to retrieve hidden attributes from outside of the class 
    Outcome : Returns the value stored within the corresponding attribute
    '''
    def get_isbn(self):
        return self.__isbn
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_genre(self):
        return self.__genre
    def get_availability_t_or_f(self):
        return self.__availability
    # get method returning genre name as a string
    def get_genre_name(self):
        return self.__GENRE[self.__genre]
    # get method returning availability (True = Available / False = Borrowed)
    def get_availability(self):
        return 'Available' if 'True' in self.__availability else 'Borrowed'
    
    '''
    Setter Methods : 
    Description : Method used to change the value of hidden attributes from outside of the class
    Outcome : Sets a new value the corresponding attribute
    '''
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
        self.__availability = 'False\n'
    # set method for returning a book - Availability == True
    def return_it(self):
        self.__availability = 'True\n'
    # returns a formatted string - ISBN, Title, Author, Genre, Availability
    def __str__(self):
        return '{:<15}{:<26}{:<26}{:<21}{:<10}'.format(self.get_isbn(),self.get_title(),self.get_author(),self.get_genre_name(),self.get_availability())

'''
Function Name : print_menu
Description : Displays a menu to the user
Outcome : Displays the given menu and then prompts the user for their selection
The function uses 3 checks to verify the user's input. Checks: ([input between 3 and 0],[input of 2130],[input between 6 and 0])
-If the user inputs 2130 then it will print a admin menu with additional editing priviledges
-If an invalid entry in entered, the message "Invalid option" will be presented and the user will be asked to input a valid entry
Valid inputs are returned
'''
def print_menu(librarian_menu):
    if librarian_menu == False:
        print(MENU_HEADING + '\n' + ('=' * 34)) 
        for k,v in MENU_OPTIONS.items():
            print(f'{k}. {v}')
        check = False
        while check == False:
            uSelection = input('Enter your selection: ')
            if uSelection.isnumeric():
                uSelection = int(uSelection)
                if uSelection <= 3 and uSelection >= 0:
                    print()
                    check = True
                    return uSelection
                elif uSelection == 2130:
                    librarian_menu = True
                    check = True
            if check == False:
                print('Invalid Input')
                
    if librarian_menu == True:
        print()
        print(LIBR_MENU + '\n' + ('=' * 39)) 
        for k,v in LIBR_OPTIONS.items():
            print(f'{k}. {v}')

        check = False
        while check == False:
            uSelection = input('Enter your selection: ')
            if uSelection.isnumeric():
                uSelection = int(uSelection)
                if uSelection <= 6 and uSelection >= 0:
                    print()
                    check = True
                    return uSelection
            if check == False:
                print('Invalid Input')

'''
Function Name : search_books
Description : Function uses a keyword inputted from the user to search the inventory file for books containing the keyword in 
its [Title, Author, Genre]
Outcome : Creates a list called found_books, iterates over the current inventory list
If there are books that match with the keyword, it is added to the found_books list and then that list 
is formatted and presented to the user. 
If there are no books that match the keyword, it returns the message "No matching books found." 
'''
def search_books(search_val):
    load_books()

    found_books = []
    counter = 0
    while counter < len(bookshelf):
        if (search_val.lower() in bookshelf[counter].get_title().lower() or 
            search_val.lower() in bookshelf[counter].get_author().lower() or 
            search_val.lower() in bookshelf[counter].get_genre_name().lower()):
            found_books.append(bookshelf[counter])
        counter += 1
    
    if found_books: # If the list is empty = False -> else  If the list has items = True -> return
        print('{:<15}{:<26}{:<26}{:<21}{:<10}'.format('ISBN','Title','Author','Genre','Availability'))
        print('{:<15}{:<26}{:<26}{:<21}{:<20}'.format('-'*14,'-'*25,'-'*25,'-'*20,'-'*12))
        for book in found_books:
            print(book)
    else:
        print('No matching books found.')
    print()

'''
Function Name : search_str
Description : Displays the header for the search_books funciton and retrieves user selection
Outcome : Displays the search_books, prompts the user for their selection, and returns that selection
'''
def search_str():
    load_books()

    print('- - Search for books -- ')
    while True:
        search = input('Enter search value: ')
        if search.isalpha() == True:
            return search
        else:
            print('Invalid Input')

'''
Function Name : load_books
Description : Opens CSV file and formats it into an iterable list
Parameters : file_contents_list : list containing each book and their information
Outcome : Creates an iterable list of each book, and turns each book into a member of the Book class
          Returns the number of books
'''
def load_books():

    file = open('books.csv','r+')
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

'''
Function Name : borrow_book
Description : Finds book via ISBN number & changes availability from True to False
Parameters : flag
                True = Book has been found & borrowed
                False = Book ISBN has no match
Outcome : Changes matching book's availability from True to False -- or -- prints fallback statement
'''
def borrow_book():
    load_books()

    print('- - Borrow a book -- ')
    borrow_isbn = input('Enter the 13-digit ISBN (format 999-9999999999) : ')

    flag = False
    for book in bookshelf:
        if borrow_isbn == book.get_isbn():
            if 'True' in book.get_availability_t_or_f():
                book.borrow_it()
                print(f'\'{book.get_title()}\' with ISBN {borrow_isbn} successfully borrowed.\n')
            elif 'False' in book.get_availability_t_or_f():
                print(f'\'{book.get_title()}\' with ISBN {borrow_isbn} is not currently available.\n')
            flag = True
    if flag == False:
        print(f'No book with ISBN {borrow_isbn} found\n')

    save_books()

'''
Function Name : return_book
Description : Finds book via ISBN number & changes availability from False to True
Parameters : flag
                True = Book has been found & returned
                False = Book ISBN has no match
Outcome : Changes matching book's availability from False to True -- or -- prints fallback statement
'''
def return_book():
    load_books()

    print('- - Return a book -- ')
    return_isbn = input('Enter the 13-digit ISBN (format 999-9999999999) : ')

    flag = False
    for book in bookshelf:
        if return_isbn == book.get_isbn():
            if 'True' in book.get_availability_t_or_f():
                print(f'\'{book.get_title()}\' with ISBN {return_isbn} is not currently borrowed.\n')
            elif 'False' in book.get_availability_t_or_f():
                book.return_it()
                print(f'\'{book.get_title()}\' with ISBN {return_isbn} successfully returned.\n')
            flag = True
    if flag == False:
        print(f'No book with ISBN {return_isbn} found\n')
    
    save_books()

'''
Function Name : find_book_by_isbn
Description : Finds book via ISBN number
Parameters : flag
                True = Book has been found
                False = Book ISBN has no match
Outcome : Returns index # of matching book -- or -- prints fallback statement & returns -1
'''
def find_book_by_isbn():
    find_isbn = input('Enter ISBN : ')

    counter = 0
    flag = False
    # stops when ISBN matches or when every book has been iterated through
    while flag == False and counter < len(bookshelf):
        for book in bookshelf:
            if find_isbn == bookshelf[counter].get_isbn():
                flag = True
                # returns index of matching book
                return counter
            counter+=1
    # returns -1 if not found
    if flag == False:
        print(f'No book with ISBN {find_isbn} found')
        return -1

'''
Function Name : add_books
Description : Adds new book to bookshelf
Parameters :
    add_isbn : takes input for new book's ISBN number
    add_title : takes input for new book's title
    add_author : takes input for new book's author
    add_genre : takes input for new book's genre
Outcome : Adds new book to bookshelf with inputted ISBN, Title, Author, and Genre
'''
def add_books():
    load_books()

    print('- - Add a book -- ')
    # recieve inputs for ISBN, title, and author of book being added
    add_isbn = input('Enter ISBN : ')
    add_title = input('Enter Title : ')
    add_author = input('Enter Author : ')

    # recieve input for added book's genre, checks that it matches one from our genre dictionary
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
                print('Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, Young Adult, Children\'s Fiction, Self-help, Fantasy, Historical Fiction, Poetry')
    # adds book to the bookshelf
    book = Book(add_isbn,add_title,add_author,add_genre,'True')
    bookshelf.append(book)
    print(f'\'{book.get_title()}\' with ISBN {add_isbn} successfully added.\n')

    save_books()

'''
Function Name : remove_book
Description : Receives book list. Searches for the book via isbn in the bookshelf. If isbn exists, book is removed from the booshelf
Parameters :
    remove_isbn : Receives an isbn number and searches through the bookshelf to see if book is present
Outcome : Removes book from bookshelf
'''
def remove_book():
    load_books()

    print('- - Remove a book -- ')
    remove_index = find_book_by_isbn()
    if remove_index != -1:
        print(f'\'{bookshelf[remove_index].get_title()}\' with ISBN {bookshelf[remove_index].get_isbn()} successfully removed.\n')
        del bookshelf[remove_index]
    
    save_books()
'''
Function Name : print_books
Description : Prints out book information such as ISBN, Title, Author, Genre and Availability in string format
Outcome : Searches for the book in bookshelf and if present will print out all information in a string format
'''
def print_books():
    load_books()

    print('- - Print book catalog -- ')
    print('{:<15}{:<26}{:<26}{:<21}{:<10}'.format('ISBN','Title','Author','Genre','Availability'))
    print('{:<15}{:<26}{:<26}{:<21}{:<20}'.format('-'*14,'-'*25,'-'*25,'-'*20,'-'*12))
    for book in bookshelf:
        print(book)
    print()

'''
Function Name : save_books
Description : Receives a book list and pathname to boooks.csv. Iterates over the list, formatting a comma separated string containing each book's attribute values
             writes each string as a separate line to the file and returns number of books saved to the file
Outcome : Overwrites existsing file in bookshelf with the new information
'''
def save_books():
    with open('books.csv','w') as file:
        for book in bookshelf:
            saved_text = f'{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{book.get_availability_t_or_f()}'
            if saved_text.endswith('\n'):
                file.write(saved_text)
            else: 
                saved_text = f'{saved_text}\n'
                file.write(saved_text)


def main():
    # check that file exists
    file_name = input('Starting the system ...\nEnter book catalog filename: ')
    while os.path.isfile(file_name) == False:
        # exits program if file_input not found in current directory
        file_name = input('File not found. Re-enter book catalog filename : ')
    print('Book catalog has been loaded.\n')

    librarian_menu = False
    while True:
        match print_menu(librarian_menu):
            case 1:
                search_books(search_str())
            case 2:
                borrow_book()
            case 3:
                return_book()
            case 4:
                add_books()
                librarian_menu = True
            case 5:
                remove_book()
                librarian_menu = True
            case 6:
                print_books()
                librarian_menu = True
            case 0:
                print('--- Exit the system ---\nBook catalog has been saved\nGood Bye!')
                exit()
            case _:
                print('Invalid Input.\n')

main()
