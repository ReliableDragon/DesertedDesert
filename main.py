#!/usr/bin/env python3
from game import Game

DEBUG = True

command_help = {
  '/help': 'Prints this message.',
  '/stats': 'Prints your character\'s stats.',
  '/exit': 'Exits the game. Does not save!',
}

debug_help = {
  '/map': 'Prints the map',
}

if DEBUG:
  command_help = {**command_help,  **debug_help}

game = None

def print_help():
  for k,v in command_help.items():
    print("{0}: {1}".format(k, v))
    
def print_stats():
  game.player.print_stats()
  
def print_exit():
  print("Goodbye!")
  
def print_map():
  print(game.map)
  print("Player location: {0}".format(game.player.location))

commands = {
  '/help': print_help,
  '/stats': print_stats,
  '/exit': print_exit,
}

debug_commands = {
  '/map': print_map,
}

if DEBUG:
  commands = {**commands, **debug_commands}

def run_game():
  command = ''
  while command != '/exit':
    command = input('')
    if command in commands:
      commands[command]()
    else:
      game.process_input(command)
  
if __name__ == '__main__':
  # name = input("What is your name?\n")
  # gender = None
  name = "Gabe"  # Skip intro for testing.
  gender = "m"
  while not gender or (gender[0] != 'm' and gender[0] != 'f'):
    gender = input("What is your gender? [m/f]\n")
  game = Game(name, gender[0])
  game.print_intro()
  run_game()
  
  
  
  
  
  
  
  
  
  