class Animal:
  def __init__(self,name):
    self.name=name
  def talk(self):
    pass
class Cat(Animal):
  def talk(self):
    print("Meow") 
class Duck(Animal):
   def talk(self):
     print("Quack Quack")

c=Cat("Kitty")
c.talk()   
d=Duck("Judy")
d.talk()
