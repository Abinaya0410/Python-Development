import random

low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))

number = random.randint(low, high)

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print("Correct.")
        break
