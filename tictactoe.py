#!/usr/bin/env python
#from IPython.display import clear_output
import os


def DisplayBoard(board):
  #clear_output()
  os.system('clear')
  print('check 1')
  print(board[7]+'|'+board[8]+'|'+board[9])
  print("-----")
  print(board[4]+'|'+board[5]+'|'+board[6])
  print("-----")
  print(board[1]+'|'+board[2]+'|'+board[3])

def PlayerAssignment():
  Player1 = ''
  while not(Player1 == 'X' or Player1 =='O'):
    marker = input('Player 1 please select either X or O: ')
    Player1 = marker.upper()

  if Player1 == 'X':
    return ['X','O']
  else:
    return ['O','X']

def PlayerMove(board,player):
  """
  
  """
  count = 0
  while count < 5:
    marker = input('Player '+player+' please make a move. (keys 1-9) : ')
    if marker.isnumeric() and int(marker) < 10 and int(marker) > 0:
      if board[int(marker)] == ' ':
        return int(marker)
      else:
        print('That position is taken')
    else:
      print('That is not an appropriate move.')
    count += 1
  print('5 unsuccessful attempst have been made to make a move, you are probably just screwing around right now...')
  return 0

def CheckWin(board):
  """
  This function checks if there are any wins currently on the Tic-Tac-Toe board.  To win a player must have at least
  1 of square 1, 5, and 9.  Thus these squares are focused on. If none of them are taken then no win has occurred.
  """
  if board[1] == 'X' or board[1] == 'O':
    if board[1]==board[2]==board[3]:
        return board[1]
    elif board[1]==board[4]==board[7]:
        return board[1]
    elif board[1]==board[5]==board[9]:
        return board[1]
  if board[5] == 'X' or board[5] == 'O':
    if board[5]==board[3]==board[7]:
        return board[5]
    elif board[5]==board[4]==board[6]:
        return board[5]
    elif board[5]==board[2]==board[8]:
        return board[5]
  if board[9] == 'X' or board[9] == 'O':
    if board[9]==board[3]==board[6]:
        return board[9]
    elif board[9]==board[8]==board[7]:
        return board[9]

  return 0


def TicTacToe():
  """
  Starts a game of Tic-Tac-Toe between two players on one computer.  This game involves the placeing of markers
  in a 3 by 3 grid.  The first player to get three of their markers (an X or an O) in a row wins the game.
  In the event that every square is taken without any wins, the game is a tie.
  """
  os.system('clear')
  playerTurn = 0
  players = PlayerAssignment()
  board = ['-',' ',' ',' ',' ',' ',' ',' ',' ',' ']
  winFlag = 0
  DisplayBoard(board)
  while winFlag == 0:
    board[PlayerMove(board, players[playerTurn])] = players[playerTurn]
    DisplayBoard(board)
    winFlag = CheckWin(board)
    if not winFlag == 0:
      print('Player '+ winFlag +' has won the game!')
      print('CONGRATULATIONS!')
    if playerTurn == 0:
      playerTurn = 1
    else:
      playerTurn = 0
    if board.count(' ') == 0:
      print('The board is full without any winners, thus it is a tie!\nBetter luck next time!')
      break

TicTacToe()