from abc import ABC, abstractmethod

class animal(ABC):
  @abstractmethod
  def make_sound(self):
    pass

class Lion(animal):
  def make_sound(self):
    print("Roor!");

class Cow(animal):
  def make_sound(self):
    print("Moo!");

lion = Lion();
lion.make_sound();

cow = Cow();
cow.make_sound();
