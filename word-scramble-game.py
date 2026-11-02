
import random

words = {
    "python": "A programming language",
    "computer": "An electronic machine",
    "keyboard": "Used for typing",
    "developer": "A person who creates software",
    "internet": "Used to connect computers worldwide"
}

high_score = 0

while True:

    score = 0

    print("\n=== WORD SCRAMBLE GAME ===")
    print("You have 3 rounds!")
    print("You get 3 attempts for each word.")

    for round_no in range(1, 4):

        word = random.choice(list(words.keys()))

        scrambled = list(word)
        random.shuffle(scrambled)

        scrambled_word = "".join(scrambled)

        print("\nRound", round_no)
        print("Scrambled word:", scrambled_word)

        choice = input("Do you want a hint? (yes/no): ").lower()

        if choice == "yes":
            print("Hint:", words[word])

        attempts = 3
        guessed = False

        while attempts > 0:

            guess = input("Enter your answer: ").strip().lower()

            if guess == word:
                print("Correct! You won!")
                score = score + 1
                guessed = True
                break

            else:
                attempts = attempts - 1

                if attempts > 0:
                    print("Wrong answer! Try again.")
                    print("Attempts left:", attempts)
                else:
                    print("No attempts left!")
                    print("Correct word was:", word)

        if not guessed:
            print("Better luck next round!")

    print("\n=== GAME OVER ===")
    print("Your final score:", score, "/ 3")

    if score > high_score:
        high_score = score
        print("Congratulations! New high score!")

    print("Your highest score:", high_score)

    if score == 3:
        print("Excellent! Perfect score!")
    elif score >= 2:
        print("Great job!")
    else:
        print("Keep practicing!")

    play_again = input(
        "\nDo you want to play again? (yes/no): "
    ).lower()

    if play_again != "yes":
        print("Thanks for playing!")
        print("Your highest score was:", high_score)
        break
