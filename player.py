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
        for i in range(size):
            self.desk[x][y].boat = currentBoat

