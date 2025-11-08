class One:
    a = None
    print(a)
    def __init__(self):
        self.a = 7

    
    def __new__(self):
        print('__new__ method was called')
        self = super().__new__(self)
        return self
        

print('before ab exists')
ab = One()
bc = One

print(f'ab.a: {ab.a}')
print(f'bc.a: {bc.a}')
