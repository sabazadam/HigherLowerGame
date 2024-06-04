from game_data import data
from art import *
from random import randint
print(logo)
randomIndex = randint(0,len(data) - 1)
randomIndex2 = randint(0,len(data) - 1)
score = 0
def take2differentItemInArray():
    while True:
        randomIndex = randint(0, len(data) - 1)
        randomIndex2 = randint(0,len(data) - 1)
        if randomIndex != randomIndex2:
            break
    return [data[randomIndex],data[randomIndex2]]

def game():
    liste = take2differentItemInArray()
    for i in range(2):
        print(f"{liste[i]['name']}, {liste[i]['description']}, from {liste[i]['country']}")
        if i == 0: print(vs)
    response = input("Who has more follower 'A' or 'B': " )
    if response.lower() == "a":
        if liste[0]['follower_count'] > liste[1]['follower_count']:
            return True
        else:
            return False
    else:
        if liste[1]['follower_count'] > liste[0]['follower_count']:
            return True
        else:
            return False
while game():
    score += 1
    print(f"You're right! Current score: {score}")
print(f"Sorry that's wrong. Final score= {score}")
