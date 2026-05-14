"""
AUTHOR: Faith Paule
PROGRAM CODE: BCS13
DATE: S.Y. 2022-2023

PROGRAM: Circular Linked List Implementation
LANGUAGE: Python 3
TOPIC: Data Structures and Algorithms (DSA) - Circular Linked Lists
TECH STACK: Python Standard Library (Object-Oriented Programming)

DESCRIPTION:
Implements a Circular Linked List data structure where the last node points
back to the first node, forming a circle. Unlike a standard linked list,
there is no NULL at the end.

KEY CHARACTERISTICS:
- Each node contains data and a reference to the next node
- Last node's 'next' points to the first node (head)
- Can traverse indefinitely in a circle
- Useful for round-robin scheduling, game loops, etc.

STRUCTURE:
CreateList (outer class)
    └── Node (inner class)
        ├── data: stored value
        └── next: pointer to next node
"""

class CreateList:
    """
    Outer class representing the Circular Linked List.
    Manages head and tail pointers and provides list operations.
    """
    
    # ========================================================================
    # INNER CLASS: Node
    # ========================================================================
    class Node:
        """
        Represents a single node in the circular linked list.
        
        Attributes:
            data: The value stored in the node
            next: Reference/pointer to the next node in the list
        """
        
        def __init__(self, data):
            """
            Constructor for Node - creates a new node.
            
            Args:
                data: The value to store in the node
            """
            self.data = data      # Store the data value
            self.next = None      # Initially, next points to nothing

    # ========================================================================
    # MAIN LIST CONSTRUCTOR
    # ========================================================================
    def __init__(self):
        """
        Constructor for CreateList - initializes empty circular linked list.
        
        For an empty list:
        - head = None (no first node)
        - tail = None (no last node)
        """
        # Declaring head and tail pointer as None (empty list)
        self.head = None    # Points to first node
        self.tail = None    # Points to last node

    # ========================================================================
    # ADD METHOD (Append to end)
    # ========================================================================
    def add(self, data):
        """
        Adds a new node to the end of the circular linked list.
        
        Maintains circular property: tail.next always points to head.
        
        Algorithm:
        1. Create new node with given data
        2. If list is empty, new node becomes both head and tail
        3. If list not empty, add after tail, update tail, maintain circular link
        
        Args:
            data: The value to add to the list
        """
        
        # Step 1: Create a new node
        new_node = self.Node(data)
        
        # Step 2: Check if the list is empty
        if self.head is None:
            # If empty, both head and tail point to the new node
            self.head = new_node
            self.tail = new_node
            # In a circular list, the only node points to itself
            new_node.next = self.head  # Circular link to head
        else:
            # Step 3: List not empty - add to end
            
            # Current tail's next should point to new node
            self.tail.next = new_node
            
            # New node becomes the new tail
            self.tail = new_node
            
            # Maintain circular property: tail points back to head
            self.tail.next = self.head

    # ========================================================================
    # DISPLAY METHOD (Traverse and print all nodes)
    # ========================================================================
    def display(self):
        """
        Displays all nodes in the circular linked list.
        
        Since list is circular, we traverse until we return to head.
        Special handling for empty list.
        
        Algorithm:
        1. Start at head
        2. If list empty, print message
        3. Otherwise, traverse while printing each node
        4. Stop when we come back to head (circular condition)
        """
        
        # Start from the head node
        current = self.head
        
        # Case 1: List is empty
        if self.head is None:
            print("List is empty")
        
        # Case 2: List has nodes
        else:
            print("Nodes of the circular linked list: ")
            
            # Traverse the circular list
            while True:
                # Print current node's data
                print(" " + str(current.data), end="")
                
                # Move to next node
                current = current.next
                
                # Stop condition: when we've returned to the head
                # (completing the circle)
                if current == self.head:
                    break
            
            # Print new line after all nodes displayed
            print()


# ============================================================================
# MAIN PROGRAM - USER INTERFACE
# ============================================================================

if __name__ == "__main__":
    """
    Main execution block - creates list and gets user input.
    Only runs if script is executed directly (not imported as module).
    """
    
    # Create an empty circular linked list
    cl = CreateList()

    # Get number of nodes from user
    num_of_nodes = int(input("Enter the number of nodes: "))

    # Loop to add each node with user-provided data
    for i in range(num_of_nodes):
        data = int(input(f"Enter data for node {i+1}: "))
        cl.add(data)  # Add node to circular linked list

    # Display all nodes in the list
    cl.display()
