import sys

from Tkinter import *
from map_manager import Map_Manager

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

    self.f           = Frame(self.root)

    # bind all key presses to the button handler
    self.root.bind("w",self.key_handler)
    self.root.bind("a",self.key_handler)
    self.root.bind("s",self.key_handler)
    self.root.bind("d",self.key_handler)

    # render based on the original map
    for x in xrange(width):
      self.pixelHolder.append([])
      for y in xrange(height):
        self.pixelHolder[x].append(Label(self.root,text='',width=2))
        self.pixelHolder[x][y].grid(row=y,column=x)

    # create buttons
    self.up    = Button(master=self.f,text=' UP  ',command=lambda: self.key_handler(char='w'))
    self.down  = Button(master=self.f,text='DOWN ',command=lambda: self.key_handler(char='s'))
    self.left  = Button(master=self.f,text='LEFT ',command=lambda: self.key_handler(char='a'))
    self.right = Button(master=self.f,text='RIGHT',command=lambda: self.key_handler(char='d'))

    self.quit = Button(master=self.f,text='Quit',command=self.on_exit)
    self.reset = Button(master=self.f,text='Redraw Map',command=self.scramble_map)

    self.up.grid(row=0,column=1)
    self.left.grid(row=1,column=0)
    self.down.grid(row=1,column=1)
    self.right.grid(row=1,column=2)
    self.quit.grid(row=0,column=4,sticky=E)
    self.reset.grid(row=1,column=4,sticky=E)

    self.f.grid(columnspan=width,sticky=S)
    self.render_map()
    self.root.protocol("WM_DELETE_WINDOW",self.on_exit)
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

  def on_exit(self):
    self.root.destroy()
    sys.exit()

  def scramble_map(self):
    self.mm.redraw_map()
    self.render_map()

  def key_handler(self,event=None,char=None):
    # to do: have things update when the user enters a button press
    print 'in key_handler'
    print 'event: ', event
    print 'char:  ', char
    if event is not None and event.char in 'wasd':
      print event.char
      # call the player movement function
      self.mm.move_player(event.char)
    if char is not None and char in 'wasd':
      print char
      self.mm.move_player(char)
    self.render_map()