import numpy as np

winning_combos = np.array([[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]])

def calc_possible_tiles(board_tiles, bot_tiles, opp_tiles):
	for i in bot_tiles:
		tile_index = board_tiles.index(i)
		board_tiles.pop(tile_index)
	for i in opp_tiles:
		tile_index = board_tiles.index(i)
		board_tiles.pop(tile_index)
	return board_tiles

def select_tile(possible_tiles, bot_tiles, winStatus):
	print('these are the possible tiles:')
	print(possible_tiles)
	#choose tile:
	#tile_select = possible_tiles[0]	#choose first tile
	tile_select = possible_tiles[np.random.randint(len(possible_tiles))]	#choose random tile
	tile_index = possible_tiles.index(tile_select)
	print('bot selects tile %i' %tile_select)
	possible_tiles.pop(tile_index)
	print('now, the remaining tiles are:')
	print(possible_tiles)
	bot_tiles.append(tile_select)
	print('the bot has now selected these tiles:')
	print(bot_tiles)
	#see whether bot has won yet (does it have a any of the winning combos?)
	if len(bot_tiles) >= 3:
		for row in winning_combos:
			#print(list(row))
			row_comboMatch = set(list(row)).intersection(bot_tiles)
			row_comboCount = len(row_comboMatch)
			#print(row_comboMatch)
			#print(row_comboCount)
			if row_comboCount == 3:
				winStatus += 1

	return bot_tiles, winStatus


class simulateGame():

	def __init__(self):
		print('starting game')
		self.winStatus = 0
		self.bot_tiles = []
		self.opp_tiles = []

		self.playerTurn = ["bot", "opp", [np.random.randint(2)]]


	def simulate(self):
		print('starting simulation')
		while self.winStatus == 0:
			self.possible_tiles = calc_possible_tiles(list(np.arange(9)), self.bot_tiles, self.opp_tiles)
			if len(self.possible_tiles) > 0:
				if self.playerTurn == "bot":
					self.bot_tiles, self.winStatus = select_tile(self.possible_tiles, self.bot_tiles, self.winStatus)
					self.playerTurn = "opp"
					if self.winStatus > 0:
						print("bot WINS!")
				else:
					self.opp_tiles, self.winStatus = select_tile(self.possible_tiles, self.opp_tiles, self.winStatus)
					self.playerTurn = "bot"
					if self.winStatus > 0:
						print("opp WINS!")
			else:
				self.winStatus = 1
				print("DRAW!")

		print(self.bot_tiles)
		print(self.opp_tiles)

game = simulateGame()
game.simulate()
