from time import sleep
from game import *

class TicTacToe2p(TicTacToe):
  def __init__(self, board=None):
    if board == None:
      self.board =  [['   ', ' | ', '   ', ' | ', '   '],
                  ['   ', ' | ', '   ', ' | ', '   '],
                  ['   ', ' | ', '   ', ' | ', '   ']]
    else:
      self.board = board
    self.winner = None
    
  
        
  def main(self):
    i = 0
    while self.winner == None:
      self.draw_board()
      self.check_winner()
      if len(self.check_available_moves()) == 0 or self.winner != None:
        break
      sleep(0.5)
      if i % 2 == 0:
        turn = "X"
      elif i :
        turn = "O"
      move = 0
      while True:
        try:
          move = int(input("\nMake a move (1-9): "))
          
          if move in self.check_available_moves():
            self.make_move(move, turn)
            break
          else:
            sleep(0.5)
            print("\nThat move is not available.")
        except:
          sleep(0.5)
          print("\nThat move is not valid.")
      print('\n\n')
      i += 1

    if self.winner != None:
      print(f"GG, The {self.winner} player wins!")
    elif len(self.check_available_moves()) == 0:
      print("Wow, solid game!")
