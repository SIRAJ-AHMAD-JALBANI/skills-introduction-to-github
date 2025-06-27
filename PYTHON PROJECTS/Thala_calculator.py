# Thala Calculator(Ms Dhoni) - presented by Techinal coderji


def reason_by_string(n):
    string_n = str(n)
    out_string_list = []

    for i in range(len(string_n)):
        if string_n[i] == "7":
            out_string_list.append(f"7 at {i + 1}th Position of your Number.")


def get_thala_for_reason(user_input):
    output_list = []
    reason_list = []
    
    # TEST 1 - Direct String
    reason_list = reason_by_string(n):
    if reason_list:
        output_list.extend(reason_list)

    return output_list













def main():
    print("Welcome to thala calculator.")
    while True:
        user_input = int(input("Enter Any Number: "))   
        if user_input == 0:
            print("Thanks for using Thala Calculator. ")
            return 
        
        output_string = get_thala_for_reason(user_input)
        if output_string:
            print(output_string)
            print("Thala for Reason")
        else:
            print("No Thala for a reason")


if __name__ == "__main__":
    main()