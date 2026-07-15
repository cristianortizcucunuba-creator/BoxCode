def validar_password(password):
    mayus= 0
    num = 0

    if len(password) < 8:
        return False
    for caracter in password:
        if caracter.isupper():
            mayus += 1
        elif caracter.isdigit():
            num += 1
    if mayus < 1:
        return False
    elif num < 1:
        return False
    return True

userPassword = input("Enter your password for validation: ")
while validar_password(userPassword) == False:
    print("your password is very easy")
    userPassword= input ("intenta con otra contraseña: ")
print("your password is sure :D")