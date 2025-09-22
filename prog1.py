from abc import ABC, abstractmethod

class ABclass(ABC):

    def print(self, x):
        print("Passed value", x)
    
    @abstractmethod
    def task(self):
        print("We are inside ABclass task")

class Test_class(ABclass):

    def task(self):
        print("We are inside Test_class task")

obj = Test_class()
obj.task()
obj.print(100)