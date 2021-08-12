import datetime

#the file will contain the class share with name, ID, ORH, ORL , update ORH,ORL, signal 

#returns if market price is open


class stock:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.orh = 0
        self.orl = positive_infinity
        self.curr_order = "" # True when order is placed. To block multiple trade
    def update_or(self,lvp): 
        if lvp > self.orh:
            self.orh = lvp
        elif lvp < self.orl:
            self.orl = lvp
    def status_update(self,s):    # runs when transaction is made or ended 
        self.curr_order = s
        if s == 'BUY':
            return orh
        elif s== 'SELL':
            return orh              # returns SL in case transactions begins
        else:
            return 0                # indicates transaction completed
    def id(self):
        return self.id
    def status(self):
        return self.curr_order 
    def ORH(self):
        return self.orh
    def ORL(self):
        return self.orl
        