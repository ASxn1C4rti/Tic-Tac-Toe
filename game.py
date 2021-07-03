class TicTacToe:
  
    
  def check_available_moves(self):
    empty_moves = []
    number = 0
    for row in self.board:
      for column in row:
        if column != ' | ':
          number += 1
        if column ==  '   ':
          empty_moves.append(number)
    return empty_moves

  def draw_board(self):
    i = 0
    for row in self.board:
      for column in row:
        if i == 0 or i == 5 or i == 10:
          print("             ", end=' ')
        if i != 4 and i != 9:
          print(column, end=' ')
        else:
          print(column)
          print('\n             _____   _____   _____\n')
        i += 1
    print("\n")    
    
  def check_winner(self):
    # X Player
    if self.board[0][0].strip() == 'X' and self.board[0][2].strip() == 'X' and self.board[0][4].strip() == 'X':
      self.winner = 'X'
    elif self.board[1][0].strip() == 'X' and self.board[1][2].strip() == 'X' and self.board[1][4].strip() == 'X':
      self.winner = 'X'
    elif self.board[2][0].strip() == 'X' and self.board[2][2].strip() == 'X' and self.board[2][4].strip() == 'X':
      self.winner = 'X'
    elif self.board[0][0].strip() == 'X' and self.board[1][0].strip() == 'X' and self.board[2][0].strip() == 'X':
      self.winner = 'X'
    elif self.board[0][2].strip() == 'X' and self.board[1][2].strip() == 'X' and self.board[2][2].strip() == 'X':
      self.winner = 'X'
    elif self.board[0][4].strip() == 'X' and self.board[1][4].strip() == 'X' and self.board[2][4].strip() == 'X':
      self.winner = 'X'
    elif self.board[0][0].strip() == 'X' and self.board[1][2].strip() == 'X' and self.board[2][4].strip() == 'X':
      self.winner = 'X'
    elif self.board[0][4].strip() == 'X' and self.board[1][2].strip() == 'X' and self.board[2][0].strip() == 'X':
      self.winner = 'X'
    
    # O Player
    if self.board[0][0].strip() == 'O' and self.board[0][2].strip() == 'O' and self.board[0][4].strip() == 'O':
      self.winner = 'O'
    elif self.board[1][0].strip() == 'O' and self.board[1][2].strip() == 'O' and self.board[1][4].strip() == 'O':
      self.winner = 'O'
    elif self.board[2][0].strip() == 'O' and self.board[2][2].strip() == 'O' and self.board[2][4].strip() == 'O':
      self.winner = 'O'
    elif self.board[0][0].strip() == 'O' and self.board[1][0].strip() == 'O' and self.board[2][0].strip() == 'O':
      self.winner = 'O'
    elif self.board[0][4].strip() == 'O' and self.board[1][4].strip() == 'O' and self.board[2][4].strip() == 'O':
      self.winner = 'O'
    elif self.board[0][2].strip() == 'O' and self.board[1][2].strip() == 'O' and self.board[2][2].strip() == 'O':
      self.winner = 'O'
    elif self.board[0][0].strip() == 'O' and self.board[1][2].strip() == 'O' and self.board[2][4].strip() == 'O':
      self.winner = 'O'
    elif self.board[0][4].strip() == 'O' and self.board[1][2].strip() == 'O' and self.board[2][0].strip() == 'O':
      self.winner = 'O'
    
  def make_move(self, n, turn):
    if n not in self.check_available_moves():
      print("\nUnavailable moves")
      return False
    elif n == 1:
      self.board[0][0] = ' ' + turn + ' '
    elif n == 2:
      self.board[0][2] = ' ' + turn + ' '
    elif n == 3:
      self.board[0][4] = ' ' + turn + ' '
    elif n == 4:
      self.board[1][0] = ' ' + turn + ' '
    elif n == 5:
      self.board[1][2] = ' ' + turn + ' '
    elif n == 6:
      self.board[1][4] = ' ' + turn + ' '
    elif n == 7:
      self.board[2][0] = ' ' + turn + ' '
    elif n == 8:
      self.board[2][2] = ' ' + turn + ' '
    elif n == 9:
      self.board[2][4] = ' ' + turn + ' '
