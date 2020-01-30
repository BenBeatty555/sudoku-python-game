# X X X  || X X X  || X X X
# X X X  || X X X  || X X X
# X X X  || X X X  || X X X
# =====     =====     =====
# X X X  || X X X  || X X X
# X X X  || X X X  || X X X
# X X X  || X X X  || X X X
# =====     =====     =====
# X X X  || X X X  || X X X
# X X X  || X X X  || X X X
# X X X  || X X X  || X X X

import argparse
import sys
import tkinter as tk

PUZZLE_SIZE = 9

def main():
	parser = argparse.ArgumentParser(description='Process a sudoku puzzle and output the result')
	parser.add_argument('--count',action='store_true',help="count the number of moves needed")
	parser.add_argument('--steps',action='store_true',help="show all the steps to solve")
	args = parser.parse_args()
	
	board = [
	['X', 8 ,'X',   'X', 2 ,'X',    4 , 7 ,'X'], 
	['X', 3 , 4 ,    5 , 8 ,'X',   'X','X', 2 ],
	['X', 1 , 9 ,   'X','X','X',   'X', 3 , 8 ],
	
	[ 5 ,'X', 8 ,    4 , 7 ,'X',    9 ,'X','X'],
	['X', 4 , 2 ,   'X', 5 ,'X',    6 , 8 ,'X'],
	['X', 9 ,'X',    6 , 3 ,'X',   'X','X','X'],
	
	['X','X','X',   'X','X','X',   'X', 4 , 5 ],
	['X', 5 , 1 ,    3 , 9 ,'X',    7 ,'X','X'],
	[ 4 ,'X', 3 ,   'X','X', 5 ,   'X', 9 , 1 ]
	]

	#solve(board)

	t(board)
	

# solve
#  input: board: a 2d array of tuples, (number,True) or (x,False) if empty
#  output: 
def solve(board):

	x,y=empty_place(board)
	
	if x>PUZZLE_SIZE:
		return True
	
	for i in range(1,10):
		if valid_place(board,i,(x,y)):
			board[x][y] = i
			if solve(board):
				return True
			board[x][y]='X'
			
	return False
	
# valid_place
#  input: board: a 2d array of tuples, (number,True) or (x,False) if empty
#         number: the number that is being checked at the current position
#         pos: the position for the number as a tuple
#  output: true if valid or false if not
def valid_place(board,number,pos):
	x,y = pos
	#across
	for i in range(PUZZLE_SIZE):
		num = board[x][i]
		if i != y:
			if number == num:
				return False
	#vertical 
	for i in range(PUZZLE_SIZE):
		num = board[i][y]
		if i != x:
			if number == num:
				return False
	#group
	for i in range(PUZZLE_SIZE):
		for j in range(PUZZLE_SIZE):
			if (i//3 == x//3) and (j//3 == y//3) and not (i==x and j==y):
				num = board[i][j]
				#print(i,j,x,y,num,number)
				if num == number:
					return False
	return True
# empty_place
#  input: board: a 2d array of tuples, (number,True) or (x,False) if empty
#         pos: the position to check empty as a tuple
#  output: tuple of (x,y)
def empty_place(board):
	x,y = 0,0
	
	for i in range(x,9):
		for j in range(y,9):
			if board[i][j]=='X':
				return (i,j)
	return (PUZZLE_SIZE+1,PUZZLE_SIZE+1)
	
def t(board):
	root = tk.Tk()
	root.title("Sudoku")
	text_vars = []
	for i in range(PUZZLE_SIZE):
		text_vars.append([])
		for j in range(PUZZLE_SIZE):
			text_vars[len(text_vars)-1].append(tk.StringVar(root))
			if board[j][i] != 'X':#if number is filled already
				text_vars[i][j].set(board[j][i])
				entry = tk.Entry(root,width=5,justify='center',borderwidth=1,font='Helvetica 8 bold',textvariable=text_vars[i][j])
				
			else:#number entry is empty
				entry = tk.Entry(root,width=5,justify='center',borderwidth=1,textvariable=text_vars[i][j])
			entry.grid(column=2*i+1,row=2*j+1,ipady=5)
	for i in range(PUZZLE_SIZE//3-1):
		for j in range(PUZZLE_SIZE//3-1):
			l = tk.Label(root,text="",width=1,font=("Helvetica", 2))
			l.grid(column=6*(i+1),row=6*(j+1))
	tk.Button ( root,text ="Solve",command=lambda :do_button(text_vars,board),font='Helvetica 7').grid(column=1,row=18)
	root.mainloop()

def do_button(text_vars,board):
	print('solveing...')
	if solve(board):
		for i in range(PUZZLE_SIZE):
			for j in range(PUZZLE_SIZE):
				text_vars[i][j].set(board[j][i])
				#print(text_vars[i][j].get())
				#text_vars[0][0].set(5)
		print('solved')
	
	else:
		print('unsolvible')
	
if __name__ == '__main__':
    main()
