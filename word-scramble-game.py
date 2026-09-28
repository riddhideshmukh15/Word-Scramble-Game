import random

words = {
    "python": "A programming language",
    "computer": "An electronic machine",
    "keyboard": "Used for typing",
    "developer": "A person who creates software",
    "internet": "Used to connect computers worldwide"
}

while True:

    score = 0

    print("\n=== WORD SCRAMBLE GAME ===")
    print("You have 3 rounds!")

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

        guess = input("Enter your answer: ").lower()

        if guess == word:
            print("Correct! You won!")
            score = score + 1
        else:
            print("Wrong answer!")
            print("Correct word was:", word)

    print("\n=== GAME OVER ===")
    print("Your final score:", score, "/ 3")

    if score == 3:
        print("Excellent! Perfect score!")
    elif score >= 2:
        print("Great job!")
    else:
        print("Keep practicing!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break