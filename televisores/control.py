class Control:

    def __init__(self):
        self.tv = None
    
    def getTv(self):
        return self.tv
    def setTv(self, tv):
        self.tv = tv
    def enlazar(self, tv):
        self.tv = tv
        self.tv.setControl(self)
    def setCanal(self,i):
        self.tv.setCanal(i)
    def turnOn(self):
        self.tv.turnOn()
    def turnOff(self):
        self.tv.turnOff()
    def canalUp(self):
        self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()
    def volumenUp(self):
        self.tv.volumenUp()
    def volumenDown(self):
        self.tv.volumenUp()