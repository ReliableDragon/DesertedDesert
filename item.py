class Item(object):
  def __init__(self, key, printable_name, name, description):
    self.key = key
    self.printable_name = printable_name
    self.name = name
    self.description = description
    
  def __repr__(self):
    return "<Item ({0}, {1}, {2}, {3})>"\
    .format(self.key, self.printable_name, self.name, self.description)