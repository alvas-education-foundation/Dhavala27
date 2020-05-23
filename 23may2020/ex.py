user_name= input("Enter user name: ")
password= input("Enter password: ")
         
for i in range(3):
    if user_name == 'Micheal' and password == 'e3$WT89x':
        print("You have successfully login")
        break
    elif i==2:
        print("Account locked!")
        break
    else:
        print("Wrong Username or password")
        user_name= input("Enter user name: ")
        password= input("Enter password: ")
