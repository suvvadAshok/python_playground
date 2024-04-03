import random

gameTerms = ["rock", "paper", "scissor"]

while gameTerms:
    computer_choice = random.choice(gameTerms)

    human_choice = input("select your choice: ")
    human_choice = human_choice.lower()
    if gameTerms.count(human_choice):
        pass
    else:
        print("please..! make correct choice")
        break

    print(f"computer choice: {computer_choice}")

    if computer_choice == "rock":
        if human_choice == "paper":
            print("Wow! you won!")
            break
        elif human_choice == "scissor":
            print("Oooh! you lost")
            break
        else:
            print("ready for rematch")  

    elif computer_choice == "paper":
        if human_choice == "scissor":
            print("Wow! you won!")
            break
        elif human_choice == "rock":
            print("Oooh! you lost")
            break
        else:
            print("ready for rematch")

    else:
        if human_choice == "rock":
            print("Wow! you won!")
            break
        elif human_choice == "paper":
            print("Oooh! you lost")
            break
        else:
            print("ready for rematch")
