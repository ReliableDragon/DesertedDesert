class Location(object):
  def __init__(self, key, name, description):
    self.key = key
    self.name = name
    self.description = description
    
  def __repr__(self):
    return "<Location ({0}, {1}, {2})".format(self.key, self.name, self.description)