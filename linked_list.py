from node import Node
from typing import Any

class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.size = 0 # Var to constantly track size of the list

    def append(self, data) -> None:
        new_node = Node(data)
        current_node = self.head
        self.size += 1
        if current_node is None:
            self.head = new_node
            return
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def display(self) -> None:
        if not self.head:
            print('List is empty')
            return
        
        current_node = self.head
        output = []
        while current_node is not None:
            output.append(str(current_node.get_data()))
            current_node = current_node.get_next()
        print(f'LinkedList: {" -> ".join(output)} -> None')

    def length(self) -> int:
        
        #current_node = self.head
        #counter = 0
        #while current_node != None:
        #    counter += 1
        #    current_node = current_node.get_next()

        return self.size # Now O(1) instead if O(n)
    
    def push_front(self, data) -> None:
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.size += 1

    def remove_last(self) -> None:
        # Handle exception cases
        if not self.head:
            return # List is empty
        if not self.head.get_next():
            self.head = None # Only one element
            self.size -= 1
            return
        
        current_node = self.head
        while current_node.get_next().get_next() is not None:
            current_node = current_node.get_next()
        current_node.set_next(None)
        self.size -= 1

    def remove_front(self) -> None:
        # Handle exception cases
        if not self.head:
            return # List is empty

        self.head = self.head.get_next()
        self.size -= 1

    def value_at(self, index) -> Any:
        # Handle exception cases
        if index < 0 or index >= self.size:
            raise IndexError("Out of range")
        current_node = self.head
        count = 0
        while current_node is not None:
            if count == index:
                return current_node.get_data()
            count += 1
            current_node = current_node.get_next()

    def insert(self, index, data) -> None:
        # Handle exception cases
        if index < 0 or index > self.size:
            raise IndexError('Out of range')
        if index == self.size:
            self.append(data)
            return
        if index == 0:
            self.push_front(data)
            return

        new_node = Node(data)
        current_node = self.head
        count = 0
        self.size += 1

        while count + 1 < index:
            count += 1
            current_node = current_node.get_next()

        node_after = current_node.get_next()
        current_node.set_next(new_node)
        new_node.set_next(node_after)
    
    def remove(self, index) -> None:
        # Handle exception cases
        if index < 0 or index >= self.size:
            raise IndexError('Out of range')
        if index == self.size - 1:
            self.remove_last()
            return
        if index == 0:
            self.remove_front()
            return
        
        current_node = self.head
        count = 0

        while current_node.get_next() is not None:
            if count + 1 == index:
                node_to_rem = current_node.get_next()
                node_after = node_to_rem.get_next()
                current_node.set_next(node_after)
                self.size -= 1
                return
            count += 1
            current_node = current_node.get_next()
    
    def reverse(self) -> None:
        # Do not process the list if empty
        if not self.head:
            return
        
        previous_node = None
        current_node = self.head
        next_node = None

        while current_node is not None:
            next_node = current_node.get_next()
            current_node.set_next(previous_node)
            previous_node = current_node
            current_node = next_node
        self.head = previous_node