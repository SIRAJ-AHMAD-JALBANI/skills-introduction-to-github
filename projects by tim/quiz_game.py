print("Welcome to my computer quiz!")

# ask the user if they want to play the game if yes then let them play else stop the code
playing = input("Do you want to play the game?(Enter Yes to play!) ")
if playing.lower() != "yes":
    quit()

print("Ok lets play!")
print("Give attention to spellings!")
score= 0
answer = input("What does Cpu stands for? ")
if answer.lower() == "central processing unit":
    print("Correct! ")
    score+= 1
else:
    print("Incorrect!")

answer = input("What does Gpu stands for? ")
if answer.lower() == "graphics processing units":
    print("Correct! ")
    score+= 1
else:
    print("Incorrect")
    
answer = input("What does Ram stands for? ")
if answer.lower() == "random access memory":
    print("Correct! ")
    score+= 1
else:
    print("Incorrect")
answer = input("What does Rom stands for? ")
if answer.lower() == "read only memory":
    print("Correct! ")
    score+= 1
else:
    print("Incorrect")
answer = input("What does ESC stands for? ")
if answer.lower() == "escape":
    print("Correct! ")
    score+= 1
else:
    print("Incorrect")

print(f"You got {score} marks out of 5! ")
print(f"You got {score / 5 * 100}% marks!")