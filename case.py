import bateau


class Case:
    def __init__(self):
        self.boat = bateau.Boat(50)
        self.shoted = False
        self.boat = False
        self.isBoat = False

    def shot(self):
        self.shoted = True
    
    def bindBoat(self, boat):
        self.boat = boat
