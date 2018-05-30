
class ItemFns(object):
  def __init__(self, game_map, player):
    self.map = game_map
    self.player = player
    
  def slap(self, target):
    if target == "chicken":
      print("BGAWK. You're in {0}. BGAWK.".format(self.map.get_printable_name(self.player.location)))
      return True
    else:
      return False
  
  trigger_fns = {"slap": slap}
  
  item_triggers = {"chicken": ["slap"]}
  
  def available(self, player):
    triggers = []
    for key, _ in player.inventory.items():
      triggers += self.item_triggers[key]
    return triggers
  
  def process_input(self, action, target):
    return self.trigger_fns[action](self, target)