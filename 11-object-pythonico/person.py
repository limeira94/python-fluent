class Person:
    def __init__(self, name):
        self.__name = name
        
    @property
    def name(self):
        """Getter for name"""
        return self.__name
    
    @name.setter
    def name(self, value):
        """Setter for name"""
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self.__name = value
        
    @name.deleter
    def name(self):
        """Deleter for name"""
        del self.__name
        
    