

#Demo Pin Class
class Pin:
    _out = 3
    @property
    def OUT(self):
        return self._out
    _in = 3
    @property
    def IN(self):
        return self._in

    def __init__(self, pinNum, pinType):
        self.pinNum = pinNum
        self.pinType = pinType
        self._value = False

    def value(self, inVal=-1):
        if inVal == -1 :
            return self._value
        else:
            if inVal == 0 or inVal == 1:
                self._value = inVal
        

    
        
