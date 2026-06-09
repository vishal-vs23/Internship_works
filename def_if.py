a = int(input("Enter a number A : "))
b = int(input("Enter a number B : "))

def sign (a,b):
    if a > 0 and b > 0 :
        print("A and B is positive")
    elif a < 0 and b < 0 :
        print("A and B is negative")
    elif a > 0 and b < 0 :
        print("A is positive and B is negative")
    elif a < 0 and b > 0 :
        print("A is negative and B is positive")   
    else:
        print("A and B is zero")
        


# def compare(a, b):
#     if a > b:
#         print("a is greater than b")
#     elif a < b:
#         print("b is greater than a")
#     else:
#         print("a is equal to b")
    
# print(compare(a, b)) 
print(sign(a, b))