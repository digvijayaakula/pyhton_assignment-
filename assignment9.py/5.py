def multiplier(n):
    def multiply(x):
        return x * n
    return multiply
n = int(input("Enter multiplier: "))
x = int(input("Enter number: "))
fun = multiplier(n)
print(fun(x))