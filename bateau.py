class Boat:
    alive = True

    def __init__(self,size):
        self.pv = size

    def damage(self):
        self.pv -= 1

    def destroy(self):
        self.alive = False
