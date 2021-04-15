class Animal:
  def __init__(self,name):
    self.name=name
  def talk(self):
    pass
class Cat(Animal):
  def talk(self):
    print("Meow") 
class Cow(Animal):
   def talk(self):
     print("Moo")

c=Cat("Kitty")
c.talk()   
d=Cow("Judy")
d.talk()
