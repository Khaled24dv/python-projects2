
users ={}
def Register ():
  while True:  
    userName = input("Enter UserName : ").strip()
    if userName ==" ":
      print("username cannot be empty ")
      continue
    if userName in users:
      print("username is exists")
      continue
    password = input("enter password :").strip()
    if password == " ":
      print("password cannot empty .")
      continue
    if len(password)<6:
      print("password must be at least 6 characters .")
      continue
    users[userName]={"password":password,"balance":0}
    print("account created successfuly ")

def login ():
  username = input("enter username :").strip()
  password = input("enter password : ").strip()
  if username not in users:
    print("username does not exist .")
    return None
  if users[username]["password"]!=password  :
    print("incorect password :")    
    return None
  print("login successefuly .")
  return username

def BankMenu(current_user):
  while True:
    print("Bank Menu  \n")
    print("1 . check balance .")
    print("2 . deposite .")
    print("3 . withdraw .")
    print("4 . transfer .")
    print("5 . change password .")
    print("6 . logout .")

    choice = input("enter one choice in this choices .")
    if choice == 1:
      checkbalance(current_user)
    elif choice == 2:
      deposite (current_user)
    elif choice == 3:
      withdraw(current_user)
    elif choice == 4:
      transfer(current_user)
    elif choice == 5:
      changepassword(current_user)
    elif choice == 6:
      logout(current_user)
      print("logout successufuly .")
      break
    else :
      print("invalid option .")

def checkbalance(current_user):
  print(f"your current balance is : {users[current_user]['balance']} EGP ")


def deposite(current_user):
  amount = input("enter the amount of money is deposited .").strip()
  if amount <=0 :
    print("amount must be greater than 0.")
    return 
  users[current_user]["balance"] += amount
  print("deposite successefuliy .")
  print(f"the current balance = {users[current_user]["balance"]}")


def  withdraw(current_user):
  amount = input("enter the amount  withdraw .").strip()
  if amount<=0:
       print("amount must be greater than 0.")
       return
  if amount>users[current_user]["balance"]:
    print("insufficent balance :")
    return
  users[current_user]["balance"]-=amount
  print("wihtdrow successifuly :")
  print(f"the current balance is {users[current_user]["balance"]}")
    
  
def transfer(current_user):
    receiver = input("Enter receiver username: ").strip()

    if receiver not in users:
        print("User does not exist.")
        return

    if receiver == current_user:
        print("You cannot transfer to yourself.")
        return

    amount = float(input("Enter transfer amount: "))

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    if amount > users[current_user]["balance"]:
        print("Insufficient balance.")
        return

    users[current_user]["balance"] -= amount
    users[receiver]["balance"] += amount

    print("Transfer successful.")
    print(f"Your Current Balance: {users[current_user]['balance']} EGP")
    
def changepassword(current_user):
    old_password = input("Enter old password: ").strip()

    if users[current_user]["password"] != old_password:
        print("Incorrect old password.")
        return

    new_password = input("Enter new password: ").strip()

    if len(new_password) < 6:
        print("Password must be at least 6 characters.")
        return

    users[current_user]["password"] = new_password

    print("Password changed successfully.")

def logout(current_user):
   print("logout successifuly :")


def Main():
    while True:
        print("\n===== Main Menu =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            Register()

        elif choice == "2":
            current_user = login()

            if current_user:
                BankMenu(current_user)

        elif choice == "3":
            print("Thank you for using our bank.")
            break

        else:
            print("Invalid choice. Try again.")