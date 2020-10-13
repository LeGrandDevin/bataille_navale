import player
class Partie:
    def __init__(self,size_desk):
        self.player1 = player.Player(size_desk)
        self.player2 = player.Player(size_desk)
    