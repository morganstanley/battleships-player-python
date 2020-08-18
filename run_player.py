#!/usr/bin/env python3

import sys
import json
from players.random import Player


def process_input(player, input_line):
        parts = input_line.split(" ")
        action = parts[0]

        if action == "init":
            player.__init__()
        elif action == "place-ships":
            ships = player.placeShips(parts[1])
            player.writeToServer("placed-ships {}".format(json.dumps(ships, sort_keys=True, separators=(",", ":"))))
        elif action == "move":
            try:
                coords = player.getMove()
                player.writeToServer("shoot {},{}".format(coords[0], coords[1]))
            except Exception as e:
                print('Player Error: Failed to get a move'.format(e))
        elif action == "opponent":
            opponent_move = parts[1].split(',')
            player.onOpponentMove([opponent_move[0], opponent_move[1], opponent_move[2]])
            try:
                coords = player.getMove()
                player.writeToServer("shoot {},{}".format(coords[0], coords[1]))
            except Exception as e:
                print('Player Error: Failed to get a move'.format(e))
        elif action == "result":
            shot_result = parts[1].split(',')
            player.onShotResult([shot_result[0], shot_result[1], shot_result[2]])


if __name__ == "__main__":
    player = Player()
    line = sys.stdin.readline()
    while line:
        process_input(player, line.strip())
        line = sys.stdin.readline()
