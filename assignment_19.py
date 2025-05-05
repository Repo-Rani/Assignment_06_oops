# 19. callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return self.factor * x

multiplier = Multiplier(5)  

print(callable(multiplier)) 
result = multiplier(10)  
print(result)          