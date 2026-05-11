def prime(a):
    if a<=1:
        return False
    for b in range(2,a):
        if a%b==0:
            return False
    return True
print(prime(7))