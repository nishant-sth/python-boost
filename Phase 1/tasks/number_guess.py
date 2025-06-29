import random
exact_number = random.randint(1, 100)

guess_count = 0
while True:
    guess_number = int(input("Guess the number between 1 to 100 "))
    guess_count+=1

    if guess_number > exact_number:
        print('Too High! Try again')
    elif guess_number < exact_number:
        print('Too Low! Try again')
    else:
        print(f'Congratulation! Your guess {guess_number} is correct. ')
        print(f"It took you {guess_count} guesses.")
