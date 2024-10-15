import random


def SecretCodeGenerator():
    code = ''
    while len(code) < 4:
        digit = random.randrange(10)
        letter = str(digit)
        if letter not in code:
            code += letter
    return code


def Verifier(guess, code):
    guess = list(guess)
    code = list(code)
    bulls = 0
    cows = 0
    for i in range(len(code) - 1, -1, -1):
        if code[i] == guess[i]:
            bulls += 1
            code.pop(i)
            guess.pop(i)

    for i in range(len(code) - 1, -1, -1):
        if code[i] in guess:
            cows += 1
            code.pop(i)

    return bulls, cows


play = True
code = SecretCodeGenerator()
trials = 1
print("code generated")

while play:
    guess = input("Enter your 4 digit guess")
    while len(guess) != 4:
        guess = input("Please enter exactly 4 digits")
    bulls, cows = Verifier(guess, code)
    print("Bulls:", bulls, " Cows:", cows)
    if bulls == 4:
        print("Well done perfect guess, trials: ", trials)
        play = False
        print("Code was: ", code)
    else:
        trials += 1









