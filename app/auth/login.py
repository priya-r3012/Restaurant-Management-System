import json


def login_user():
    print("---LOGIN---")
    try:
    
        with open (r"app/database/user_data.json",'r') as file:
          user_data = json.load(file) 
    except FileNotFoundError:
        print("Error: User file not found")
        return
    
    user_email=input("Enter Email: ")
    user_password=input("Enter Password: ")

    user_found = False
    for user in user_data:
        if user_email == user["email"] and user_password == user["password"]:
            user_found=True
            break
     
    if user_found:
        print("Login successfull!") 
    else:
        print("Invalid email or password!")
