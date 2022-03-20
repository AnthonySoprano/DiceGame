# built-in imports
import sys
import random

# custom imports
from game_util import *
from gen_util import *
from constants import *

# Command Line Arguments passed
PLAYER_COUNT = int(sys.argv[1])
POINTS_FOR_WIN = int(sys.argv[2])


# Create Circular LinkedList with players in random order of Round Robin
player_names = getRandomOrderedNames(PLAYER_COUNT)
player_order = PlayerOrder()
for player_name in player_names:
    player_order.addPlayer(player_name)

# the player whose turn it is
cur_player = player_order.head
# table to store players who have completed the game
points_table = []

# game ends when list if empty
while player_order.head is not None:

    # check and handle consecutive ones using skip_flag
    if cur_player.skip_flag:
        handleConsecutiveOnes(cur_player)
        cur_player = player_order.getNextPlayer(cur_player)
        continue
    
    print()
    print(cur_player.name, ROLL_PROMPT)
    roll_command = input()
    if roll_command=='r':
        rolled_point = random.randint(1, 6)
        print(cur_player.name, ROLLED_MSG, rolled_point)

        # store two previous rolls for each player to handle consecutive ones
        cur_player.points = min(POINTS_FOR_WIN, cur_player.points+rolled_point)
        cur_player.prev_rolls.pop(0)
        cur_player.prev_rolls.append(rolled_point)
        if cur_player.prev_rolls == [1,1]:
            print(cur_player.name, ONES_MSG)
            cur_player.skip_flag = True

        # Output rank and score for each player after each round
        rank  = 0
        print(RANK_COL, PLAYER_COL, SCORE_COL)
        for rank in range(1, len(points_table)+1):
            print(rank, points_table[rank-1][0], points_table[rank-1][1])  # prints players that completed the game
        player_order.printOrder(rank+1)                                    # prints player that are active in the game

        # check and handle comapleted player
        if cur_player.points == POINTS_FOR_WIN:
            print(cur_player.name, COMPLETED_MSG, len(points_table)+1)
            points_table.append([cur_player.name, cur_player.points])
            player_order.removePlayer(cur_player.name)
        
        # check and handle case wehn 6 is rolled
        if rolled_point == 6 and cur_player.points < POINTS_FOR_WIN:
            print(cur_player.name, SIX_MSG)
        else:
            cur_player = player_order.getNextPlayer(cur_player)
    else:
        print(INVALID_INPUT_MSG)

print()
print(GAME_END_MSG)
for rank in range(1, len(points_table)+1):                
    print(rank, points_table[rank-1][0])                # prints Final Ranks of all players 

