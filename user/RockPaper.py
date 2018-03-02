import random
import time

responses = ("rock","paper","scissors")

###
question = input("What shall you play? Rock, paper, or scissors?")
print("rock...")
time.sleep(2)
print("paper...")
time.sleep(2)
print("scissors!")
print("I played..." + random.choice(responses))
print("\n")


if question == "paper" and responses == "scissors":
    print ("you lose")

