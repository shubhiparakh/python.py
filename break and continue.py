'''n=18
no_of_guesses = 1
print("number of guesses is limited to 9 times only")
while(no_of_guesses<=9):
    guess_number= int(input("guess a number"))
    if guess_number<18:
        print("enter a number greater")
    elif guess_number>18:
        print("enter a lesser number")
    else:
        print("you guessed the number, you won")
        print(no_of_guesses, "no of guesses you took to finish")
        break
    print(9-no_of_guesses, "no of guesses left")
    no_of_guesses = no_of_guesses + 1
    if (no_of_guesses>9):
        print("game over")


n=18
no_of_guesses = 1
print("you can guess 9 times")
while(no_of_guesses<9):
    num=int(input("enter your guess"))
    if num>n:
        print("enter a lower number")
    elif num<n:
        print("enter a greater number")
    else:
        print("you won the game")
        print(no_of_guesses, "no of guesses you took to win")
    print("no of guesses left", 9-no_of_guesses)
    no_of_guesses +=1
    if no_of_guesses>9:
        print("game over")
'''

print("enter first number")
num1 = input(num1)
print("enter other number")
num2= input(num2)
















