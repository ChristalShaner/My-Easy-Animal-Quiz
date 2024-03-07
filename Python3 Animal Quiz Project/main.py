def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer!")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry, wrong answer, try again: ")
            attempt = attempt + 1
    if attempt == 3:
        print("The correct answer is: ", answer)


score = 0
print("Guess the Animal! (Answer without articles or plurality)")
guess1 = input("What is the fastest dog species? ")
check_guess(guess1, "Greyhound")
guess2 = input("What is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("What is the only bird that can fly backwards? ")
check_guess(guess3, "Hummingbird")
guess4 = input("What is the only animal that has no stomach? ")
check_guess(guess4, "Platypus")
guess5 = input("What is the strongest creature on Earth? (For its size) ")
check_guess(guess5, "Ant")
guess6 = input(
    "What creature can survive for more than two years without food? ")
check_guess(guess6, "Tarantula")
guess7 = input("What animal enjoys rolling in mud to stay cool? ")
check_guess(guess7, "Pig")
guess8 = input("What is the only mammal capable of flying? ")
check_guess(guess8, "Bat")
guess9 = input("What is the loudest creature in the world? (For its size) ")
check_guess(guess9, "Shrimp")
guess10 = input("What is the deadliest animal in the world? ")
check_guess(guess10, "Mosquito")
print("Your Score is " + str(score))
