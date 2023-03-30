import json
# USER records Sample
# userPass = {
#     "Adarsh" : 211,
#     "Hriday" : 233,
#     "Aman"  : "Aman@420",

# Fetching data from json
filename = "userrecords.json"
with open(filename, 'r') as f:
    userPass = json.load(f)


# Register the new user 
def createUser():
    print("Choose your username and password ")
    username = input("Choose your username : ")
    username = username.title()
    if username.isalnum():
    
        password  = input("Choose your password : ")
        cnfpass = input("Confirm your password : ")

        # Confiming  passwords
        if password == cnfpass:
            
            try:
                # Update the user record with new user 
                newUser = {username : password}
                newUser.update(userPass)
                
                with open(filename, 'w') as f:
                    json.dump( newUser, f)
                
                print("Operation Successfull !")

                userInput()

            except Exception as e:
                print(e)
            
            
        else:
            print("\tpasswords do not match ! ")

            createUser()

    else:
        print("Invalid username ! [special symbols not allowed ]")
        createUser()

        
# Log In user using USER records 
def userAuth(name):
    
    passw = input("Enter the password : ")
    passvalue = str(userPass.get(name))

    if passvalue == passw  :
        print("Logged In Successfully! ")
        
    else:
        print("Incorrect Password ! ")
        userAuth(name)


# Get keys form USER records into a list
userlist = userPass.keys()
userlist = list(userlist)


# For Sign IN or Sign UP confirmation
def userInput():
    usr = input("Enter username : ")
    usr = usr.title()

    if usr in userlist:
        print(f"Welcome {usr}")
        userAuth(usr)

    else:
        print("User not found ! \nRegister Yourself :  ")
        createUser()


welcomeMsg = '''\n********* Welcome to Adweb Solutions ********'''
print(welcomeMsg)
userInput()

userPass.update()

