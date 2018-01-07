import random
import copy
from projectile import Projectile


class Player(object):
    """Models the attributes of the playable avatar."""

    def __init__(self, health=5, stamina=5, gold=0,
                attack=1, defense=0, xPos=0, yPos=0):
        """Initialize player avatar attributes."""
        self.health      = health
        self.max_health  = health
        self.stamina     = stamina
        self.max_stamina = stamina
        self.gold        = gold
        self.attack      = attack
        self.defense     = defense
        self.xPos        = xPos
        self.yPos        = yPos
        self.facing      = 'east'
        self.alive       = True
        self.attack      = Projectile(xPos,yPos,attack,refresh_time=0.1)

    def _is_alive(self):
        return self.alive

    def _kill(self):
        self.alive = False

    def set_x_position(self,value):
        self.xPos = value

    def set_y_position(self,value):
        self.yPos = value

    def set_facing(self,value):
        self.facing = value

    def set_health(self,value):
        self.health = value

    def set_max_health(self,value):
        self.max_health = value

    def get_health(self):
        return self.health

    def get_max_health(self):
        return self.max_health

    def set_stam(self,value):
        self.stamina = value

    def set_max_stam(self,value):
        self.max_stamina = value

    def get_attack(self):
        return self.attack

    def get_stam(self):
        return self.stamina

    def get_max_stam(self):
        return self.max_stamina

    def get_x_position(self):
        return self.xPos

    def get_y_position(self):
        return self.yPos

    def get_facing(self):
        return self.facing

    def get_gold_amount(self):
        # Reads the current amount of gold the player has.
        return self.gold

    def acquire_gold(self, gold_to_add):
        # Adds a specified amount of gold to players inventory.
        self.gold += gold_to_add

    def decrease_health(self,value):
        self.health -= value
        if self.health <= 0:
            self._kill()

    def shoot_projectile(self):
        new_proj = copy.copy(self.attack)
        new_proj.set_y_position(self.yPos)
        new_proj.set_x_position(self.xPos)
        new_proj.set_facing(self.facing)
        return new_proj

    def player_movement(self,movement):
        print 'moving player from Player'
        """Models the playable avatar's movement."""
        #movement = input()
        if movement == 'w':
            self.yPos -= 1
            self.facing = 'north'
        elif movement == 'a':
            self.xPos -= 1
            self.facing = 'west'
        elif movement == 's':
            self.yPos += 1
            self.facing = 'south'
        elif movement == 'd':
            self.xPos += 1
            self.facing = 'east'
        """elif movement == 'r':
            self.stamina += 1"""

        return ({'x':self.xPos,'y':self.yPos})


class Enemy_One(Player):
    def __init__(self,health=5, stamina=5, attack=1, defense=0, xPos=0, yPos=0):
        super(Enemy_One, self).__init__(health=health, stamina=stamina, 
            attack=attack, defense=defense, xPos=xPos, yPos=yPos)
        self.attack = attack # we don't want the enemy to have projectile, but it 
                             # needs some integer attack value, so overright the old
                             # projectile that the super init creates
    def decrease_health(self,value):
            self.health -= value
            if self.health <= 0:
                self._kill()
            print 'enemy health: ',self.get_health()
            print 'killed:       ',not self._is_alive()

    def player_movement(self, movement):
        print 'moving enemy_one from Enemy_One'
        random_enemy_one_int = random.randint(1,4)
        if movement == 'w' or 'a' or 's' or 'd':
            if random_enemy_one_int == 1:
                self.xPos += 1
            elif random_enemy_one_int == 2:
                self.xPos -= 1
            elif random_enemy_one_int == 3:
                self.yPos += 1
            elif random_enemy_one_int == 4:
                self.yPos -= 1

        return {'x':self.xPos,'y':self.yPos}
