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
    self.root        = Tk()
    self.mm          = Map_Manager(width,height)
    self.pixelHolder = []
    self.width       = width
    self.height      = height

    # bind all key presses to the button handler
    self.root.bind("<Key>",self.key_handler)

    # render based on the original map
    for x in xrange(width):
      self.pixelHolder.append([])
      for y in xrange(height):
        self.pixelHolder[x].append(Label(self.root,text='',width=2))
        self.pixelHolder[x][y].grid(row=y,column=x)

    self.render_map()
    self.root.mainloop()

  def render_map(self):
    # redraw the map based on the map_manager.currentMap values
    for x in xrange(len(self.pixelHolder)):
      for y in xrange(len(self.pixelHolder[x])):
        if self.mm.currentMap[x][y] == self.mm._WALL:
          self.pixelHolder[x][y]['text'] ='X'
          self.pixelHolder[x][y].config(fg='#FFFFFF')
          self.pixelHolder[x][y].config(bg=self.wallColor)
        elif self.mm.currentMap[x][y] == self.mm._FLOOR:
          self.pixelHolder[x][y]['text'] =' '
          self.pixelHolder[x][y].config(fg='#FFFFFF')
          self.pixelHolder[x][y].config(bg=self.floorColor)
        elif self.mm.currentMap[x][y] == self.mm._ITEM:
          self.pixelHolder[x][y]['text'] ='G'
          self.pixelHolder[x][y].config(fg='#FFFFFF')
          self.pixelHolder[x][y].config(bg=self.itemColor)
        else:
          self.pixelHolder[x][y]['text'] ='@'
          self.pixelHolder[x][y].config(fg='#000000')
          self.pixelHolder[x][y].config(bg=self.playerColor)
    self.root.after(100,self.render_map)



  def key_handler(self,event=None):
    # to do: have things update when the user enters a button press
    if event.char in 'wasd':
      # call the player movement function
      self.mm.move_player(event.char)

      # make sure that the mm.currentMap has been updated
      # then finally redraw the new map
      self.render_map()