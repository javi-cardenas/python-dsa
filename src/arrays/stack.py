class Stack:
    def __init__(self, iterable=None):
        self._items = iterable.copy() if iterable else [] # copy to avoid shared reference
    
    def __len__(self):
        return len(self._items)
    
    def __str__(self):
        return f"Stack({self._items})"
    
    def push(self, value):
        self._items.append(value)
        
    def pop(self):
        if self.is_empty():
            return None # return None instead of raising IndexError
        return self._items.pop()
    
    def peek(self):
        if self.is_empty():
            return None # return None instead of raising IndexError
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0