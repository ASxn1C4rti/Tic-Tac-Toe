
from ply1 import*
from ply2 import*
from A_I import *
from time import sleep  
  

if __name__=='__main__':
  print()
  print("Tic Tac Toe by xASonicMenx".center(46))
  sleep(1)
  guide_board = [[' 1 ', ' | ', ' 2 ', ' | ', ' 3 '],
                 [' 4 ', ' | ', ' 5 ', ' | ', ' 6 '],
                 [' 7 ', ' | ', ' 8 ', ' | ', ' 9 ']]
                 
  i = 0
  print()
  print((" BOARD POSITION ").center(46,"="))
  print()
  for row in guide_board:
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
  sleep(1)
  
  while True:
    print()
    print(" MAIN MENU ".center(46, '='))
    print()
    print('Choose one'.center(46))
    mode = 0
    while mode not in [1, 2, 3, 4]:
      try:
        mode = int(input("""\n[1] vs A.I.
[2] vs Computer
[3] 2 Player
[4] Quit\n\n>>"""))

      except Exception:
        print("\nThat's not a number...")
    if mode == 1:
      AI()
    elif mode == 2:
      main = TicTacToe1p()
      main.main()
    elif mode == 3:
      main = TicTacToe2p()
      main.main()
    else:
      break
  print("\nTHANKS FOR PLAYING.\nCONSIDER GIVING IT A STAR IF YOU LIKE IT.")
