def factorial(n):
    if type(n)!=int or n<=0:
        raise ValueError('The number is not valid.')
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(8))