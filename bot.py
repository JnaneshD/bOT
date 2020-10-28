class Fight:
	def __init__(self):
		self.game = 0
		self.rows = 0
		self.cols = 0
		self.possible_moves = [[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
	def make_board(self):
		self.board = [['' for i in range(self.cols)] for i in range(self.rows)]
	def populate(self,x,y,ch):
		for move in self.possible_moves:
			if (self.rows>x+move[0]>=0 and self.cols>y+move[1]>=0 and self.board[x+move[0]][y+move[1]]==""):
				self.board[x+move[0]][y+move[1]] = ch
	def move_opponent(self,x,y):
		self.board[x][y] = 'O'
		self.populate(x,y,'O')
	def Score(self,x,y):
		count = 0
		for move in self.possible_moves:
			if (self.rows>x+move[0]>=0 and self.cols>y+move[1]>=0):
				if(self.board[x+move[0]][y+move[1]]=='X' or self.board[x+move[0]][y+move[1]]==''):
					count+=1
		return count
	def makeMove(self):
		cur_max = 0
		max_pos = [0,0]
		for i in range(self.rows):
			for j in range(self.cols):
				score = self.Score(i,j)
				if(self.board[i][j]==''):
					if(score==8):
						self.board[i][j] = 'X'
						self.populate(i,j,'X')
						return [i,j]
					if(score>cur_max):
						cur_max = score
						max_pos[0],max_pos[1] = i,j
		if(cur_max>0):
			self.board[max_pos[0]][max_pos[1]] = 'X'
			self.populate(max_pos[0],max_pos[1],'X')
			return [max_pos[0],max_pos[1]]
		else:
			return False
	def run(self):
		x = True
		while(x):
			inp = input()
			args = inp.split()
			condition = args[0]
			if(condition=="BOARD_INIT"):
				self.rows = int(args[1])
				self.cols = int(args[2])
				self.make_board()
				print("0")
			elif(condition=="MAKE_MOVE"):
				array = self.makeMove()
				if(array):
					print(array[0],array[1])
				else:
					print("GAME_OVER")
			elif(condition=="OPPONENT_MOVE"):
				opnt_x = int(args[1])
				opnt_y = int(args[2])
				self.move_opponent(opnt_x,opnt_y)
				print("0")
			elif(condition=="OBSTRUCTION"):
				obs_x = int(args[1])
				obs_y = int(args[2])
				self.board[obs_x][obs_y] = '0'
				print("0")
				pass
			elif(condition=="PRINT"):
				for i in self.board:
					print(i)
			else:
				print("INVALID_ARGUEMENT")
if __name__=="__main__":
	g = Fight()
	g.run()