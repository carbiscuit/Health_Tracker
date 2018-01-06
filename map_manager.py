import random
import copy

from player import Player

class Map_Manager():
  # class to update the map at the start of each turn and as turns progress
  _WALL = 0
  _FLOOR = 1
  _ITEM = 2
  _PLAYER = 3

  def __init__(self,width,height):
    # initialize the map manager with map size
    self.init_map(width,height)
    self.myPlayer    = Player(xPos=4,yPos=1)
    self.currentMap  = [[cell for cell in col] for col in self.originalMap]
    self.currentMap[self.myPlayer.xPos][self.myPlayer.yPos] = self._PLAYER

  def init_map(self,width=16,height=16):
    # create a map for the start of play
    self.originalMap = []
    for x in xrange(width):
      self.originalMap.append([])
      for y in xrange(height):
        self.originalMap[x].append(random.randint(0,2))


  def move_player(self,char):
    # track player movement based on keypress
    old_x = self.myPlayer.get_x_position()
    old_y = self.myPlayer.get_y_position()
    self.myPlayer.player_movement(movement=char)
    new_x = self.myPlayer.get_x_position()
    new_y = self.myPlayer.get_y_position()
    print 'old value: ',self.originalMap[old_x][old_y]
    self.currentMap[old_x][old_y] = self.originalMap[old_x][old_y]
    self.currentMap[new_x][new_y] = self._PLAYER