class Person:
    def __init__(self, name):
        self.name = name

    def gender(self):
        raise NotImplementedError("Subclasses must define gender")

    def greet(self):
        return f"Hello, I'm {self.name} and I identify as {self.gender()}."
