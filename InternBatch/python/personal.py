"""
    personal is a module having these functions
    
    hello
    add
    pat
"""

def hello(name):
    """hello(name) -> greet using name"""
    print("Hello ", name)
    
def add(x, y):
    """add(x, y) -> return x + y"""
    return x + y

def pat(nrows):
    """
        pat(nrows) prints normal pattern
    """
    print(*['*'*r for r in range(1, nrows+1)], sep='\n')
    
if __name__ == '__main__':
    hello('sachin yadav')
    print(add(5, 10))
    pat(10)
