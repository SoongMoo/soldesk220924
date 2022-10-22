PI = 3.141592

def sum1(num1, num2):
    result = num1 + num2
    return result

class FourCal1:
    def __init__(self, num1, num2): 
        self.first = num1
        self.second = num2
    def add(self):
        self.result = self.first + self.second
    def div(self):
        self.result = self.first / self.second

class MoreFourCal1(FourCal1): # add(), div()
    def mul(self):
        self.result = self.first * self.second
    def sub(self):
        self.result = self.first - self.second

    def div(self): 
        if self.second == 0:
            self.result = 0
        else :
            self.result = self.first / self.second