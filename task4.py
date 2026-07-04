
### task 4 :
### ATM Simulator Smart :
PIN = 1234
balance =5000
PIN_User = int (input("enter password : "))
if PIN_User != PIN :
    print("the password is invalid :")
else:
       print("1->withdraw :")
       print("2->check balance :")
       choice = int (input("enter choice 1 or 2 :"))
       if choice == 1:
            val = int (input("enter number balanced withdarw :"))
            if val > balance:
                 print("invalid")
            else :
                 print(f"the number withdraw is = {val}")
                 print(f"the balanced = {balance-val}")
       elif choice ==2:
            print(f"the balance = {balance}")
       else:
            print("invalid choice : ")
           
            
      