from random import randrange
from .element import Element

class Field:
  def __init__(self, width, height):
    self.height = height
    self.width = width
  
  def gen_random_element(self) -> Element:
    return Element(
      randrange(0, self.width), 
      randrange(0, self.height),
    )
  
  def get_center_element(self) -> Element:
    return Element(
      self.width // 2,
      self.height // 2,
    )