
class Player():
    """Models the attributes of the playable avatar."""

    def __init__(self, health=5, stamina=5, attack=1, defense=0, xPos=0, yPos=0):
        """Initialize player avatar attributes."""
        self.health = health
        self.stamina = stamina
        self.attack = attack
        self.defense = defense
        self.xPos = xPos
        self.yPos = yPos

    def player_movement(self):
        """Models the playable avatar's movement."""
            movement = input()
            if movement == 'w':
                self.yPos + 1
            elif movement == 'a':
                self.xPos - 1
            elif movement == 's':
                self.yPos - 1
            elif movement == 'd':
                self.xPos + 1
            """elif movement == 'r':
                self.stamina += 1"""