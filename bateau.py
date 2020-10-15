class Boat:

    def __init__(self, pv):
        self.alive = True
        self.pv = pv

    def damage(self):
        self.pv -= 1

    def destroy(self):
        self.alive = False

    def isAlive(self):
        if self.pv == 0:
            return False
        return True

