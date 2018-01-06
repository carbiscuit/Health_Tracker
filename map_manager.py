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
    self.width       = width
    self.height      = height

    self.originalMap[self.myPlayer.xPos][self.myPlayer.yPos] = self._FLOOR
    self.currentMap  = [col[:] for col in self.originalMap]
    self.currentMap[self.myPlayer.xPos][self.myPlayer.yPos] = self._PLAYER

  def init_map(self,width=16,height=16):
    # create a map for the start of play
    self.originalMap = []
    for x in xrange(width):
      self.originalMap.append([])
      for y in xrange(height):
        if x==0 or y==0 or x==width-1 or y==height-1:
          self.originalMap[x].append(self._WALL)
        else:
          self.originalMap[x].append(random.randint(0,2))

  def _is_wall(self,x,y):
    """Returns a '0' for wall."""
    return self.currentMap[x][y] == self._WALL

  def _is_item(self,x,y):
    """Returns a '2' for item."""
    return self.currentMap[x][y] == self._ITEM

  def _is_empty(self,x,y):
    """Returns a '1' for floor."""
    return self.currentMap[x][y] == self._FLOOR

  def _is_in_bounds(self,x,y):
    """Checks in-bound paramters."""
    return x >= 0 and y >= 0 and x < self.width and y < self.height

  def move_player(self,char):
    # track player movement based on keypress and prevent illegal moves.
    old_x = self.myPlayer.get_x_position()
    old_y = self.myPlayer.get_y_position()
    self.myPlayer.player_movement(movement=char)
    new_x = self.myPlayer.get_x_position()
    new_y = self.myPlayer.get_y_position()

    if not self._is_in_bounds(new_x,new_y):
      new_x = old_x
      new_y = old_y
      self.myPlayer.set_x_position(old_x)
      self.myPlayer.set_y_position(old_y)
    elif self._is_wall(new_x,new_y):
      new_x = old_x
      new_y = old_y
      self.myPlayer.set_x_position(old_x)
      self.myPlayer.set_y_position(old_y)
    elif self._is_item(new_x,new_y):
      self.originalMap[new_x][new_y] = self._FLOOR

    self.currentMap[old_x][old_y] = self.originalMap[old_x][old_y]
    self.currentMap[new_x][new_y] = self._PLAYER