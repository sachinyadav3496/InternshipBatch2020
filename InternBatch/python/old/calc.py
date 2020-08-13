import os
os.system('cls') # to clear your output screen
print('\n\n\n\n')
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    return "Zero Division Error"

def main(x, y, ch):
    if ch == '+':
        print(add(x, y))
    elif ch == '-':
        print(sub(x, y))
    elif ch == '*':
        print(mul(x, y))
    elif ch == '/':
        print(div(x,y))
    else:
        print("Invalid Operation")
if __name__ == '__main__':
    x = int(input("X: "))
    y = int(input("Y: "))
    ch = input("Choice (+,-,*,/): ")
    main(x, y, ch)
