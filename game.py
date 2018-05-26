from map import Map

class Game(object):
  
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender
    if not (self.gender == 'm' or self.gender == 'f'):
      raise Exception("Got {0} for gender. Expected 'm' or 'f'.".format(self.gender))
    self.map = Map('farm_map.txt', 'farm_data.txt')
    
  def print_intro(self):
    text = """A long time ago, a $MAN named {0} lived in the wilderness with $HIS aging parents. 
           $HE lived a poor life, farming just enough for them to get by, eking out a living 
           in the rocky soil. Eventually, $HIS mother died, and $HIS father did not survive 
          long after that. Now all alone, the $MAN must decide what to do with $HIS life."""\
          .format(self.name)
    text = self.process_text(text)
    print(text)
    prompt()
    
  def print_stats(self):
    print("Name: {0}".format(self.name))
    
  def print_map(self):
    print(self.map)
    
  def process_input(self, text):
    print("Sorry, I don't understand.")

  def process_text(self, text):
    text = text.replace("$HE", "he" if self.is_male() else "she")
    text = text.replace("$HIS", "his" if self.is_male() else "her")
    text = text.replace("$MAN", "man" if self.is_male() else "woman")
    return ' '.join(text.split())
      
  def is_male(self):
    return self.gender == 'm'
  
  def is_female(self):
    return not is_male()
  
def prompt():
  print("What do you do?")
    