from location import Location

import os
import sys

class Map(object):
  def __init__(self, map_filename, data_filename):
    self._locations = []
    self._distances = {}
    with open(os.path.join(sys.path[0], data_filename), 'r') as f:
      for line in f:
        key,name,description = line.strip().split("|")
        self._locations.append(Location(key, name, description))
    with open(os.path.join(sys.path[0], map_filename), 'r') as f:
      for line in f:
        data = line.strip().split(" ")
        key = data[0]
        distances = map(lambda s: s.split(","), data[1:])
        self._distances[key] = {to: distance for (to, distance) in distances}
        
  def __repr__(self):
    rep = "<Map "
    rep += "locations:["
    for l in self._locations:
      rep += "{0}, ".format(l)
    rep += "], distances:{"
    for k, v in self._distances.items():
      rep += "{0}: {1}, ".format(k, v)
    rep += "}>"
    return rep
        
  def get_distance(self, curr, dest):
    return self._distances[curr][dest]
  
  def describe(self, loc):
    return _locations[loc].description
  
  def get_visible(self, loc):
    return [destination for destination, _ in self._distances.items()]
    