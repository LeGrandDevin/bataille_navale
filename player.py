from case import case
class Player:
    team = []
    desk =[]

    def __init__(self,size_desk):
        for i in range(size_desk):
            self.desk.append(case())