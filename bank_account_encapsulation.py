"""
Name: Faith Moselle O. Paule
Program Code: BCS45

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

class BankAccount:
    """
    A BankAccount class demonstrating encapsulation and access modifiers.
    
    Demonstrates:
    - Protected attributes (single underscore)
    - Public methods that provide controlled access to internal data
    - Data hiding principle - balance is protected from direct external modification
    """
    
    def __init__(self, account_number, balance):
        """
        Constructor - Initializes a new BankAccount instance.
        
        Args:
            account_number (str): The bank account number (protected attribute)
            balance (float/int): Initial account balance (protected attribute)
        
        Note: Both attributes use single underscore (_) to indicate they are
        protected and should not be accessed directly from outside the class.
        """
        self._account_number = account_number  # Protected attribute
        self._balance = balance                # Protected attribute

    def deposit(self, amount):
        """
        Public method - Adds money to the account.        
        Validates and updates the balance through a controlled interface.
        Args:
            amount (float/int): The amount to deposit
        Demonstrates: Controlled access to protected attribute _balance
        """
        if amount > 0:
            self._balance += amount
            print(f"Deposit successful. New Balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Public method - Withdraws money from the account if sufficient funds exist.
        Implements business logic (balance check) before modifying protected data.
        Args:
            amount (float/int): The amount to withdraw
        Demonstrates: Data validation before modifying protected attribute
        """
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal successful. New Balance: {self._balance}")
        else:
            print("Insufficient funds. Cannot withdraw.")

    def get_balance(self):
        """
        Public getter method - Provides read-only access to protected _balance.
        Returns:
            float/int: The current account balance
        Demonstrates: Controlled access through method instead of direct attribute access
        This is a key principle of encapsulation - hiding internal data, providing
        methods to interact with it safely.
        """
        return self._balance
    
    def get_account_number(self):
        """
        Public getter method - Provides read-only access to protected _account_number.
        Returns:
            str: The account number
        Demonstrates: Even simple data should be accessed through methods to maintain
        encapsulation and allow future changes without breaking client code.
        """
        return self._account_number

# ============================================================================
# DEMONSTRATION AND TESTING
# Create an instance (object) of BankAccount
print("=" * 60)
print("BANK ACCOUNT DEMONSTRATION")
print("=" * 60)

# Instantiate a new bank account
my_account = BankAccount("123456", 2500)
print(f"\n1. Account Created:")
print(f"   Account Number: {my_account._account_number}")  # Accessing protected - possible but NOT recommended
print(f"   Initial Balance: ${my_account._balance}")       # Direct access - breaks encapsulation principle
print("    Note: Direct access to protected attributes is possible but violates OOP best practices")

# Better approach using getter method
print(f"\n   Better practice via getter: ${my_account.get_balance()}")

# Perform deposit operation
print("\n2. Deposit Operation:")
print("   Transaction: Deposit $500")
my_account.deposit(500)  # Demonstrates controlled balance modification

# Perform withdrawal operation
print("\n3. Withdrawal Operation:")
print("   Transaction: Withdraw $200")
my_account.withdraw(200)  # Demonstrates validation before modification

# Check final balance using getter method
print("\n4. Check Final Balance:")
print(f"   Final Balance via getter: ${my_account.get_balance()}")

# Demonstrate attempted over-withdrawal
print("\n5. Edge Case - Over-withdrawal:")
print("   Transaction: Attempt to withdraw $5000")
my_account.withdraw(5000)  # Should fail due to insufficient funds

print("\n" + "=" * 60)
print("ENCAPSULATION PRINCIPLES DEMONSTRATED:")
print("=" * 60)
print("✓ Data hiding - _balance is protected from direct external modification")
print("✓ Controlled access through deposit(), withdraw(), and get_balance()")
print("✓ Business logic validation in withdraw() method")
print("✓ Single responsibility - class manages its own data")
print("=" * 60)


# ============================================================================
# ADDITIONAL EXAMPLE: Private vs Protected vs Public (For clarification)
# ============================================================================

class AccessModifiersDemo:
    """
    Demonstrates the three types of access modifiers in Python:
    1. Public (default) - accessible everywhere
    2. Protected (_single_underscore) - internal use by convention
    3. Private (__double_underscore) - name mangled, truly hidden
    """
    
    def __init__(self):
        self.public_attribute = "I am public"           # Public - accessible anywhere
        self._protected_attribute = "I am protected"    # Protected - internal use
        self.__private_attribute = "I am private"       # Private - name mangled
    
    def public_method(self):
        """Public method - can be called from anywhere"""
        return "Public method called"
    
    def _protected_method(self):
        """Protected method - for internal or subclass use by convention"""
        return "Protected method called"
    
    def __private_method(self):
        """Private method - name mangled to _ClassName__private_method"""
        return "Private method called"
    
    def access_private_inside_class(self):
        """
        Demonstrates that private members ARE accessible inside the class.
        This is the ONLY place where private members should be accessed.
        """
        return self.__private_attribute  # Works inside class


# Quick demonstration
print("\n" + "=" * 60)
print("ACCESS MODIFIERS COMPARISON")
print("=" * 60)

demo = AccessModifiersDemo()

# Public access - works fine
print(f"\n✓ Public access: {demo.public_attribute}")
print(f"✓ Public method: {demo.public_method()}")

# Protected access - works but shows warning in IDEs (by convention, should avoid)
print(f"\nProtected access (possible but not recommended): {demo._protected_attribute}")
print(f"Protected method (possible but not recommended): {demo._protected_method()}")

# Private access - THIS WILL FAIL with AttributeError
try:
    print(f"\nPrivate access attempt: {demo.__private_attribute}")
except AttributeError as e:
    print(f"Private access failed: {e}")
    print("   This demonstrates true encapsulation - private members are hidden!")

# But private members CAN be accessed via name mangling (not recommended)
print(f"\nName mangling workaround (breaks encapsulation): {demo._AccessModifiersDemo__private_attribute}")
print("   Note: This is possible but violates the principle of encapsulation!")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("1. Encapsulation bundles data and methods into a single unit")
print("2. Protected (_) is a convention - suggests 'internal use only'")
print("3. Private (__) provides true hiding through name mangling")
print("4. Always prefer getter/setter methods over direct attribute access")
print("5. Encapsulation simplifies complexity and protects data integrity")
print("=" * 60)
