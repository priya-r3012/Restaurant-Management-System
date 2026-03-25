from app.auth.signup import User
from app.auth.login import login_user



class authentication:
 
   def menu(self):
    while True:
        print("-"*32)
        print("------- PICKWICK REGISTRATION MENU--------")
        print("="*32)
        print("/" +  "1.  Signup")
        print("/" +  "2.  Login")
        print("/" +  "3.  Exit")
        print("-"*32)
        self.user_input()

   def user_input(self):
    
    
        option=int(input("Select Any option: "))    
    

        if option == 1:
            User().sign_up()
           

        elif option == 2:
            login_user()
              

        elif option == 3:
            exit()

        else:
            print("invalid option")   






 



    

