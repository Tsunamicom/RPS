# Written in Python 3.4 by Kurtis Mackey
import random

Hand = {'Rock': {'Rock': 1, 'Paper': 0, 'Scissors': 2},
        'Paper': {'Rock': 2, 'Paper': 1, 'Scissors': 0},
        'Scissors': {'Rock': 0, 'Paper': 2, 'Scissors': 1}}

aibeat = {'Rock': 1, 'Paper': 2, 'Scissors':0}
throw_values = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
aiselection = [0, 1, 2]


# ==============================================================================
# ====================================CLASSES===================================

class Player:

  def __init__(self, name):
    self.name = name
    self.win = 0
    self.lose = 0
    self.draw = 0
    self.rock = 0
    self.paper = 0
    self.scissors = 0
    self.prediction = [0, 1, 2]  # Currently not used

  def win_percent(self):  # Possible div/0
    return self.win/(self.win + self.lose + self.draw)

  def lose_percent(self):  # Possible div/0
    return self.lose/(self.win + self.lose + self.draw)

  def throw_rock(self):
    self.rock += 1
    return 'Rock'

  def throw_paper(self):
    self.paper += 1
    return 'Paper'

  def throw_scissors(self):
    self.scissors += 1
    return 'Scissors'


player1 = Player('Player 1')
player2 = Player('Player 2')
currentplayer = player1



# ==============================================================================
# ================================FUNCTIONS=====================================


def player_choice(player=currentplayer):
  print('==WIN(%s)== %s ==LOSE(%s)==' % (player.win, player.name, player.lose))
  print('=========DRAW(%s)==========' % player.draw)
  print('Select one of the following options:')
  print(r'0 - Rock || 1 - Paper || 2 - Scissors')
  playerselect = int(input('==>> '))
  print('')

  if playerselect == 0:
    return player.throw_rock()
  elif playerselect == 1:
    return player.throw_paper()
  elif playerselect == 2:
    return player.throw_scissors()
  else:
    print('Invalid Entry!  Must be 0, 1, or 2.')
    return player_choice()




def rps(p1, p2, player=currentplayer):

  aiselection.append(aibeat[p1])  # Currently over ALL players

  print('%s throws %s' % (player.name, p1))
  print('Computer throws %s' % (p2))

  if Hand[p1][p2] == 1:
    player.draw += 1
    print('Draw')
  elif Hand[p1][p2] == 0:
    player.lose += 1
    print('P2 Wins!')
  else:
    player.win += 1
    print('P1 Wins!')
  print('')


def player_select():
  pass  # Not implemented yet





# ==============================================================================
# ===================================MAIN=======================================


currentplayer.name = 'Tsunami'
gamenum = int(input('How many games?: '))
print('')
for i in range(gamenum):
    print('Game %s' % (i+1))
    ai_choice = throw_values[random.choice(aiselection)]
    rps(player_choice(), ai_choice)

print('===== END STATS =====')
print('Wins: %s out of %s' % (currentplayer.win, gamenum))
print('Win Percent: %.2f' % (currentplayer.win/gamenum*100))
print('Draws: %s' % currentplayer.draw)
print('Rock Thrown: %s' % currentplayer.rock)
print('Paper Thrown: %s' % currentplayer.paper)
print('Scissors Thrown: %s' % currentplayer.scissors)
