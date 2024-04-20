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

MAIN_MENU = "Reader's Guild Library - Main Menu"
MAIN_OPTIONS = {1 : 'Search for Books',
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
'''
Class Name : Book
Description : Creates an object for books within a library
Attributes : A book's [ISBN, Title, Author, Genre, Availabiity]
There is a class constant that houses the Genre Categories that a book can be a part of
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
        self.__availability = 'False'
    # set method for returning a book - Availability == True
    def return_it(self):
        self.__availability = 'True'
    # returns a formatted string - ISBN, Title, Author, Genre, Availability
    def __str__(self):
        return '{:<15}{:<26}{:<26}{:<21}{:<10}'.format(self.get_isbn(),self.get_title(),self.get_author(),self.get_genre_name(),self.get_availability())
'''
Function Name : load_books
Description : Retrieves the inventory list from the given csv file and copies that information into a usable list
Outcome : Creates a list with each item containing a book - [ISBN,Title,Author,Genre,Availability]
-Iterates over the list and adds each book as an object into the bookshelf list
-Splits the book elements into seperate values
'''
def load_books(bookshelf, file_name):
    with open(file_name,'r+') as file:
        file_contents_list = file.readlines()
        book_number = 0
        for book in file_contents_list:
            file_contents_list[book_number] = file_contents_list[book_number].split(',')
            book = Book(file_contents_list[book_number][0],file_contents_list[book_number][1],file_contents_list[book_number][2],file_contents_list[book_number][3],file_contents_list[book_number][4])
            bookshelf.append(book)
            book_number+=1
        return(book_number)
'''
Function Name : print_menu
Description : Displays a menu to the user
Outcome : Displays the given menu and then prompts the user for their selection
The function uses 3 checks to verify the user's input. Checks: ([input between 3 and 0],[input of 2130],[input between 6 and 0])
-If the user inputs 2130 then it will print a admin menu with additional editing priviledges
-If an invalid entry in entered, the message "Invalid option" will be presented and the user will be asked to input a valid entry
Valid inputs are returned
'''
def print_menu(MENU_HEADING, MENU_OPTIONS):
    print()
    print(MENU_HEADING + '\n' + ('=' * 34)) 
    for k,v in MENU_OPTIONS.items():
        print(f'{k}. {v}')
    check = False
    while check == False:
        menu_selection = input('Enter your selection: ')
        if menu_selection.isnumeric() == False:
            print('Invalid option')
            check = False
        else:
            menu_selection = int(menu_selection)
            if menu_selection <= 3 and menu_selection >= 0:
                check = True
                return menu_selection
            elif menu_selection == 2130:
                print(LIBR_MENU + '\n' + ('=' * 39)) 
                for k,v in LIBR_OPTIONS.items():
                    print(f'{k}. {v}')
                check = False
                while check == False:    
                    menu_selection = int(input('Enter your selection: ')) 
                    if menu_selection <= 6 or menu_selection >= 0: #len()
                        check = True
                        return menu_selection
                    else: 
                        print('Invalid option')
                        check = False
            else:
                print('Invalid option')
                check = False
'''
Function Name : search_str
Description : Displays the header for the search_books funciton and retrieves user selection
Outcome : Displays the search_books, prompts the user for their selection, and returns that selection
'''
def search_str():
    print()
    print('- - Search for books -- ')
    search = input('Enter search value: ')
    return search
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
    found_books = []
    counter = 0
    while counter < len(bookshelf):
        if (search_val.lower() in bookshelf[counter].get_title().lower() or 
            search_val.lower() in bookshelf[counter].get_author().lower() or 
            search_val.lower() in bookshelf[counter].get_genre_name().lower()):
            found_books.append(bookshelf[counter])
        counter += 1
    
    if found_books: # If the list is empty = False -> else  If the list has items = True -> return
        counter = 0
        print('{:<15}{:<26}{:<26}{:<21}{}'.format('ISBN','Title','Author','Genre','Availability'))
        print(('-'*14), ('-'*25), ('-'*25), ('-'*20), ('-'*12))
        for book in found_books:
            print('{:<15}{:<26}{:<26}{:<21}{}'.format(book.get_isbn(), book.get_title(), book.get_author(), book.get_genre_name(), book.get_availability()))
            counter += 1
    else:
        print('No matching books found.')

def borrow_book():
    print('- - Borrow a book -- ')
    borrow_isbn = input('Enter the 13-digit ISBN (format 999-9999999999): ')
    result = find_book_by_isbn(borrow_isbn)
    if result != -1:
        if bookshelf[result].get_availability() == 'Available':
            bookshelf[result].borrow_it()
            print(f"'{bookshelf[result].get_title()}' with ISBN {borrow_isbn} successfully borrowed.")
        else:
            print(f"'{bookshelf[result].get_title()}' with ISBN {borrow_isbn} is not currently available.")
    else:
        print(f'No book found with that ISBN.')

def find_book_by_isbn(borrow_isbn):
    counter = 0
    flag = False
    # stops when ISBN matches or when every book has been iterated through
    while flag == False and counter < len(bookshelf):
        for book in bookshelf:
            if borrow_isbn == bookshelf[counter].get_isbn():
                # returns index of matching book
                return counter
            counter+=1
        # returns -1 if not found
        return -1

def return_book():
    return_isbn = input('Enter the 13-digit ISBN (format 999-9999999999): ')
    counter = 0
    flag = False
    for book in bookshelf:
        if return_isbn == bookshelf[counter].get_isbn():
            bookshelf[counter].return_it()
            flag = True
            print(f"'{bookshelf[counter].get_title()}' with ISBN {return_isbn} successfully borrowed.")
        counter+=1
    if flag == False:
        print(f'No book with ISBN {return_isbn} found')

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

def remove_book():
    remove_isbn = find_book_by_isbn()
    if remove_isbn != -1:
        del bookshelf[remove_isbn]

def print_books():
    print('{:<15}{:<26}{:<26}{:<21}{:<10}'.format('ISBN','Title','Author','Genre','Availability'))
    for book in bookshelf:
        print(book)

def save_books():
    with open('books.csv','r+') as file:
        saved_text = ''
        for book in bookshelf:
            saved_text = f'{book.get_isbn()},{book.get_title()},{book.get_author()},{book.get_genre()},{book.get_availability_t_or_f()}'
            file.write(saved_text)
    print('Book catalog has been saved.')

def main():
    print('Starting the system ... ')
    global file_name
    file_name = input('Enter book catalog filename: ')
    while os.path.isfile(file_name) == False:
        file_name = input('File not found. Re-enter book catalog filename: ')
    global bookshelf
    bookshelf = []
    load_books(bookshelf, file_name)
    print('Book catalog has been loaded.')
    
    user_selection = print_menu(MAIN_MENU, MAIN_OPTIONS)
    while user_selection != 0:
        match user_selection: 
            case 1:
                search = search_str()
                search_books(search)
                user_selection = print_menu(MAIN_MENU, MAIN_OPTIONS)
                continue
            case 2:
                print()
                borrow_book()
                user_selection = print_menu(MAIN_MENU, MAIN_OPTIONS)
                continue
            case 3:
                print()
                return_book()
                user_selection = print_menu(MAIN_MENU, MAIN_OPTIONS)
                continue
            case 4:
                print()
                add_books()
                user_selection = print_menu(MAIN_MENU, MAIN_OPTIONS)
                continue
            case 5:
                print()
                remove_book()
                user_selection = print_menu(MAIN_MENU, MAIN_OPTIONS)
                continue
            case _:
                print()
                print_books()
                user_selection = print_menu(MAIN_MENU, MAIN_OPTIONS)
                continue
    print()
    print('-- Exit the System -- ')
    save_books()
    print('Good Bye!')
    exit()

if __name__ == '__main__':
    main()
