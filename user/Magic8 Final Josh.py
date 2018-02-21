import random
import time
responses = ["Not so sure", "Only time will tell", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never in a million years",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable", "Oh lord, forgive me for what I have seen", "entrer dans le vide, paysan", "le vide consommera toutes les cellules de votre corps", "是的，但用中文"]

## asks you question
## time.sleep(2) stops the timer for two seconds, so the 'hmm's will come 2 seconds after each other
def answer():
    question = input("Ask Jason Vu The Wise a question and you shall receive... ")
    print("Let me dig deep into the fabric of the universe, and find your answer")
    time.sleep(2)
    print("Hmm")
    time.sleep(2)
    print("Hmmm")
    time.sleep(2)
    print("Hmmmm")
    time.sleep(2)
    print("Ah!")
    time.sleep(1)
    print(random.choice(responses))
    print("\n")
answer()

## I'm pretty sure "\n" just leaves a space
## asks for play again
## I lent Jason Vu my expertise
secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
while secondQuestion == str("Y"):
    answer()
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
else:
    print(input("Press any key to exit"))
