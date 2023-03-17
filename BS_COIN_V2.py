import subprocess
import socket
import time 


def checkbalance():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    class ATM:
        def __init__(self, file_name):
            self.file_name = file_name

        def check_balance(self):
            with open(self.file_name, 'r') as file:
                number_string = file.read().strip()  # read the file contents and remove any leading/trailing white space
                balance = int(number_string)  # convert the string to an integer
            return balance

        def deposit(self, amount):
            with open(self.file_name, 'r') as f:
                balance = float(f.read())
            balance += amount

    atm = ATM(ip_address + '.txt')
    print(f"Your balance is: ${atm.check_balance():.2f}")
    question()


def trade():
    import os


    # Define the USB drive path
    usb_drive_path = "yes"

    # Get the hostname and IP address of the sender
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

# Prompt the user for the message amount, recipient's IP address, and file path
    message = int(input("Enter how much you want to give: "))
    ipname = input("What is the recipient's IP address: ")
    file_path = input("What is the file path (where the file is located): ")

# Define the filename for the balance text file
    balancename = ip_address + ".txt"

# Check if the balance file exists and is not empty
    if os.path.exists(balancename) and os.path.getsize(balancename) > 0:
    # Open the balance file and read its contents
        with open(balancename, "r") as file:
            number_string = file.read().strip()  # read the file contents and remove any leading/trailing white space
            number = int(number_string)  # convert the string to an integer
    else:
    # If the file doesn't exist or is empty, set the balance to 0
        number = 0

# Check if the sender has sufficient balance to send the message amount
    if number < message:
        print("Sorry, you do not have enough balance to send this amount.")
        print("Please try again later.")
        quit()

    # Deduct the message amount from the sender's balance
    number -= message

    # Write the new balance to the sender's balance file
    with open(balancename, "w") as file:
        file.write(str(number))

# Add the message amount to the recipient's balance
    filename = ipname + ".txt"
    recipient_balance_file = os.path.join(file_path, filename)
    if os.path.exists(recipient_balance_file) and os.path.getsize(recipient_balance_file) > 0:
        with open(recipient_balance_file, "r") as file:
            number_string = file.read().strip()  # read the file contents and remove any leading/trailing white space
            number = int(number_string)  # convert the string to an integer
    else:
        number = 0

    number += message

    with open(recipient_balance_file, "w") as file:
        file.write(str(number))

# Prompt the user to confirm if the recipient has received the message
    while True:
        response = input("Has the recipient received the message? (y/n)")

        if response.lower() == "y":
            print("Message delivered successfully.")
            break
        elif response.lower() == "n":
            print("Please try again later.")
            break
        else:
            print("Invalid response. Please enter 'y' or 'n'.")

# Print a confirmation message
    print("amount saved to USB drive.")

    question()






def tutorial():
    print("Thank you for using BS coin")
    print("this is a currency that allows you to trade it with your mates")
    print(" (if you have any) ")
    time.sleep(1)
    print("we are also working hard to get the stocks part of it up and running")
    print("so you can invest in companys to earn more BS coin")
    time.sleep(2)
    print("to trade with your friends you need to have an internet connection")
    print("and you need a usb. first plug the usb (with this folder on it) ")
    time.sleep(2)
    print("into their computer and and run the trade program from the main app")
    print(" (this one) ")
    time.sleep(1)
    print("then just follow the instruction and BOOM you have given your mate some")
    print("BS coin")
    time.sleep(1)
    print("credits: chatGPT: 40%, oliver deakin: 50%, random people on stack overflow: 10%")
    
def question():
    print("pick an option below")
    option = input("""[1] Check balance, [2] Trade with others,
[3] replay tutorial, [4] quit: """)
    if option == "1":
        checkbalance()
        
    elif option == "2":
        trade()
        
    elif option == "3":
        tutorial()
        
    elif option == "4":
        quit()

        
    

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
filename = ip_address + '.txt'


print("Are you new to BS coin [y/n]")
action = input()

if action == "y" or action == "Y":
    print("Thank you for using BS coin")
    print("this is a currency that allows you to trade it with your mates")
    print(" (if you have any) ")
    time.sleep(1)
    print("we are also working hard to get the stocks part of it up and running")
    print("so you can invest in companys to earn more BS coin")
    time.sleep(2)
    print("to trade with your friends you need to have an internet connection")
    print("and you need a usb. first plug the usb (with this folder on it) ")
    time.sleep(2)
    print("into their computer and and run the trade program from the main app")
    print(" (this one) ")
    time.sleep(1)
    print("then just follow the instruction and BOOM you have given your mate some")
    print("BS coin")
    time.sleep(1)
    print("credits: chatGPT: 40%, oliver deakin: 50%, random people on stack overflow: 10%")
    with open(filename, 'a') as f:
        f.write("10")
        f.close()
    question()

if action == "n" or action == "N":
    with open(filename, 'a') as f:
        
        f.close()
    question()


    
    



