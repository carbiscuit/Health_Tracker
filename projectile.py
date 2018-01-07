class Projectile:
  def __init__(self, xPos, yPos, damage=1, facing='east', refresh_time=0.25):
    self.xPos         = xPos
    self.yPos         = yPos
    self.damage       = damage
    self.facing       = facing
    self.refresh_time = refresh_time
    self.alive        = True

  def calc_next_position(self):
    if self.facing[:] == 'east':
      self.xPos+=1
    elif self.facing[:] == 'west':
      self.xPos-=1
    elif self.facing[:] == 'south':
      self.yPos+=1
    else:
      self.yPos-=1

  def _is_alive(self):
    return self.alive

  def _kill(self):
    self.alive = False

  def get_refresh_time(self):
    return self.refresh_time

  def get_x_position(self):
    return self.xPos

  def get_y_position(self):
    return self.yPos

  def get_facing(self):
    return self.facing

  def get_attack(self):
    return self.damage

  def set_x_position(self, value):
    self.xPos = value

  def set_y_position(self, value):
    self.yPos = value

  def set_facing(self, value):
    self.facing = value
