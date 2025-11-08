class One(object):
    a = 0
    
    def __init__(self):
        self.a = 7
#        print(f'One init self: {self}')
#        print(f'One init self id: {id(self)}')
    
    def __new__(self):
#        print(f'One new self: {self}')
#        print(f'One new self id: {id(self)}')
        self = super().__new__(self)
        return self
    
#    print('one made')

class Two(list):
    l = 0

a = Two()
print(a)
print(type(a))
print(id(a))


b = One()
print(b)
print(type(b))
print(id(b))



"""print('here')
a = One()
print( id(a) )
print(type(a))

print( id(One) )
print(f'{One.a} {a.a}')
a.a = 11
print(f'{One.a} {a.a}')
One.a = 21
print(f'{One.a} {a.a}')"""
