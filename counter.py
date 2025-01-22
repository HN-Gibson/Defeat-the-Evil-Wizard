class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value
    
    def increment (self):
        self.value += 1

    def get_value (self):
        return self.value