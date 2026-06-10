def get_status(num, name):
    if num > 0:
        return f"{name} is positive"
    elif num < 0:
        return f"{name} is negative"
    else:
        return f"{name} is zero"

def sign(numbers, names):
    statuses = []
    # Loop through the numbers and names simultaneously
    for num, name in zip(numbers, names):
        statuses.append(get_status(num, name))
    
    # Format the output dynamically: "X, Y, Z, W, and V"
    all_but_last = ", ".join(statuses[:-1])
    last = statuses[-1]
    print(f"{all_but_last}, and {last}")

# Input section
numbers = []
names = ["A", "B", "C", "D", "E"]

for name in names:
    val = int(input(f"Enter a number {name} : "))
    numbers.append(val)

# Call the function with the lists
sign(numbers, names)