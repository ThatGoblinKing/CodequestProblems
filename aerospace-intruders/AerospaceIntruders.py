#https://lmcodequestacademy.com/problem/aerospace-intruders
from contextlib import redirect_stdout
from io import StringIO

EXPECTED_OUTPUT = """Destroyed Ship: TEST xLoc: 12
Destroyed Ship: BOGEE xLoc: 22
Destroyed Ship: DOOM xLoc: 103
Destroyed Ship: SHIP7 xLoc: 140
Destroyed Ship: SHIP3 xLoc: 135
Destroyed Ship: SHIP5 xLoc: 115
Destroyed Ship: SHIP12 xLoc: 95
Destroyed Ship: SHIP6 xLoc: 75
Destroyed Ship: SHIP11 xLoc: 60
Destroyed Ship: SHIP9 xLoc: 35
Destroyed Ship: SHIP13 xLoc: 15
Destroyed Ship: SHIP8 xLoc: 15
Destroyed Ship: SHIP2 xLoc: 20
Destroyed Ship: SHIP10 xLoc: 45
Destroyed Ship: SHIP1 xLoc: 40
Destroyed Ship: SHIP4 xLoc: 85"""


class Ship:
    def __init__(self, name, classification, x, y):
        self.name = name
        self.classification = ord(classification[0]) - ord("A")
        self.x = x
        self.y = y

    def __str__(self):
         return f"{self.name} xLoc: {self.x}"

    def move(self):
        if self.classification == 0:
            self.x -= 10
        elif self.classification == 1:
            self.x -= 20
        else:
            self.x -= 30


def convertStringToShip(string) -> Ship:
    ship_name, temp = string.split("_")
    classification, temp = temp.split(":")
    x, y = temp.split(",")
    return Ship(ship_name, classification, int(x), int(y))

def main():
    cases = int(input())
    for _ in range(cases):
        line = input()
        ships = int(line)
        shipList = []
        for i in range(ships):
            shipList.append(convertStringToShip(input()))
        sorted_ships = sorted(shipList, key=lambda ship: (ship.x, -ship.y))
        while len(sorted_ships) > 0:
            print(f"Destroyed Ship: {sorted_ships[0]}")
            sorted_ships.pop(0)
            for ship in sorted_ships:
                ship.move()
            sorted_ships.sort(key=lambda ship: (ship.x, -ship.y))

f = StringIO()
with redirect_stdout(f):
    main()
s = f.getvalue().strip()
print(s)