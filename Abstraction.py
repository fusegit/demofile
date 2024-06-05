from abc import ABC,abstractmethod

class Human(ABC):
    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def speak(self):
        pass
    def hoby(self):
        print('play cricket')

class Person(Human):
    def __init__(self) -> None:
      print('in sub class con')
    def walk(self):
        print('person are waking')

    def speak(self):
         print('person are speaking')

per=Person()
per.hoby()
per.speak()
per.walk()

# class Animal(Human):
#     def __init__(self) -> None:
#         print('con in animal class')

#     def speak(self):
#         print('animal are not speaking')
#     def walk(self):
#         print('animal are walking on the ground')


# ani=Animal()
# ani.hoby()
# ani.speak()
# ani.walk()

