def password_checker(password):
    upper=0
    lower=0
    number=0
    special=0
    special_chars="@#$%&*!"
    if len(password)<8:
        return "password must be 8 characters"
    for i in password:
        if i>="A" and i<="Z":
            upper=upper+1
        elif i>="a" and i<="z":
            lower=lower+1
        elif i>="0" and i<="9":
            number=number+1
        elif i in special_chars:
            special=special+1
    if upper>=1 and lower>=1 and number>=1 and special>=1:
        return "strong password"
    else:
        return "weak password"
password=input("enter password : ")
result=password_checker(password)
print(result)