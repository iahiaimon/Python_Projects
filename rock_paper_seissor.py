import random

print("\nHey lets play Rock paper seissor....\n")
while True:
    user = input("Choose your choice: ");
    bot = random.choice(['rock' , 'paper' , 'seissor'])
    print()

    print("The user choose: ", user)
    print("The bot choose: ", bot)
    print()

    if (user == bot) :
        print("Same choice! Match Draw...")
    elif(user == "rock" and bot == "seissor"):
        print("User choose Rock User Win")
    elif(user == "paper" and bot == "rock"):
        print("User Choose Paper User Win!")
    elif(user == "seissor" and bot == "paper"):
        print("User choose seissor User Win!")
    else:
        print (f"Bot choose {bot}, Bot Win!")
    print("---------------------")
    print()



