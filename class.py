class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Eating...")
    def breathe(self):
        print("Breathing...") 


#Animal1 = Animal("dog")
#Animal1.eat()    

class Dog(Animal):
    def sound(self):
        print("Barking....")

class Cat(Animal):
    def sound(self):
        print("Meow...")


dog1 = Dog("Jack")
dog1.eat()  
dog1.sound()                      
print(" ")
cat1 = Cat("cat")
cat1.eat()
cat1.sound()