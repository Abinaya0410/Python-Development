def check_pass(password):
    strength=0


    if len(password)>= 8:
        strength+= 1

    if any(c.isupper() for c in password):
        strength+= 1

    if any(c.islower() for c in password):
        strength+= 1

    if any(c.isdigit() for c in password):
        strength+= 1

    if any(c in "!@#$%^&*()-_=+[]{};:',.<>?/|" for c in password):
        strength+= 1

    if strength== 5:
        return "Strong password"
    elif strength >=3:
        return "Medium password"
    else:
        return "Weak password"

p = input("Enter your password:")
print(check_pass(p))
