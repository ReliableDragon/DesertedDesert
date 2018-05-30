from location import Location
from item import Item

import os
import sys

class Map(object):
  def __init__(self, map_filename, map_descriptions_filename, items_filename, items_map_filename):
    self._locations = {}
    self._distances = {}
    self._items = {}
    with open(os.path.join(sys.path[0], map_descriptions_filename), 'r') as f:
      for line in f:
        key,printable_name,name,description,atmosphere = line.strip().split("|")
        self._locations[key] = Location(key, printable_name, name, description, atmosphere)
    with open(os.path.join(sys.path[0], map_filename), 'r') as f:
      for line in f:
        data = line.strip().split(" ")
        key = data[0]
        distances = map(lambda s: s.split(","), data[1:])
        self._distances[key] = {to: distance for (to, distance) in distances}
    with open(os.path.join(sys.path[0], items_filename), 'r') as f:
      for line in f:
        key,printable_name,name,description = line.strip().split('|')
        self._items[key] = Item(key, printable_name, name, description)
    with open(os.path.join(sys.path[0], items_map_filename), 'r') as f:
      for line in f:
        loc,item = line.strip().split(' ')
        self._locations[loc].items.append(self._items[item])
        
  def __repr__(self):
    rep = "<Map "
    rep += "locations:{"
    for k, v in self._locations.items():
      rep += "{0}: {1}, ".format(k, v)
    rep += "}, distances:{"
    for k, v in self._distances.items():
      rep += "{0}: {1}, ".format(k, v)
    rep += "}>"
    return rep
        
  def get_distance(self, curr, dest):
    return self._distances[curr][dest]
  
  def get_name(self, loc):
    return self._locations[loc].name
  
  def get_printable_name(self, loc):
    return self._locations[loc].printable_name
  
  def describe(self, loc):
    return self._locations[loc].description
  
  def get_atmosphere(self, loc):
    return self._locations[loc].atmosphere
  
  def get_visible(self, loc):
    return [self._locations[destination] for destination, _ in self._distances[loc].items()]
  
  def get_items(self, loc):
    return self._locations[loc].items
  
  def get_item(self, key):
    return self._items[key]
    