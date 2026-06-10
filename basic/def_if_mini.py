def get_status(num, name):
    if num > 0:
        return f"{name} is positive"
    elif num < 0:
        return f"{name} is negative"
    else:
        return f"{name} is zero"

def sign(a, b, c):
    status_a = get_status(a, "A")
    status_b = get_status(b, "B")
    status_c = get_status(c, "C")
    print(f"{status_a}, {status_b}, and {status_c}")

# Input section
a = int(input("Enter a number A : "))
b = int(input("Enter a number B : "))
c = int(input("Enter a number C : "))
sign(a, b ,c)