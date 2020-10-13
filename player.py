import case
import bateau
class Player:
    team = []
    desk =[]

    def __init__(self,size_board):
        for i in range(size_board):
            self.desk.append([])
            for j in range(size_board):
                self.desk[i].append(case.case())
    
    def placeBoat(self,size,x,y,horizontal):
        currentBoat = bateau.Boat(size)
        if(horizontal):
            for i in range(size):
                x += 1
                self.desk[x][y].boat = currentBoat
                self.desk[x][y].isBoat = True
        else:
            for i in range(size):
                y += 1
                self.desk[x][y].boat = currentBoat
                self.desk[x][y].isBoat = True

    def showBoard(self):
        for ligne in self.desk:
            print('')
            for case in ligne:
                if(case.isBoat):
                    print('#',end='')
                else:
                    print('~',end='')
