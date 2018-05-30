
class Player(object):
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
    if not (self.gender == 'm' or self.gender == 'f'):  # Yes, yes. I know.
      raise Exception("Got {0} for gender. Expected 'm' or 'f'.".format(self.gender))
    self.location = 'home'
    self.inventory = {}
    
  def print_stats(self):
    print("Name: {0}\nLocation: {1}\nItems: {2}".format(self.name, self.location, self.inventory))
    
  def give(self, item):
    self.inventory[item.key] = item