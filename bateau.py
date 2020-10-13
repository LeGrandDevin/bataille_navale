class Boat:
    alive = True

    def __init__(self, pv):
        self.pv = pv

    def damage(self):
        self.pv -= 1

    def destroy(self):
        self.alive = False


# afficher le plateau (2 grilles ou 1), pouvoir placer les bateaux et qu'ils s'affichent sur le plateau.
# pouvoir tirer sur des bateaux (round/case jsais pas), et voir si un bateau est touché si il perd un PV.
# check si il y a victoire d'un joueur à chaque touché.
# faire contre un bot qui fait les choses rdm et après on verra pour faire un duel de vrai joueur / un bot plus dur
# plateau 10 par 10 (faire une grille 10 par 10 en comptant le 0, mettre à chaque début de ligne/colonne le nom
# de ces dernières (1,2,3...10 - A,B,C...J ou 1,2,3...10) comme ça ça s'ajustera et en plus on aura les coordonnées à
# vue d'oeil
