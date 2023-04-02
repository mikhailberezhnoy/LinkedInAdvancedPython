class mbclass():
    def __init__(self, Length, Width, Height):
        self.L =Length
        self.W =Width
        self.H =Height

    def __repr__(self):
        return f'L={self.L}, W={self.W}, H={self.H}'
    def  __getattr__(self, attr):
        if attr=='Volume':
            return (self.L*self.W*self.H)
        else:
            self.attr

    def  __setattr__(self, attr, value):
        if attr=='sizes':
            self.L = value['L']
            self.W = value['W']
            self.H = value['H']
        else:
            super().__setattr__(attr, value)

Mbins1 = mbclass(10,20,30)
Mbins2 = mbclass(120,0,40)

print (Mbins1)
print (Mbins2)

# Test __getattr__
print(Mbins1.Volume)
print(Mbins1.L)

# Test __setattr__

Mbins1.sizes = {"L":15,"H":14, "W":11}
print (Mbins1)


print (dir(Mbins1))