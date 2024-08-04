# Dependency Inversion Principle (DIP)
# High-level modules should not depend on low-level modules. Both should depend on abstractions.
class Keyboard:
    def __init__(self):
        self.is_on = False
    
    def type(self):
        if self.is_on:
            print("Typing...")
        else:
            print("Keyboard is off")

class Computer:
    def __init__(self, keyboard):
        self.keyboard = keyboard
    
    def start(self):
        self.keyboard.is_on = True

keyboard = Keyboard()
computer = Computer(keyboard)
computer.start()
keyboard.type()

# in this code if we wnt to change Keyboard class we should also change computer class and this reduce 
# our code felxblity
# to solve that problem we should impelant a interface 

from abc import ABC, abstractmethod

class KeyboardInterface(ABC):
    @abstractmethod
    def type(self):
        pass

class Keyboard(KeyboardInterface):
    def __init__(self):
        self.is_on = False
    
    def type(self):
        if self.is_on:
            print("Typing...")
        else:
            print("Keyboard is off")

class Computer:
    def __init__(self, keyboard: KeyboardInterface):
        self.keyboard = keyboard
    
    def start(self):
        self.keyboard.is_on = True

keyboard = Keyboard()
computer = Computer(keyboard)
computer.start()
keyboard.type()
