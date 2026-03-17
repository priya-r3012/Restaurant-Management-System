import uuid 
import json
import os
class User:
    def __init__(self,role="staff"):
       
        self.user_id = str(uuid.uuid4())[0:4]
        self.role = role 
    def sign_up(self):

        print("Please enter your details for sign up:")

        name = input("Enter your name: ")
        if  name.isalpha() and name.title():
             pass
  
        else:
            print("Invalid name. Name should be only alphabet!")
            return None

        email = input("Enter your email: ")
        if "@" not in email:
            print("Invalid email.Email should be @ address")
            return None

        password = input("Create a password: ")
        if  password.isalnum() and len(password)>=8:
            pass

        else:
            print("Invalid password. Password should contain  alphabet or numbers!")
            return None
    
        if not name or not email or not password:
         print("Error: All  are required. Please try again.")
         return None
    
        user_id=str(uuid.uuid4())[0:4]
        print(f"User {name} is signed up with ID: {user_id}")
        
        try:
           with open(r"app/database/user_data.json", "r") as json_file:
              user_details=json.load(json_file)
        except(FileNotFoundError,json.JSONDecodeError):
            user_details=[]      
            
        new_user_details={
         "name" : name,
         "email" : email,
         "password" : password,
         "role" : self.role,
         "user_id" : user_id
       }
        
        user_details.append(new_user_details)                         
        
        with open (r"app/database/user_data.json","w") as json_file:
            json.dump(user_details, json_file, indent=4)

           
