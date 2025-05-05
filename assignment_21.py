# 21. Make a Custom Class Iterable

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start  
        if start < 0:
            raise ValueError("Start value must be non-negative")

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value
        elif self.current == 0:
            value = self.current
            self.current -=1
            return value
        else:
            raise StopIteration  

countdown = Countdown(5)  

for number in countdown:
    print(number) 