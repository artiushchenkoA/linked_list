from typing import Any

class Node(object):
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

    #Getters
    def get_data(self) -> Any:
        return self.data
    
    def get_next(self) -> Any | None:
        return self.next
    
    #Setters
    def set_data(self, data) -> None:
        self.data = data
    
    def set_next(self, next) -> None:
        self.next = next
