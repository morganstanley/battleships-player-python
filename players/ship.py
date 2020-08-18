ShipType = {
    "SUB": "SUB",
    "SPEEDBOAT": "SPEEDBOAT",
    "BATTLESHIP": "BATTLESHIP",
    "AIRCRAFT_CARRIER": "AIRCRAFT_CARRIER",
    "OIL_RIG": "OIL_RIG",
}

Orientation = {
    "LEFT": "LEFT",
    "DOWN": "DOWN",
    "RIGHT": "RIGHT",
    "UP": "UP",
}


def get_cells(ship, top_left, orientation):
    cells = []

    X = True
    _ = False
    layout = None

    if ship == "AIRCRAFT_CARRIER":
        if orientation == "LEFT":
            layout = [
                [X, X, X, X],
                [_, X, X, _]
            ]
        elif orientation == "UP":
            layout = [
                [_, X],
                [X, X],
                [X, X],
                [_, X]
            ]
        elif orientation == "RIGHT":
            layout = [
                [_, X, X, _],
                [X, X, X, X]
            ]
        elif orientation == "DOWN":
            layout = [
                [X, _],
                [X, X],
                [X, X],
                [X, _]
            ]
    elif ship == "BATTLESHIP":
        if orientation == "LEFT" or orientation == "RIGHT":
            layout = [
                [X, X, X, X]
            ]
        elif orientation == "UP" or orientation == "DOWN":
            layout = [
                [X],
                [X],
                [X],
                [X]
            ]
    elif ship == "OIL_RIG":
        if orientation == "LEFT" or orientation == "RIGHT":
            layout = [
                [X, _, _, X],
                [X, X, X, X],
                [X, _, _, X]
            ]
        elif orientation == "UP" or orientation == "DOWN":
            layout = [
                [X, X, X],
                [_, X, _],
                [_, X, _],
                [X, X, X]
            ]
    elif ship == "SPEEDBOAT":
        if orientation == "LEFT":
            layout = [
                [X, _],
                [X, X]
            ]
        elif orientation == "UP":
            layout = [
                [X, X],
                [X, _]
            ]
        elif orientation == "RIGHT":
            layout = [
                [X, X],
                [_, X]
            ]
        elif orientation == "DOWN":
            layout = [
                [_, X],
                [X, X]
            ]
    elif ship == "SUB":
        if orientation == "LEFT" or orientation == "RIGHT":
            layout = [
                [X, X]
            ]
        elif orientation == "UP" or orientation == "DOWN":
            layout = [
                [X],
                [X]
            ]

    if layout is not None:
        cells = []
        for y_ind, row in enumerate(layout):
            for x_ind, contains_ship in enumerate(row):
                if contains_ship:
                    cells.append({"x": top_left["x"] + x_ind, "y": top_left["y"] + y_ind})
    return cells


# Checks the ships are valid by
# 1) Ensuring there's no overlap with the "banned" cells (Other ships & islands)
# 2) Each cell of the ship placement is within the bounds of the grid

# This validation is also done on the server side, but 3 failed placements results
# in losing the game so good to check prior.
def is_ship_valid(takenCells, shipCells):
    all_cells_raw = list(set((item["x"], item["y"]) for item in takenCells))
    all_cells_raw.extend((item["x"], item["y"]) for item in shipCells)
    all_cells_unique = set(all_cells_raw)

    return len(all_cells_raw) == len(all_cells_unique) and all((0 <= item[0] and item[0] < 12) and (0 <= item[1] and item[1] < 12) for item in all_cells_raw)
