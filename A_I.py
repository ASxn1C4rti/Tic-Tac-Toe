import random
import numpy as np
import math
import time

board = np.zeros((3, 3))
player = 2
bot = 1
translation = { 0 : ' ',
              1 : 'X',
              2 : 'O'}
        
def insertLetter(player, pos, board):
  pos -= 1
  x, y = [pos//3, pos%3]
  board[x][y] = player
  
def spaceIsFree(pos, board):
   pos -= 1
   x, y = [pos//3, pos%3]
   return board[x][y] == 0
  
def printBoard(board):
  print()
  for row in range(len(board)):
    print('              ', end=' ')
    print( '   |   '.join(translation[col] for col in board[row]))
    if row != len(board) - 1:
       print('\n             _____   _____   _____\n') 
      
  
  
def isWinner(player, board):
  # Horizontal
  for row in range(3):
    check = [True if i == player else False  for i in board[row, :]]
    if all(check):
      return player
    
  # Vertical
  for col in range(len(board)):
    check = [True if i == player else False for i in board[:, col]]
    
    if all(check):
      return player
    
  # Diagonal
  if all([True if i == player else False for i in board[(0, 1, 2), (0, 1, 2)]]) or all([True if i == player else False for i in board[(0, 1, 2), (2, 1, 0)]]):
    return player
  return None
  
def playerMove():
  move = 0
  while True:
    try:
      move = int(input('\nMake a move (1-9): '))
      if spaceIsFree(move, board):
        break
      else:
        print('\nUnavailable move')
    except:
      print('\nInvalid move')
  return move
  
    
  


def compMove():
    bestScore = -math.inf
    bestMove = None
  
    for row in range(9):
      if spaceIsFree(row+1, board):
        board[row//3][row%3] = bot
        score = minimax(board, 1, False)
        board[row//3][row%3] = 0
        if score > bestScore:
          bestScore = score
          bestMove = row + 1
        

        
    return bestMove
    
def evaluate(board):
    spaces = sum([1 for i in range(1, 10) if spaceIsFree(i, board)])
  
    if isWinner(bot, board):
      return [True, 1 * (spaces + 1)]
  
    if isWinner(player, board):
      return [True,(-1) * (spaces + 1)]
  
    if isBoardFull(board):
      return [True, 0]
    
    return [False, None]
    
def minimax(board, depth, isMaximizing):
    
    if evaluate(board)[0]:
      return evaluate(board)[1]
    
    
    if isMaximizing:
      bestScore = -math.inf
  
      for row in range(9):
        if spaceIsFree(row+1, board):
          board[row//3][row%3] = bot
          score = minimax(board, depth + 1, False)
          board[row//3][row%3] = 0
          if score > bestScore:
            bestScore = score
      return bestScore
    else:
      bestScore = math.inf
  
      for row in range(9):
        if spaceIsFree(row+1, board):
          board[row//3][row%3] = player
          score = minimax(board, depth + 1, True)
          board[row//3][row%3] = 0
          if score < bestScore:
            bestScore = score
      return bestScore
  
def randomMove(board):
  available = []
  for row in range(1, 10):
    if spaceIsFree(row, board):
      available.append(row)
  return random.choice(available)
  
def isBoardFull(board):
  for row in board:
    for col in row:
      if col == 0:
        return False
  return True

def compFirstMove1():
  return random.choice(range(1, 10, 4))
  
def compFirstMove2():
  if spaceIsFree(5, board):
    return 5
  
  return random.choice([i for i in range(1, 10, 2) if spaceIsFree(i, board)])
  
# Main Game
def AI():
  global player, bot, board
  board = np.zeros((3, 3))
  winner = None
  cmoves = 0
  print()
  while winner == None and not isBoardFull(board):
      
    # Computer
    if cmoves == 0:
      cmove = compFirstMove1()
      cmoves += 1
    else:
      print("\nComputer is calculating...\n")
      cmove = compMove()
      cmoves += 1
      
    insertLetter(bot, cmove, board)
    winner = isWinner(bot, board)
    printBoard(board)
    time.sleep(1)
    if isBoardFull(board) or winner != None:
      break
      
    # Player
    pmove = playerMove()
    insertLetter(player, pmove, board)
    winner = isWinner(player, board)
    printBoard(board)
    time.sleep(0.2)  
      
  # Result  
  if winner != None:
    print(f'\n{translation[winner]} wins!')
  else:
    print('\nTie!')
