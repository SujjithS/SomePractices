class Animal:
  def __init__(self,name):
    self.name=name
  def talk(self):
    pass
class Cat(Animal):
  def talk(self):
    print("Meow") 
class Dog(Animal):
   def talk(self):
     print("Woof Woof")

c=Cat("Kitty")
c.talk()   
d=Dog("Caesar")
d.talk()
