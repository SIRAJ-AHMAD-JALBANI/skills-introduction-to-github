name = input("Type your name: ")
print("Welcome",name,"to this adventure!")

answer = input("You are on a dirt road, it has "
"come to an end and you can go left or right."
" Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You  come to a river, you can walk around it or swim accross. Type walk to walk around it and swim  to swim accross: ")

    if answer =='swim':
        print("You swam accross and were eaten by an alligator.")
    elif answer == 'walk':
        print("You walked for many miles, ran out of water and you lost the game.")

    else:
        print('Not a valid option. You lose.')

elif answer =="right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross to or heck back (cross/ back)? ")
    if answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them(Yes or no)?").lower()
        if answer == 'yes':
            print("You talk to the stranger and they give you gold. You Win! ")
        if answer == 'no':
            print("You ignored the stranger and they are offended and you lose.")
    elif answer == 'back':
        print("You lost!")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thank for playing the game!",name)