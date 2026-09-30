account = 80
main_loop = True

while True:
    for i in ["Welcome back!", "For withdrawal -> 1", "For deposit -> 2"]:
        print(i)

    choice = input("choice -> ")
    while main_loop:
        if choice == "1":
            withdrawals = int(input("Enter the value :"))
            if 0 < withdrawals <= account:
                account = account - withdrawals
                print(f"Successful operation : Your current balance -> {account}")
            elif withdrawals > account:
                print(
                    f"Your balance is insufficient. Your current balance is -> {account}"
                )
            else:
                print("The withdrawal number is illogical.")

        elif choice == "2":
            deposit = int(input("Enter the deposit amount and make the deposit : "))
            if deposit > 0:
                account = account + deposit
                print(f"Successful operation : Your current balance -> {account}")
            else:
                print("The deposit number is illogical. ")

        else:
            print("Invalid choice, try again. Try again ")
            break
        for i in ["Another operation", "Yes -> 1", "No -> 2"]:
            print(i)

        while True:
            choice1 = input("choice --> ")
            if choice1 == "1":
                main_loop = False
                break
            elif choice1 == "2":
                exit()
            else:
                print("Try again")
