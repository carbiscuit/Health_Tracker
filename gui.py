import sys
import time
import signal
import threading

from Tkinter import *
from map_manager import Map_Manager

class Dungeon_Gui():
  # tkinter class holder to render the map

  # constants for colors
  wallColor     = ('#%02x%02x%02x'%(88,24,69))
  floorColor    = ('#%02x%02x%02x'%(199,0,57))
  itemColor     = ('#%02x%02x%02x'%(255,195,0))
  projColor     = ('#%02x%02x%02x'%(100,140,230))
  playerColor   = ('#%02x%02x%02x'%(218,247,166))
  enenyOneColor = ('#%02x%02x%02x'%(142,247,12))
  healthColor   = ('#%02x%02x%02x'%(220,120,180))
  noHealthColor = ('#%02x%02x%02x'%(142,142,142))
  stamColor     = ('#%02x%02x%02x'%(100,140,230))
  noStamColor   = ('#%02x%02x%02x'%(142,142,142))

  def __init__(self,width=16,height=16,FPS=10):
    # create the root window and start the mainloop
    self.root        = Tk()
    self.exit_event  = threading.Event()
    self.mm          = Map_Manager(width,height,self.exit_event)
    self.player      = self.mm.myPlayer
    self.pixelHolder = []
    self.width       = width
    self.height      = height
    self.FPS         = FPS

    self.r_thread    = threading.Thread(target=self.render_thread)
    self.r_thread.setDaemon(True)

    # bind all key presses to the button handler
    self.root.bind("<KeyRelease-w>",self.key_handler)
    self.root.bind("<KeyRelease-a>",self.key_handler)
    self.root.bind("<KeyRelease-s>",self.key_handler)
    self.root.bind("<KeyRelease-d>",self.key_handler)
    self.root.bind("<KeyRelease-space>",self.attack_handler)

    # render based on the original map
    for x in xrange(width):
      self.pixelHolder.append([])
      for y in xrange(height):
        self.pixelHolder[x].append(Label(self.root,text='',width=2))
        self.pixelHolder[x][y].grid(row=y,column=x)

    # create buttons in a frame below the map
    self.f     = Frame(self.root)
    self.up    = Button(master=self.f,text=' UP  ',command=lambda: self.key_handler(char='w'))
    self.down  = Button(master=self.f,text='DOWN ',command=lambda: self.key_handler(char='s'))
    self.left  = Button(master=self.f,text='LEFT ',command=lambda: self.key_handler(char='a'))
    self.right = Button(master=self.f,text='RIGHT',command=lambda: self.key_handler(char='d'))

    self.quit  = Button(master=self.f,text='Quit',command=self.on_exit)
    self.reset = Button(master=self.f,text='Redraw Map',command=self.scramble_map)

    # create the player stats frame
    self.stats_frame         = Frame(self.f)
    self.player_health_label = Label(self.stats_frame,text='Player Health',
                                     justify=LEFT,width=20)
    self.player_health_label.grid(row=0,columnspan=10,sticky=W)
    self.playerHealthbar = []
    self.playerHealthbar = []
    for x in xrange(10):
      self.playerHealthbar.append(Label(self.stats_frame,text='',width=2))
      self.playerHealthbar[x].grid(row=1,column=x,sticky=W)
    
    self.player_stam_label = Label(self.stats_frame,text='Player Stamina',
                                     justify=LEFT,width=20)
    self.player_stam_label.grid(row=2,columnspan=10,sticky=W)
    self.playerStambar = []
    for x in xrange(10):
      self.playerStambar.append(Label(self.stats_frame,text='',width=2))
      self.playerStambar[x].grid(row=3,column=x,sticky=W)

    self.player_gold_label = Label(self.stats_frame,text='Gold: %d'%self.player.get_gold_amount())
    self.player_gold_label.grid(row=0,column=11,stick=W)

    # pack the buttons using the grid manager
    self.stats_frame.grid(columnspan=10,column=4,row=0,rowspan=4,sticky=E,padx=10)
    self.up.grid(row=2,column=1)
    self.left.grid(row=3,column=0)
    self.down.grid(row=3,column=1)
    self.right.grid(row=3,column=2)
    self.quit.grid(row=2,column=3,sticky=E)
    self.reset.grid(row=3,column=3,sticky=E)
    self.f.grid(columnspan=width,sticky=S)
    # override the standard signal.SIGINT response and define exit behavior
    signal.signal(signal.SIGINT, self.thread_safe_ctrl_c)
    self.root.protocol("WM_DELETE_WINDOW",self.on_exit)

    # start a thread to render the map and then begin the mainloop
    self.r_thread.start()
    self.root.mainloop()

  def thread_safe_ctrl_c(signal, frame):
    # method that is bound to the signal.SIGINT (keyboardInterrupt) to ensure
    # safe exit of threads when program closes
    print 'exiting threads safely'
    self.on_exit()

  def render_thread(self):
    # thread to handle map updates separate from the mainloop
    while not self.exit_event.is_set():
      self.render_map()
      time.sleep(1./self.FPS)

  def render_map(self):
    # redraw the map based on the map_manager.currentMap values
    fraction_of_healthbar = int(round(10.0*self.player.get_health()/self.player.get_max_health()))
    for x in xrange(len(self.playerHealthbar)):
      if x < fraction_of_healthbar:
        self.playerHealthbar[x].config(bg=self.healthColor)
      else:
        self.playerHealthbar[x].config(bg=self.noHealthColor)

    fraction_of_stambar = int(round(10.0*self.player.get_stam()/self.player.get_max_stam()))
    for x in xrange(len(self.playerStambar)):
      if x < fraction_of_stambar:
        self.playerStambar[x].config(bg=self.stamColor)
      else:
        self.playerStambar[x].config(bg=self.noStamColor)

    self.player_gold_label.config(text='Gold: %d'%self.player.get_gold_amount())
    for x in xrange(len(self.pixelHolder)):
      for y in xrange(len(self.pixelHolder[x])):
        if self.mm.get_pixel(x,y) == self.mm._WALL:
          self.pixelHolder[x][y].config(text='')
          self.pixelHolder[x][y].config(fg='#FFFFFF')
          self.pixelHolder[x][y].config(bg=self.wallColor)
        elif self.mm.get_pixel(x,y) == self.mm._FLOOR:
          self.pixelHolder[x][y].config(text='')
          self.pixelHolder[x][y].config(fg='#FFFFFF')
          self.pixelHolder[x][y].config(bg=self.floorColor)
        elif self.mm.get_pixel(x,y) == self.mm._ITEM:
          self.pixelHolder[x][y].config(text='G')
          self.pixelHolder[x][y].config(fg='#FFFFFF')
          self.pixelHolder[x][y].config(bg=self.itemColor)
        elif self.mm.get_pixel(x,y) == self.mm._PROJECTILE:
          self.pixelHolder[x][y].config(text='')
          self.pixelHolder[x][y].config(fg='#FFFFFF')
          self.pixelHolder[x][y].config(bg=self.projColor)
        elif self.mm.get_pixel(x,y) == self.mm._PLAYER:
          if self.player.get_facing()[:] == 'east':
            self.pixelHolder[x][y]['text'] ='>'
          elif self.player.get_facing()[:] == 'west':
            self.pixelHolder[x][y]['text'] ='<'
          elif self.player.get_facing()[:] == 'north':
            self.pixelHolder[x][y]['text'] ='^'
          else:
            self.pixelHolder[x][y]['text'] ='v'
          self.pixelHolder[x][y].config(fg='#000000')
          self.pixelHolder[x][y].config(bg=self.playerColor)
        elif self.mm.currentMap[x][y] == self.mm._ENEMY:
          self.pixelHolder[x][y]['text'] ='V'
          self.pixelHolder[x][y].config(fg='#BBCCAA')
          self.pixelHolder[x][y].config(bg=self.enenyOneColor)

  def on_exit(self):
    self.exit_event.set()
    time.sleep(0.5)
    self.root.destroy()
    sys.exit()

  def scramble_map(self):
    self.mm.redraw_map()

  def attack_handler(self,event=None):
    # have the player fire a projectile when the spacebar is released
    print 'in attack handler'
    if event is not None:
      self.mm.track_projectile()

  def key_handler(self,event=None,char=None):
    # have player and enemy position update when the user enters char in 'wasd'
    print 'in key_handler'
    #print 'event: ', event.keysym
    #print 'char:  ', char
    if event is not None and event.keysym in 'wasd':
      print event.char
      # call the player movement function
      self.mm.move_player(event.char)
      self.mm.move_enemy_one(event.char)
    if char is not None and char in 'wasd':
      print char
      self.mm.move_player(char)
      self.mm.move_enemy_one(char)

