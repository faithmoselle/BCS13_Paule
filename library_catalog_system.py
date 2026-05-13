"""
Name: Faith Moselle O. Paule
Program Code: BCS13

Language used: Python 3

Library Catalog System
Activity 230609 - Demonstrates OOP principles (encapsulation, classes, methods)

ACTIVITY ASSIGNMENT BELOW
================================================================================
230609 - Main Activity
Activity 1: Building a Library Catalog System
Objective: Implement a library catalog system using encapsulation principles.

Instructions:
Define a class called Book with the following attributes and methods:
Attributes:
- title : The title of the book.
- author: The author of the book.
- publication_year: The year the book was published.
- is_available: Indicates whether the book is available for borrowing.

Methods:
- __init__(self, title, author, publication_year): Initializes the book object with the given title, author, and publication year. Set is_available to True by default.
- get_title(self): Returns the title of the book.
- get_author(self): Returns the author of the book.
- get_publication_year(self): Returns the publication year of the book.
- is_book_available(self): Returns the availability status of the book.
- borrow_book(self): Marks the book as borrowed (sets is_available to False).
- return_book(self): Marks the book as returned (sets is_available to True).

Create a list called library to store the book objects.

Implement the following functionality in the main program:
  1. Prompt the user to enter book details (title, author, publication year).
  2. Create a Book object with the provided details and add it to the library list.
  3. Repeat the above step to add multiple books to the library.
  4. Display the available books in the library.
  5. Prompt the user to choose a book to borrow by entering its index.
     - If the chosen book is available, mark it as borrowed and display a success message. Otherwise, display an error message.
  6. Display the available books in the library again.
  7. Prompt the user to choose a book to return by entering its index.
     - If the chosen book is not available, mark it as returned and display a success message. Otherwise, display an error message.
  8. Display the available books in the library one final time.

Note: You can use the input() function to get user input and the print() function to display messages and book information.

Grading:
    First 1-10 submission without errors --> 100 points
    Second 11-20 submission without errors --> 90 points
    Third 21-30 submission without errors --> 85
    the rest without errors --> 80
    Late submission or submission with error --> 60
================================================================================
Implementing a Library Catalog System - a console-based application that demonstrates:
  1. Object-Oriented Programming (OOP) - Creating and using a Book class
  2. Encapsulation - Using getter methods to access private attributes
  3. CRUD Operations - Create (add books), Update (borrow/return), Read (display books)
  4. Menu-driven Interface - User interaction via numbered choices
  5. Input Validation - Error handling for invalid inputs and out-of-range indices
  6. Collection Management - Storing objects in a list and manipulating them

This is a practical exercise for learning:
  1. Class design and instantiation
  2. Method creation and calling
  3. List operations with custom objects
  4. User input handling in Python
  5. Basic error handling (try-except)
"""

class Book:
    """
    Book class representing a book in the library catalog.
    Demonstrates encapsulation with getter methods and private attribute management.
    """
    
    def __init__(self, title, author, publication_year):
        """
        Constructor - initializes a new Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            publication_year (str/int): The year the book was published
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True  # Default: book is available for borrowing

    # Getter methods (accessors) - provide controlled access to attributes
    def get_title(self):
        """Returns the title of the book"""
        return self.title

    def get_author(self):
        """Returns the author of the book"""
        return self.author

    def get_publication_year(self):
        """Returns the publication year of the book"""
        return self.publication_year

    def is_book_available(self):
        """
        Returns the availability status of the book.
        
        Returns:
            bool: True if available, False if borrowed
        """
        return self.is_available

    def borrow_book(self):
        """
        Marks the book as borrowed if available.
        Sets is_available to False and displays success/error message.
        """
        if self.is_available:
            self.is_available = False  # Mark as borrowed
            print(
                f"You've successfully borrowed the book: {self.title} "
                f"({self.publication_year}) by {self.author}."
            )
        else:
            print(
                f"We are sorry, '{self.title}' by {self.author} "
                f"({self.publication_year}) is not available."
            )

    def return_book(self):
        """
        Marks the book as returned if it was borrowed.
        Sets is_available to True and displays success message.
        """
        if not self.is_available:  # Book is currently borrowed
            self.is_available = True  # Set to True for return
            print(
                f"'{self.title}' by {self.author} "
                f"({self.publication_year}) has been returned."
            )
        else:
            print(
                f"'{self.title}' by {self.author} "
                f"({self.publication_year}) is already available."
            )


# Global list to store all Book objects in the library
library = []


def display_available_books():
    """
    Displays all books currently available for borrowing.
    Shows index, title, author, and publication year for each available book.
    """
    if not library:
        print("No Books Available in the library.")
    else:
        print("\n" + "=" * 50)
        print("AVAILABLE BOOKS:")
        print("=" * 50)
        for index, book in enumerate(library):
            if book.is_book_available():
                print(
                    f"[{index}] {book.get_title()} by {book.get_author()} "
                    f"({book.get_publication_year()})"
                )
        print("=" * 50)


def main():
    """
    Main program loop - Provides menu-driven interface for library management.
    Implements: add books, borrow books, return books, display available books
    """
    while True:
        # Display menu options
        print("\n" + "=" * 40)
        print("LIBRARY CATALOG SYSTEM")
        print("=" * 40)
        print("1. Add a book to the library")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display available books")
        print("5. Exit")
        print("=" * 40)
        
        choice = input("Enter your choice (1-5): ")

        # Choice 1: Add a new book
        if choice == "1":
            print("\n--- Add New Book ---")
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publication_year = input("Enter the publication year of the book: ")

            # Create new Book object and add to library list
            book = Book(title, author, publication_year)
            library.append(book)
            print(f"✓ '{title}' has been added to the library.")

        # Choice 2: Borrow a book
        elif choice == "2":
            print("\n--- Borrow a Book ---")
            display_available_books()
            
            if library:
                try:
                    booknum = int(
                        input("Enter the book number to borrow: ")
                    )
                    # Validate index range
                    if booknum < 0 or booknum >= len(library):
                        print("Invalid book number. Please try again.")
                        continue
                    
                    book = library[booknum]
                    book.borrow_book()  # Attempt to borrow
                    
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("No books available to borrow.")

        # Choice 3: Return a book
        elif choice == "3":
            print("\n--- Return a Book ---")
            display_available_books()
            
            if library:
                try:
                    booknum = int(
                        input("Enter the book number to return: ")
                    )
                    # Validate index range
                    if booknum < 0 or booknum >= len(library):
                        print("Invalid book number. Please try again.")
                        continue
                    
                    book = library[booknum]
                    book.return_book()  # Attempt to return
                    
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("No books available to return.")

        # Choice 4: Display available books
        elif choice == "4":
            display_available_books()

        # Choice 5: Exit the program
        elif choice == "5":
            print("\n✓ Thank you for using the Library Catalog System!")
            print("Goodbye!")
            break

        # Invalid menu choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Standard Python idiom - runs main() only if script is executed directly
if __name__ == "__main__":
    main()
