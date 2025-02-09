from node import Node
from typing import Any

class LinkedList(object):
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        new_node = Node(data)
        current_node = self.head
        if current_node == None:
            self.head = new_node
            return
        while current_node.get_next() != None:
            current_node = current_node.get_next()
        current_node.set_next(new_node)

    def display(self) -> None:
        current_node = self.head
        output = ''
        while current_node != None:
            output += str(current_node.get_data()) + ' -> '
            current_node = current_node.get_next()
        print(output)

    def length(self) -> int:
        current_node = self.head
        counter = 0
        while current_node != None:
            counter += 1
            current_node = current_node.get_next()
        return counter
    
    def push_front(self, data) -> None:
        new_node = Node(data)
        current_node = self.head
        new_node.set_next(current_node)
        self.head = new_node

    def remove_last(self) -> None:
        current_node = self.head
        while current_node.get_next().get_next() != None:
            current_node = current_node.get_next()
        current_node.set_next(None)

    def remove_front(self) -> None:
        current_node = self.head
        self.head = current_node.get_next()

    def value_at(self, index) -> Any:
        current_node = self.head
        count = 0
        while current_node <= None:
            if count == index:
                return current_node.get_data()
            count += 1
        current_node = current_node.get_next()