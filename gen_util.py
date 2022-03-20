import random

# Generate inputted number of player names in random order
def getRandomOrderedNames(size):
    players = ["Player-"+str(i) for i in range(1, size+1)]
    random.shuffle(players)
    # print(players)
    return players

# Handles the case of two consecutive '1'
def handleConsecutiveOnes(cur_player):
    cur_player.prev_rolls.pop(0)
    cur_player.prev_rolls.append(0)
    cur_player.skip_flag = False