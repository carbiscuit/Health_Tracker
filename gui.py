from Tkinter import *
import random
#import rouge_like

class map_manager():
  _WALL = 0
  _FLOOR = 1
  _ITEM = 2
  _PLAYER = 3

  def __init__(self,width,height):
    self.originalMap = self.init_map(width,height)
    self.myPlayer         = player(xPos=4,yPos=1)
    self.currentMap = self.originalMap
    self.currentMap[self.myPlayer.xPos][self.myPlayer.yPos] = self._PLAYER

  def init_map(self,width=16,height=16):
    self.originalMap = []
    for x in xrange(width):
      self.originalMap.append([])
      for y in xrange(height):
        self.originalMap[x].append(random.randint(0,2))
    return self.originalMap

class player():
  def __init__(self,health=100,mana=100,xPos=0,yPos=0):
    self.health = health
    self.mana = mana
    self.xPos = xPos
    self.yPos = yPos

class dungeon_gui():
  wallColor = ('#%02x%02x%02x'%(88,24,69))
  floorColor = ('#%02x%02x%02x'%(199,0,57))
  itemColor = ('#%02x%02x%02x'%(255,195,0))
  playerColor = ('#%02x%02x%02x'%(218,247,166))
  def __init__(self,width=16,height=16):
    root = Tk()
    mm   = map_manager(width,height)
    self.pixelHolder = []
    for x in xrange(width):
      self.pixelHolder.append([])
      for y in xrange(height):
        if mm.originalMap[x][y] == mm._WALL:
          tmpText  = 'X'
          tmpTextColor = '#FFFFFF'
          tmpColor = self.wallColor
        elif mm.originalMap[x][y] == mm._FLOOR:
          tmpText  = ' '
          tmpTextColor = '#FFFFFF'
          tmpColor = self.floorColor
        elif mm.originalMap[x][y] == mm._ITEM:
          tmpText  = 'G'
          tmpTextColor = '#FFFFFF'
          tmpColor = self.itemColor
        else:
          tmpText  = '@'
          tmpTextColor = '#000000'
          tmpColor = self.playerColor
        self.pixelHolder[x].append(Label(root,text=tmpText,fg=tmpTextColor,bg=tmpColor,width=2))
        self.pixelHolder[x][y].grid(row=y,column=x)
    root.mainloop()
