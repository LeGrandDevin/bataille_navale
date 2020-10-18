import Partie

game = Partie.Partie(10)
game.player1.placeBoat(3, 2, 2, False)
game.player1.placeBoat(4, 4, 4, True)

while True:
    game.player1.showBoard()
    x = input('\nx:')
    y = input('\ny:')
    game.player1.shotBoard(int(x), int(y))