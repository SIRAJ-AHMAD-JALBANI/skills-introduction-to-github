#contact book main kiya hota hai contacts hotay hain 
import os
print("Welcome to contacts.")
print()
active = True
while active:
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    prompt = int(input())
    if prompt == 1:
        contact =input("Enter contact in this style -> name : contact.  ")
        with open('contact.txt','w') as file:
            file.write(contact)

    elif prompt == 2:
        if os.path.exists('contact.txt'):
            with open('contact.txt', 'r') as file:
                print(file.read())
        else:
            print("The file does not exist!")
    elif prompt == 3:
        # Opening the file in read mode
        if os.path.exists('contact.txt'):
            with open("contact.txt", "r") as file:
                # Searching keyword
                search = input("Search here.. ")
                search_term = search
                # Read through the file line by line
                for line_number, line in enumerate(file, start=1):
                    if search_term in line:
                        print(f"Found '{search_term}' on line {line_number}: {line.strip()}")
                    else:
                        print(f"{search_term} is not found!")
        else:
            print("The file does not exist!")
    elif prompt == 4:
        if os.path.exists('contact.txt'):
            os.remove('contact.txt')
        else:
            print("The file does not exist!")
    answer = input("Do you want to exit or not!Enter q to exit!")
    if answer == 'q':
        active = False




