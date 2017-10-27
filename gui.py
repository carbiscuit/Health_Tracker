from Tkinter import *
import rouge_like

class dungeon_gui():
  self.wallColor = ('#%02x%02x%02x'%(88,24,69))
  self.floorColor = ('#%02x%02x%02x'%(199,0,57))
  self.itemColor = ('#%02x%02x%02x'%(255,195,0))
  self.playerColor = ('#%02x%02x%02x'%(218,247,166))
  def __init__():
    root = Tk()
    width = 16
    height = 16
    mm   = map_manager(width,height)
    self.pixelHolder = []
    for x in xrange(width):
      self.pixelHolder.append([])
      for y in xrange(height):
        if mm.originalMap[x][y] == mm._WALL:
          tmpText  = 'X'
          tmpColor = self.wallColor
        elif mm.originalMap[x][y] == mm._FLOOR:
          tmpText  = ' '
          tmpColor = self.floorColor
        elif mm.originalMap[x][y] == mm._ITEM:
          tmpText  = 'G'
          tmpColor = self.itemColor
        else:
          tmpText  = '@'
          tmpColor = self.playerColor
        self.pixelHolder[x].append(Label(root,text=tmpText,fg='#FFFFFF',bg=tmpColor,width=1))
        self.pixelHolder[x][y].grid(row=y,column=x)
    root.mainloop()
