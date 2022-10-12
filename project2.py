import time
from random import randrange


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def select_villain(villain):
    random_index = randrange(len(villain))
    return villain[random_index]


def intro(villain):
    print_pause("You find yourself standing in an open field, filled with"
                " grass and yellow wildflowers")
    print_pause("Rumor has it that a " + villain + " is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                "dagger.\n")


def field(items, villain):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?")
    while True:
        response = input("(Please enter 1 or 2.)\n").lower()
        ans = 'incorrect'
        while (ans == 'incorrect'):
            if (response.lower() == "1"):
                house(items, villain)
                ans = 'correct'
                break
            elif (response.lower() == "2"):
                cave(items, villain)
                break
            else:
                print("Sorry, I don't understand.")
                response = input()


def play_again(items):
    while True:
        res1 = input("Would you like to play again? (y/n)\n").lower()
        ans = 'incorrect'
        while (ans == 'incorrect'):
            if (res1.lower() == "y"):
                print("Excellent! Restarting the game ...")
                main()
                ans = 'correct'
            elif (res1.lower() == "n"):
                print("Thanks for playing! See you next time.")
                exit(0)
            else:
                print("Sorry, I don't understand.")
                res1 = input()


def house(items, villain):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps"
                " a " + villain + ".")
    print_pause("Eep! This is the " + villain + " house!")
    print_pause("The " + villain + " attacks you!")
    if "Sword of Ogoroth" in items:
        fight_fly(items, villain)
    else:
        print_pause("You feel a bit under-prepared for this, what with only"
                    " having a tiny dagger.")
        fight_fly(items, villain)


def fight_fly(items, villain):
    while True:
        choice = input("Would you like to (1) fight or (2) run away?")
        if choice == '1':

            if "Sword of Ogoroth" in items:
                print_pause("As the " + villain + " moves to attack, "
                            "you unsheath your new sword")  # random
                print_pause("The Sword of Ogoroth shines brightly in your hand"
                            " as you brace yourself for the attack")
                print_pause("But the " + villain + " takes one look at your"
                            " shiny new toy and runs away!")  # random
                print_pause("You have rid the town of the " + villain + "."
                            " You are victorious!")
                play_again(items)
                break
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the "
                            + villain + ".")
                print_pause("You have been defeated!")
                print_pause("GAME OVER!!")
                play_again(items)
                break
        elif choice == '2':
            print_pause("You run back into the field. Luckily, you don't"
                        " seem to have been followed.")
            field(items, villain)
            break


def cave(items, villain):
    print_pause("You peer cautiously into the cave.")

    if "Sword of Ogoroth" in items:
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field(items, villain)
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword"
                    " with you.")
        items.append("Sword of Ogoroth")
        print_pause("You walk back out to the field.")
        field(items, villain)


def main():
    items = []
    villains = ['pirate', 'troll', 'monster', 'evil clown']
    villain = select_villain(villains)
    intro(villain)
    field(items, villain)


main()
