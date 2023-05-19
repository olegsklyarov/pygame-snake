class Element:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, o):
    return self.x == o.x and self.y == o.y

  def __str__(self):
    return "Element: ({} {})".format(self.x, self.y)