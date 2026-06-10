a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))
c = int(input("Enter a number C: "))
d = int(input("Enter a number D: "))

if a >= b and a >= c and a >= d:
    print("The largest number is ", a)    
elif b >= a and b >= c and b >= d:
    print("The largest number is ", b)    
elif c >= a and c >= b and c >= d:
    print("The largest number is ", c)
elif d >= a and d >= b and d >= c:
    print("The largest number is ", d)
else:   
    print("Error: Invalid input")