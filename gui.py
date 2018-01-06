import random

from map_manager import Map_Manager
from Tkinter import *

class Dungeon_Gui():
  # tkinter class holder to render the map
  wallColor = ('#%02x%02x%02x'%(88,24,69))
  floorColor = ('#%02x%02x%02x'%(199,0,57))
  itemColor = ('#%02x%02x%02x'%(255,195,0))
  playerColor = ('#%02x%02x%02x'%(218,247,166))

  def __init__(self,width=16,height=16):
    # create the root window and start the mainloop
    root             = Tk()
    self.mm          = Map_Manager(width,height)
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

  def render_map(self):
    # redraw the map based on the map_manager.currentMap value
    pass

  def button_handler(self,event=None):
    # to do: have things update when the user enters a button press
    pass