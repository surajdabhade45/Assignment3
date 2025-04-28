
a = input("Enter a number: ")
a = int(a)

def factorial(a):

    if a < 2:
        return 1
    else:
        return a*(factorial(a - 1))

result = factorial(a)

print(result)
