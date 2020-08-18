import random
import json
import sys
from math import floor
import players.ship as Ship


class Player:
    def __init__(self):
        print("Init game!")

    def getMove(self):
        return (random.randint(0, 11), random.randint(0, 11))

    def getRandomTopLeft(self, max_x, max_y):
        return {"x": floor(random.uniform(0, 1) * max_x), "y": floor(random.uniform(0, 1) * max_y)}

    def getRandomOrientation(self):
        return random.choice(list(Ship.Orientation.keys()))

    def placeShips(self, islands):
        taken_cells = []
        for island in json.loads(islands)["islands"]:
            print("ISLAND: {}".format(island))
            taken_cells.append({"x": island["x"], "y": island["y"]})

        ship_placement = {}

        for ship in Ship.ShipType.keys():
            # work out boundries for top-left within the board
            orientation = self.getRandomOrientation()
            top_left = {"x": 0, "y": 0}
            ship_cells = Ship.get_cells(ship, top_left, orientation)
            max_x = 12 - max(item['x'] for item in ship_cells)
            max_y = 12 - max(item['y'] for item in ship_cells)
            while (not Ship.is_ship_valid(taken_cells, ship_cells)):
                top_left = self.getRandomTopLeft(max_x, max_y)
                ship_cells = Ship.get_cells(Ship.ShipType[ship], top_left, orientation)
            placement = {"orientation": orientation, "topleft": "{},{}".format(top_left["x"], top_left["y"])}
            ship_placement[ship] = placement
            taken_cells.extend(ship_cells)
        
        return {
            "SHIPS": ship_placement
        }
    
    def onOpponentMove(self, opponentMove): 
        print("opponent did - {}".format(opponentMove))

    def onShotResult(self, opponentMove):
        print("Shot result - {}".format(opponentMove))

    def writeToServer(self, output):
        if (output):
            print('send:{}'.format(output))
            sys.stdout.flush()
