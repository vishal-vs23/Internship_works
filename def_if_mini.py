def get_status(num, name):
    if num > 0:
        return f"{name} is positive"
    elif num < 0:
        return f"{name} is negative"
    else:
        return f"{name} is zero"

def sign(a, b):
    status_a = get_status(a, "A")
    status_b = get_status(b, "B")
    
    if (a > 0 and b > 0) or (a < 0 and b < 0) or (a == 0 and b == 0):
        # Simplifies "A is positive and B is positive" to "A and B is positive"
        state = "positive" if a > 0 else ("negative" if a < 0 else "zero")
        print(f"A and B is {state}")
    else:
        print(f"{status_a} and {status_b}")

# Input section
a = int(input("Enter a number A : "))
b = int(input("Enter a number B : "))
sign(a, b)