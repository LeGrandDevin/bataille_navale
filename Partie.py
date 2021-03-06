import player
import bateau


class Partie:
    started = False
    def __init__(self, size_desk):
        self.player1 = player.Player(size_desk)
        self.player2 = player.Player(size_desk)

    def round(self, player, x, y):
        if player == 1:
            self.player1.shotBoard(int(x), int(y))

            if self.player1.checkwin():
                return True
            else:
                return self.win(player)

        self.player2.shotBoard(int(x), int(y))

        if self.player2.checkwin():
            return True
        else:
            return self.win(player)

    def win(self, p):
        return False

    def getPlayer(self, player):
        if player == 1:
            return self.player1
        return self.player2

    def placeBoat(self,size,x,y,orientBool,player):
        if player == 1:
            self.player1.placeBoat(size,x,y,orientBool)
        else:
            self.player2.placeBoat(size,x,y,orientBool)
    
    def removeBoat(self,size,x,y,orientation,player):
        if player == 1:
            self.player1.removeBoat(size,x,y,orientation)
        else:
            self.player2.removeBoat(size,x,y,orientation)
