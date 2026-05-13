# bank_account_encapsulation.py
Learning and demonstrating Object-Oriented Programming (OOP) concepts, specifically:
1. Encapsulation - The fundamental principle of bundling data (attributes) and methods (functions) within a class, hiding internal details from outside access
2. Access Modifiers - Understanding how Python implements:
    2.1 Public (default) - no prefix, accessible everywhere
    2.2 Protected (single underscore _) - internal use by convention
    2.3 Private (double underscore __) - true data hiding via name mangling
3. BankAccount Example - A practical demonstration showing:
    3.1 Why we protect sensitive data like account balance
    3.2 How getter methods provide controlled read access
    3.3 Why operations like deposit/withdraw should go through methods, not direct attribute modification
4. Language Used:
    4.1 Python 3
    4.2 Uses OOP features: classes, methods, attributes, constructors

TOPIC: Encapsulation and Access Modifiers in Python
Concepts Covered:
1. Lists, Dictionaries, Functions (mentioned as prerequisites)
2. Encapsulation - Wrapping data and methods into a single unit
3. Access Modifiers - Controlling access to class attributes and methods

Encapsulation:
- Mechanism of wrapping attributes and code acting on methods together as a single unit
- Attributes of a class are hidden from other classes and can be accessed only 
  through methods of their current class
- Also known as 'data hiding'

Benefits of Encapsulation:
1. Simplifies complexity - hides internal implementation details
2. Protects data - prevents accidental or unauthorized modification

Python Convention for Access Control:
- Single Underscore Prefix ('_') : Indicates attribute/method should be treated 
  as 'private' or 'internal' (convention-based, not enforced)

Access Modifiers:
1. Public (+)
   - Accessible from anywhere (within class, subclasses, and outside)
   - Default in Python (no prefix)

2. Protected (#)
   - Intended for use within class and its subclasses
   - Can be accessed outside but by convention should not be
   - Denoted by single underscore prefix '_'

3. Private (_)
   - Meant to be accessed only within the class
   - NOT accessible from outside (name mangling applies)
   - Denoted by double underscore prefix '__'
   - Python implements this through name mangling
"""
