import numpy as np

print(type(np.linspace))
print(type(len))
print(type(2.5))

def myAdder(a,b,c):
    x=np.exp(a*np.sin(b))*np.log(c)
    return x

print(myAdder(1,2,3))
help(myAdder)