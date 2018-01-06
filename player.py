import random

class Player(object):
    """Models the attributes of the playable avatar."""

    def __init__(self, health=5, stamina=5, gold=0,
                attack=1, defense=0, xPos=0, yPos=0):
        """Initialize player avatar attributes."""
        self.health = health
        self.stamina = stamina
        self.gold = gold
        self.attack = attack
        self.defense = defense
        self.xPos = xPos
        self.yPos = yPos

    def set_x_position(self,value):
        self.xPos = value

    def set_y_position(self,value):
        self.yPos = value

    def get_x_position(self):
        return self.xPos

    def get_y_position(self):
        return self.yPos

    def get_gold_amount(self):
        # Reads the current amount of gold the player has.
        return self.gold

    def acquire_gold(self, gold_to_add):
        # Adds a specified amount of gold to players inventory.
        self.gold += gold_to_add

    def player_movement(self,movement):
        print 'moving player from Player'
        """Models the playable avatar's movement."""
        #movement = input()
        if movement == 'w':
            self.yPos -= 1
        elif movement == 'a':
            self.xPos -= 1
        elif movement == 's':
            self.yPos += 1
        elif movement == 'd':
            self.xPos += 1
        """elif movement == 'r':
            self.stamina += 1"""

        return ({'x':self.xPos,'y':self.yPos})

class Enemy_One(Player):
    def __init__(self,health=5, stamina=5, attack=1, defense=0, xPos=0, yPos=0):
        super(Enemy_One, self).__init__(health=3, stamina=5, 
            attack=1, defense=0, xPos=8, yPos=8)

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
