def say_hello():
    print('HELLO')
    return('HELLO')

def multiply(*args):
    
    mul=1
    
    for arg in args:
        mul = mul*arg
    print('This is the result: ',mul)
    return(mul)
    