from random import randint

name = input("Hello! What is your name?")
print("Hello,", name + ". I hope you are well.")
print("I have guessed a random number. Try and guess it!")
number = randint(1, 100)
guess = 0
guesses = 0
while guess != number:
    guesses += 1
    guess = int(input("Enter guess: "))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    
    if guesses == 10 and guess != number:
        print("Sorry,", name + ", you didn't guess it. The number was", str(number) + ".")
        print("Goodbye", name + ", thank you for playing!")
        exit()

print("Well done! The number was", number, "and you guessed correctly within 10 turns!")
print("Goodbye", name + ", thank you for playing!")