import random
words = ["python","Computer","keyboard","developer"]
word=random.choice(words)
scrambled=list(word)
random.shuffle(scrambled)
scrambled_word="".join(scrambled)
print("===WORD SCRAMBLE GAME")
print("Unscramble this word:",scrambled_word)
guess=input("Enter your answer:").lower()
if guess==word:
    print("Correct!you won!")
else:
    print("wrong answer!")
    print("The correct word was:",word)