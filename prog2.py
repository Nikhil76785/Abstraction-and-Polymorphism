from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can walk and run.")

class Snake(Animal):

    def move(self):
        print("I can crawl.")

class Dog(Animal):

    def move(self):
        print("I can bark.")

class Lion(Animal):
    
    def move(self):
        print("I can roar.")

obj = Human()
obj.move()

obj2 = Snake()
obj2.move()

obj3 = Dog()
obj3.move()

obj4 = Lion()
obj4.move()