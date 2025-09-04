email = input()
if email.count('@')==1:
    local,domain = email.split('@')

    if local and domain:
       
        if '.' in domain and not domain.startswith('.') and not domain.endswith('.'):
            print("Valid email")
        else:
            print("Invalid email")
    else:
        print("Invalid email")
else:
    print("Invalid email")
