class Case:
    boat = False
    shoted = False

    def __init__(self):
        self.boat = False

    def shot(self):
        self.shoted = True
    
    def bindBoat(self, boat):
        self.boat = boat
