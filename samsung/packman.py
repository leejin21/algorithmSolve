'''


'''

import sys; read = sys.stdin.readline

dirList = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']
drList = [-1, -1, 0, 1, 1, 1, 0, -1]
dcList = [0, -1, -1, -1, 0, 1, 1, 1]

GRID_LENGTH = 4
packMan = None
monsterList = []
mosterEggList = []
grid = [[None]*GRID_LENGTH for _ in range(GRID_LENGTH)]

class PackMan:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def __str__(self):
        return "r: " + str(self.r) + ", c: " + str(self.c)

class Monster:
    def __init__(self, i, r, c, d):
        self.i = i
        self.r = r
        self.c = c
        self.d = d

    def __str__(self):
        # pos = ", r: " + str(self.r) + ", c: " + str(self.c)
        return "i: " + str(self.i) + ", d: " + dirList[self.d]

    @staticmethod
    def copy(monster):
        return Monster(monster.i, monster.r, monster.c, monster.c)


class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.existMonsterList = []

    def addMonster(self, monster):
        self.existMonsterList.append(monster)
    
    def deleteMonster(self, monster):
        self.existMonsterList.remove(monster)

    def __str__(self):
        return str(len(self.existMonsterList))

########## UTILS ############
def printGrid():
    print("==PRINT GRID==")
    for r in range(GRID_LENGTH):
        for c in range(GRID_LENGTH):
            print(grid[r][c], end = " ")
        print()

def printMonsters():
    print("==PRINT MONSTERS==")
    for r in range(GRID_LENGTH):
        for c in range(GRID_LENGTH):
            cell = grid[r][c]
            if cell.existMonsterList:
                print("r, c: ", r, c)
            for monster in cell.existMonsterList:
                print(monster)


########## LOGIC FUNCTIONS ############

def init():
    global packMan
    packMan = PackMan(R-1, C-1)

    for r in range(GRID_LENGTH):
        for c in range(GRID_LENGTH):
            grid[r][c] = Cell(r, c)

    for m in range(M):
        r, c, d = [int(i) for i in read().split()]
        monster = Monster(m, r-1, c-1, d-1)
        monsterList.append(monster)
        grid[r-1][c-1].addMonster(monster)

def turn():
    startCopyMonsters()
    moveMonsters()
    movePackMan()
    removeDeadMonsters()
    endCopyMonsters()

def startCopyMonsters():
    for monster in monsterList:
        egg = monster.copy()
        monsterEggList.append(egg)


def moveMonsters():
    pass

def movePackMan():
    pass

def removeDeadMonsters():
    pass

def endCopyMonsters():
    global monsterEggList


    # clear monster egg list
    monsterEggList = []
    

def main():
    init()
    printGrid()
    printMonsters()

M, T = [int(i) for i in read().split()]
R, C = [int(i) for i in read().split()]

main()