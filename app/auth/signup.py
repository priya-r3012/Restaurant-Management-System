import uuid 
import json
import os
import pwinput

class User:
    def __init__(self,role="staff"):
       
          self.user_id = str(uuid.uuid4())[0:4]
          self.role = role 

    def sign_up(self):
      
        print("Please enter your details for sign up:")

        while True:
           name = input("Enter your name: ")
           name = name.title()
           if  name.isalpha():
              break
  
           else:
              print("Invalid name. Name should be only alphabet!")

        try:
             with open(r"app/database/user_data.json", "r") as json_file:
                user_details=json.load(json_file)
        except(FileNotFoundError,json.JSONDecodeError):
            user_details=[]          

        while True:
            email = input("Enter your email: ")
            if "@" not in email and "." not in email:
               print("Invalid email.Email should contain  @  and . both in address") 

            if any(user["email"] == email for user in user_details):
                print("Email already registered!")   
                continue 
            break
        
        while True:
            password = pwinput.pwinput("Create password: ")
            if  password.isalnum() and len(password)>=8:
               break
    
            else:
               print("Invalid password. Password should contain  alphabet or numbers!")
        
    
        if not name or not email or not password:
              print("Error: All  are required. Please try again.")
         
    
        user_id=str(uuid.uuid4())[:6]
        print(f"User {name} registered successfully!")
        print(f"Your User ID: {user_id}")
            
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
 
           
