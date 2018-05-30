class Location(object):
  def __init__(self, key, printable_name, name, description, atmosphere):
    self.key = key
    self.printable_name = printable_name  # Name with articles, etc.
    self.name = name  # Name players will use to target
    self.description = description  # Description when viewed from elsewhere
    self.atmosphere = atmosphere  # Description when player is there
    self.items = []
    
  def __repr__(self):
    desc = "<Location ({0}, {1}, {2}, {3}, {4}) items: ["\
           .format(self.key, self.printable_name, self.name, self.description, self.atmosphere)
    for item in self.items:
      desc += "{0}, ".format(item)
    desc += "]>"
    return desc