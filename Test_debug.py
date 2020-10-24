import Partie

game = Partie.Partie(10)
game.player1.placeBoat(3, 2, 2, False)
game.player1.placeBoat(4, 4, 4, True)
game.player1.placeBoat(5, 1, 1, False)
#game.player1.placeBoat(2, 7, 7, True)
#game.player1.placeBoat(3, 9, 2, False)

game.player2.placeBoat(3, 1, 1, False)
game.player2.placeBoat(4, 3, 3, True)
game.player2.placeBoat(5, 0, 0, False)
#game.player2.placeBoat(2, 7, 7, True)
#game.player2.placeBoat(3, 8, 1, False)

p = 2
g = True

while g:
    x = int(input('\nx:'))
    y = int(input('\ny:'))
    p = 1 if p == 2 else 2
    g = game.round(p,x,y)