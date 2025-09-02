def toFahrenheit(c):
    return (c*9/5)+32

def toCelsius(f):
    return (f-32)*5/9

temp = float(input())
unit = input().strip().upper()

if unit=="C":
    print(round(toFahrenheit(temp),2))
elif unit=="F":
    print(round(toCelsius(temp),2))
else:
    print("Invalid")
