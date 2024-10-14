import sys
#exceptions method to manage operations

#validate input entries
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("")
    sys.exit(1)


#validate if divide by 0 exept the error
try:
    result = x / y 
except ZeroDivisionError:
    print("Error: cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")