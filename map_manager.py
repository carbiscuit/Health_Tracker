from player import Player

class Map_Manager():
  # class to update the map at the start of each turn and as turns progress
  _WALL = 0
  _FLOOR = 1
  _ITEM = 2
  _PLAYER = 3

  def __init__(self,width,height):
    # initialize the map manager with map size
    self.originalMap = self.init_map(width,height)
    self.myPlayer         = player(xPos=4,yPos=1)
    self.currentMap = self.originalMap
    self.currentMap[self.myPlayer.xPos][self.myPlayer.yPos] = self._PLAYER

  def init_map(self,width=16,height=16):
    # create a map for the start of play
    self.originalMap = []
    for x in xrange(width):
      self.originalMap.append([])
      for y in xrange(height):
        self.originalMap[x].append(random.randint(0,2))
    return self.originalMap