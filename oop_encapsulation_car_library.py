'''
AUTHOR: Faith Paule
Program Code: BCS13

Implementing Object-Oriented Programming (OOP) concepts in Python, specifically focusing on:
1. Access Modifiers/Encapsulation - Demonstrating protected (_) and private (__) attributes/methods in a Car class
2. Understanding a Programming Assignment - You've been given a Library Catalog System activity (Activity 1) with clear requirements to:
	2.1 Build a Book class with encapsulation
	2.2 Implement a console-based library management system
	2.3 Handle book borrowing and returning functionality
	2.4 Submit with GitHub link and screenshots
3. Language Used
	3.1 Python 3 (using classes, methods, encapsulation conventions)
4. Technical Stacks
	4.1 Core Python 3 - No external libraries
	4.2 Concepts demonstrated: OOP, encapsulation, name mangling, getter patterns
	4.3 Input/Output: print(), input() (needed for the assignment)
'''

# Access and Modifier example
class Car:
    """
    A simple Car class demonstrating access modifiers:
    - Public methods: accessible from anywhere
    - Protected attributes (_single underscore): intended for internal use, but accessible
    - Private attributes (__double underscore): name-mangled, harder to access externally
    """
    
    def __init__(self, make, model, year):
        """Constructor method - initializes a new Car instance"""
        self._make = make      # protected attribute (convention: internal use only)
        self._model = model    # protected attribute (convention: internal use only)
        self.__year = year     # private attribute (name mangling: becomes _Car__year)

    def start_engine(self):
        """
        Public method to start the car engine
        Demonstrates calling a private method from within the class
        """
        self.__ignite_spark_plug()  # Calling private helper method
        print("Engine start...")

    def __ignite_spark_plug(self):
        """
        Private method - cannot be accessed directly from outside the class
        Name mangling makes this _Car__ignite_spark_plug internally
        """
        print("Spark plug ignited!")

    # Getter methods (accessors) - provide controlled access to private/protected attributes
    def get_make(self):
        """Getter for make attribute"""
        return self._make

    def get_model(self):
        """Getter for model attribute"""
        return self._model

    def get_year(self):
        """Getter for private year attribute - only way to access __year externally"""
        return self.__year


# Instantiation and testing
my_car = Car("Toyota", "Camry", 2022)

# Accessing attributes through getter methods
print(my_car.get_make())   # Output: Toyota
print(my_car.get_model())  # Output: Camry
print(my_car.get_year())   # Output: 2022

# Calling public method
my_car.start_engine()
# Output:
# Spark plug ignited!
# Engine start...

# This would raise an AttributeError (private attribute not directly accessible):
# print(my_car.__year)  # Commented out to avoid error

# To access name-mangled private attribute (not recommended - breaks encapsulation):
# print(my_car._Car__year)  # Would work but violates OOP principles
