from time import sleep
from random import choice
from game import *

class TicTacToe1p(TicTacToe):
  def __init__(self, board=None):
    self.winner = None
    if board == None:
      self.board =  [['   ', ' | ', '   ', ' | ', '   '],
                  ['   ', ' | ', '   ', ' | ', '   '],
                          ['   ', ' | ', '   ', ' | ', '   ']]
    else:
      self.board = board
    
    

        
  def main(self):   
    i = 0   
    while self.winner == None:     
      self.check_winner()
      if len(self.check_available_moves()) == 0 or self.winner != None:
        break
      
      # Computer move
      print("\nBot's move...\n\n")
      sleep(1)
      comp_move = choice(self.check_available_moves())
      self.make_move(comp_move, "X")
      self.draw_board()
      self.check_winner()
      if len(self.check_available_moves()) == 0 or self.winner != None:
        break
      sleep(0.5)
      while True:
        try:
          move = int(input("\nMake a move (1-9): "))
          if move in self.check_available_moves():
            self.make_move(move, "O")
            break
          else:
            sleep(0.5)
            print("\nThat move is not available.")
          
        except:
          sleep(0.5)
          print("\nThat move is not valid.")
      print('\n\n')
      self.draw_board()
      
    if self.winner == "X":
      print("Sorry, you lost. ")

    elif self.winner == "O":
      print(f"GG, You won!")
    
    elif len(self.check_available_moves()) == 0:
      print("Wow, solid game!")
