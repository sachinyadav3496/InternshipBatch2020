prime = lambda num, check=2 : print("Prime") if check >= num**(1/2) else print("Not Prime")\
 if num % check == 0 else prime(num, check+1)
prime(int(input("number: ")))
