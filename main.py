def songLyrics(thingOnBus, whatItDoes):
  print("the " + thingOnBus + " on the bus goes " + whatItDoes)
  print(whatItDoes + ", " + whatItDoes)
  print("the " + thingOnBus + " on the bus goes " + whatItDoes)
  print("all through the town")


songLyrics("doors", "open-and-shut")
print()
songLyrics("money", "clink-clink-clink")
print()


#write your 8-Ball program below:
import random

def magic8 (Name):
  possible_outcomes = ["Outlook is good", "Ask again later", "Yes", "No", "Most likely no", "Most likely yes", "Maybe", "Outlook is not good"]
  Random = random.randint(0, len(possible_outcomes) - 1)
  print(Name + ", " + possible_outcomes[Random])


name = input("Enter your name: ")
question = input("Enter your question: ")

magic8(name)



