import json
import pwinput
from app.dashboard.admin import Admin_dashboard
from app.dashboard.staff import Staff_dashboard


def login_user():
    print("\n---LOGIN---")
    try:
    
        with open (r"app/database/user_data.json",'r') as file:
          user_data = json.load(file) 
    except FileNotFoundError:
        print("Error: User file not found.")
        return
    
    user_email=input("* Enter Email: ")
    user_password=pwinput.pwinput("* Enter Password: ")

    user_found = False
    for user in user_data:
        if user_email == user["email"] and user_password == user["password"]:
           
            return user["role"]

        

            user_found=True
            break
     
    if user_found:
        print("Login successfull!") 
    else:
        print("User not found.Invalid email or password!")
