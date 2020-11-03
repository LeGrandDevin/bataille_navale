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

    def checkOutGrid(self,size,x,y,orientation):
        if y-1 + size > 9 and not orientation :
            return False

        if x-1 + size > 9 and orientation :
            return False

        for j in range (size):
            if self.desk[x + (j if orientation else 0)][y].isBoat or self.desk[x][y+ (j if not orientation else 0)].isBoat:
                return False
            
        return True
            

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

    def removeBoat(self, size, x, y, orientation):
        self.desk[x][y].boat.destroy()
        if(orientation):
            for i in range(size):
                self.desk[x][y].boat = False
                self.desk[x][y].isBoat = False
                x += 1
        else:
            for i in range(size):
                self.desk[x][y].boat = False
                self.desk[x][y].isBoat = False
                y += 1
        temp = 0
        for j in range(len(self.team)):
            if not self.team[j - temp].alive :
                self.team.pop(j - temp)
                temp += 1
        
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
            if boat.alive:
                return True
        return False



