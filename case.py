class case():

    shoted = False
    def __init__(self):
        self.shoted = False
        self.isBoat = False
    def shot(self):
        self.shoted=True
    
    def bindBoat(self,boat):
        self.boat = boat
