from game_map import Map
from player import Player
from item_fns import ItemFns

import re

class Game(object):
  
  nonword_characters = re.compile('[\W_]+')
  
  def __init__(self, name, gender):
    self.player = Player(name, gender)
    self.map = Map('farm_map.txt', 'farm_descriptions.txt', 'farm_items.txt', 'farm_items_map.txt')
    self.item_fns = ItemFns(self.map, self.player)
  
  def move_to(self, location):
    if not location:
      return False
    self.player.location = location
    print(self.map.get_atmosphere(self.player.location))
    return True
  
  def describe(self, target):
    if not target:  # Describe the current location.
      print(self.map.get_atmosphere(self.player.location))
      return True
    print(self.get_description(target))
    return True
  
  def take(self, key):
    print("Items: {0}".format(self.map.get_items(self.player.location)))
    if not key in [item.key for item in self.map.get_items(self.player.location)]:
      return False
    item = self.map.get_item(key)
    print("You pick up the {0}.".format(item.name))
    self.player.inventory[key] = item
    return True
  
  
  known_actions = {
    'move': move_to,
    'go': move_to,
    'approach': move_to,
    'look': describe,
    'investigate': describe,
    'describe': describe,
    'pick up': take,
    'grab': take,
    'take': take,
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
    
    
  def process_input(self, text):
    words = text.split()
    words = map(lambda w: self.nonword_characters.sub('', w), words)
    
    seen_locations = self.get_visible_locations()
    seen_items = self.get_visible_items()
    permanent_actions = list(self.known_actions.keys())
    item_actions = self.item_fns.available(self.player)
    
    targets = seen_locations + seen_items
    actions = permanent_actions + item_actions
    
    # print(seen_locations)
    # print(seen_items)
    
    action = next((action for action in actions if action in text), None)
    target = next((target for target in targets if target.name in text), None)
    
    if target:
      target = target.key
      
    print("Action: {0}\nTarget: {1}".format(action, target))
    
    succeeded = False
    if action in self.known_actions:
      succeeded = self.known_actions[action](self, target)
    elif action:
      succeeded = self.item_fns.process_input(action, target)
    if not succeeded:
      print("I'm sorry, I didn't understand. Try again, or /help for help.")
      
    self.prompt()


  def prompt(self):
    setting = "You are standing by {0}. You can see "\
              .format(self.map.get_printable_name(self.player.location))
    for i, loc in enumerate(self.get_visible_locations_names()):
      if i < len(self.get_visible_locations_names()) - 1:
        setting += "{0}, ".format(loc)
      else:
        setting += "and {0}".format(loc)
    if len(self.get_visible_locations_names()) == 0:
      setting += "nothing"
    setting += " nearby."
    print(setting)
    print("What do you do?")

  # Fixes pronouns and extra spaces.
  def process_text(self, text):
    text = text.replace("$HE", "he" if self.is_male() else "she")
    text = text.replace("$HIS", "his" if self.is_male() else "her")
    text = text.replace("$MAN", "man" if self.is_male() else "woman")
    return ' '.join(text.split())
  
  def is_male(self):
    return self.player.gender == 'm'
  
  def is_female(self):
    return not is_male()
  
  def get_visible_locations(self):
    return self.map.get_visible(self.player.location)
  
  def get_visible_items(self):
    return self.map.get_items(self.player.location)
  
  def get_visible_locations_names(self):
    return [loc.printable_name for loc in self.get_visible_locations()]
  
  def get_description(self, target):
    if target in [location.key for location in self.get_visible_locations()]:
      return self.map.describe(target)
    elif target in [item.key for item in self.get_visible_items()]:
      return self.map.get_item(target).description
    