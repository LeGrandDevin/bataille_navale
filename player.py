import case
import bateau


class Player:

    def __init__(self, size_board):
        self.team = []
        self.desk = []
        for i in range(size_board):
            self.desk.append([])
            for j in range(size_board):
                self.desk[i].append(case.Case())

    def placeBoat(self, size, x, y, horizontal):
        currentBoat = bateau.Boat(size)
        if(horizontal):
            for i in range(size):
                self.desk[x][y].boat = currentBoat
                self.desk[x][y].isBoat = True
                x += 1
        else:
            for i in range(size):
                self.desk[x][y].boat = currentBoat
                self.desk[x][y].isBoat = True
                y += 1
        self.team.append(currentBoat)

    def showBoard(self):
        for ligne in self.desk:
            print('')
            for case in ligne:
                if(case.shoted):
                    print('X', end='')
                elif(case.isBoat):
                    print('#', end='')
                else:
                    print('~', end='')
        for boat in self.team:
            if boat.isAlive():
                print('\nEN VIE')

    def shotBoard(self, x, y):
        case = self.desk[x][y]
        if case.isBoat:
            case.boat.damage()
            if not case.boat.isAlive():
                case.boat.destroy()
        case.shot()

    def checkwin(self):
        for boat in self.team:
            if boat.isAlive():
                return True
        return False

