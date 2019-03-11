class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:
            while counter <= position:
                if counter == position - 1: # If we are at the node prior to the desired insertion position
                    new_element.next = current.next # Link the new node to the next link
                    current.next = new_element # Link the current node to the new one
                current = current.next # Keep going to the next node
                counter += 1 # Increment the counter
        elif position == 1: # If we desire to insert a new head
            new_element.next = self.head # Link the new node to the current head node
            self.head = new_element # Reassign self.head to reflect the changes
        
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next: # While the current value is not the value we wish to remove and the next node exists
            previous = current  # Set the previous node equal to the current
            current = current.next  # Move to the next node
        if current.value == value:  # If the current node value is equal to the value we wish to remove
            if previous:  # If there exists a node previous to the current
                previous.next = current.next  # Set the previous node's pointer to node after the current
            else:
                self.head = current.next  # Else if we are at the head node, set the next node as the head

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value