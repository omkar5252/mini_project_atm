# My first ATM machine program.
import random

print(''' 
                          ***************************************************** 
                          *             WELCOME TO FIRSTBIT BANK              *
                          *****************************************************
    ''')
           
print("\nPlease insert your ATM card")
creation =" ACCOUNT CREATION "
print(creation.center(100,"*"))
name = input("Enter your name: ")
pin = int(input("Enter a pin you want to set:"))
account_number = random.randint(0000000000,9999999999)
print("\nCongratulations! Account created successfully......")

balance = 0

print('''
                                  ****************************
                                  *    1. Account details    *
                                  *    2. Balance enquiry    *
                                  *    3. Deposite cash      *
                                  *    4. Withdraw cash      *                                   
                                  *    5. Set new pin        *                    
                                  *    6. Exit               *                    
                                  ****************************
    ''')  
ch = 0
while (ch != 6):
        ch = int(input("\nEnter the choice you want to do: "))
        if (ch == 1):
            print("Account name:",name)
            print("Account number:",account_number)
            print("Available balance:",balance)
        
        elif (ch == 2):
            print("Total balance is Rs.",balance)

        elif (ch == 3):
            ammount = float(input("\nEnter the ammount of money you want to deposite:Rs."))
            if (ammount > 0):
                balance = balance + ammount
                print("Rs.",ammount,"is deposite sucessfully")
                print("Available balance is Rs.",balance)

        elif(ch == 4):
            ammount = float(input("\nEnter the amount of money you want to widthdraw:Rs."))
            if (ammount > balance):
                print("You don't have sufficient balance to make this widthdrawal")
            else:
                balance = balance - ammount
                print("Rs.",ammount,"is withdraw sucessfully")
                print("Available balance is Rs.",balance)

        elif (ch == 5):
            otp = random.randint(1111,9999)
            print("\nOne Time Password(OTP):",otp)
            i = 1
            while (i <= 3):
                otp_enter = int(input("\nPlease enter OTP here:"))
                i+=1
                if (otp == otp_enter):
                    new_pin = int(input("\nEnter your new pin:"))
                    print("\nYour new pin is set sucessfully.")
                    break
            else:
                print("\nPlease check your OTP.")
                print("Retry after sometime")
                
           
        elif (ch == 6):
            s = " PRINT RECEIPT "
            print(s.center(100,"*"))

            print("Account name:",name)
            print("Account number:",account_number)
            print("Available balance:",balance)

            s1 = " THANK YOU FOR CHOOSING US AS YOUR BANK "
            print(s1.center(100,"*"))
        else:
            print("\nPlease enter a correct value shown")

