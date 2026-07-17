pin = int(input("Enter pin: "))
balance = 10000
if pin == 12345:
    amount = int(input("Enter Amount: "))
    if amount <= balance:
        print("Transaction Successful")
    else:
        print("Transaction Failed")
else:
    print("Incorrect pin")