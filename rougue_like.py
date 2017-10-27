class player():
	def __init__(self, health = 100, mana = 100, xPos = 0, yPos = 0):
		self.health = health
		self.mana = mana
		self.xPos = xPos
		self.yPos = yPos

class map_manager():
	_WALL = 0
	_FLOOR = 1
	_ITEM = 2
	_PLAYER = 3

	def __init__(self, width, height):
		self.originalMap = self.initMap(width, height)
		self.myPlayer = player()
		self.currentMap = self.originalMap
		self.currentMap[self.myPlayer.xPos][self.myPlayer.yPos] = _PLAYER
			
			# Generating a map without the player
		def init_map(self, width = 16, height = 16):
			self.originalMap = []
			for x in xrange(width):
				self.originalMap.append([])
				for y in yrange(height):
					self.originalMap[x].append(random.randint(0,2))
			return self.originalMap