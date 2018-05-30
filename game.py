from game_map import Map
from player import Player

import re

class Game(object):
  
  nonword_characters = re.compile('[\W_]+')
  
  def __init__(self, name, gender):
    self.player = Player(name, gender)
    self.map = Map('farm_map.txt', 'farm_data.txt')
  
  def move_to(self, location):
    if not location:
      return False
    self.player.location = location
    return True
  
  def describe(self, target):
    if not target:
      print(self.map.get_atmosphere(self.player.location))
      return True
    print(self.get_description(target))
    return True
  
  known_actions = {
    'move': move_to,
    'go': move_to,
    'approach': move_to,
    'look': describe,
    'investigate': describe,
    'describe': describe,
  }
    
  def print_intro(self):
    text = """A long time ago, a $MAN named {0} lived in the wilderness with $HIS aging parents. 
           $HE lived a poor life, farming just enough for them to get by, eking out a living 
           in the rocky soil. Eventually, $HIS mother died, and $HIS father did not survive 
          long after that. Now all alone, the $MAN must decide what to do with $HIS life."""\
          .format(self.player.name)
    text = self.process_text(text)
    print(text)
    self.prompt()
    
  # TODO: Get items from Context and include them.
  def process_input(self, text):
    words = text.split()
    words = map(lambda w: self.nonword_characters.sub('', w), words)
    seen_locations = self.get_nearby()
    print(seen_locations)
    action = next((action for action in self.known_actions if action in text), None)
    target = next((location for location in seen_locations if self.map.get_name(location) in text), None)
    print("Action: {0}\nTarget: {1}".format(action, target))
    succeeded = False
    if action:
      succeeded = self.known_actions[action](self, target)
    if not succeeded:
      print("I'm sorry, I didn't understand. Try again, or /help for help.")
    self.prompt()
      
  def prompt(self):
    setting = "You are standing by {0}. You can see ".format(self.map.get_printable_name(self.player.location))
    for i, loc in enumerate(self.get_nearby_names()):
      if i < len(self.get_nearby_names()) - 1:
        setting += "{0}, ".format(loc)
      else:
        setting += "and {0}".format(loc)
    if len(self.get_nearby_names()) == 0:
      setting += "nothing"
    setting += " nearby."
    print(setting)
    print("What do you do?")
    

  # Fixes pronouns.
  def process_text(self, text):
    text = text.replace("$HE", "he" if self.is_male() else "she")
    text = text.replace("$HIS", "his" if self.is_male() else "her")
    text = text.replace("$MAN", "man" if self.is_male() else "woman")
    return ' '.join(text.split())
  
  def is_male(self):
    return self.player.gender == 'm'
  
  def is_female(self):
    return not is_male()
  
  def get_nearby(self):
    return self.map.get_visible(self.player.location)
  
  def get_nearby_names(self):
    return [self.map.get_printable_name(loc) for loc in self.get_nearby()]
  
  # TODO: Make this support objects from Context.
  def get_description(self, target):
    return self.map.describe(target)
    