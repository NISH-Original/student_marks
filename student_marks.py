import random

def validateVal(v):
  try:
    x = int(v)
    return x
  except:
    x=validateVal(input("Please enter a valid number: "))
    return x

NamesList = []
t = validateVal(input("Enter number of players: "))
for i in range(t):
    NamesList.append(input("Enter the name of player: "))

VerbList = ["eat", "yeet", "delete","kick", "lick", "chew on", "throw", "stare at", "trample", "destroy", "absolutely wreck", "rickroll", "nae nae", "do a barrel roll on", "slap", "drown", "play","ask for","steal or kidnap"]

NounList = ["Joe","a 20 foot tree", "the neighbors' Mercedes", "the essay due tomorrow", "Joe's Cat", "some petroleum jelly", "your phone", "AirPods", "his watch", "the teacher", "his dog", "an entire webseries","some Iodized Salt","the neighbors' lawn", "your TV", "some tissues", "your intelligence", "a wet mop", "your life", "a grand piano", "a bowling ball", "some toilet paper", "minecraft","Fortnite","Vinegar","your iPad","The person next to you","the person in front of you","anyone you like","no one"]

InFrontOfList = ["everyone", "the entire class", "your parents", "me", "a livestream", "the teacher", "that guy", "nobody","Joe", "a camera", "the police","some random person"]

while True:
    Verb = random.choice(VerbList)
    Noun = random.choice(NounList)
    InFrontOf = random.choice(InFrontOfList)
    Names = random.choice(NamesList)
    print("{}, I DARE YOU TO {} {} IN FRONT OF {}!\n" . format(Names.upper(),Verb.upper(),Noun.upper(),InFrontOf.upper()))

    if str.lower(input('Do you want another dare? Enter for yes, "n" for no: ')) == 'n':
        print("See you later!")
        break
