import re

def solve_operation(operation):
    values = re.split('(\d+)', operation)
    if (len(values) == 5):
        val1 = float(values[1])
        val2 = float(values[3])
        op = values[2]
    else:
        print(IndexError)
        return ("Program can only solve operations between two (2) numbers")
        
    
    if (op == "+"):
        return val1 + val2
    elif (op == "-"):
        return val1 - val2
    elif (op == "*"):
        return val1 * val2
    elif (op == "/"):
        return val1 / val2
    else:
        print(TypeError)
        print("Operation is not available in this program")


print("""Welcome to a simple calculator program. 
This program recieves a simple arithmetic operations involving ONLY 2 numbers and returns the result.
The arithmetic operations supported include '+', '-', '*', '/' """)

operation = input("Enter your operation: ")

print(solve_operation(operation))


