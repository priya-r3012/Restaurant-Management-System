from app.auth.signup import User
from app.auth.login import login_user

class authentication:
 
   def menu(self):
    while True:
        print("-"*32)
        print("-------REGISTRATION MENU--------")
        print("="*32)
        print("|" +  "1.  Signup".ljust(30) + "|")
        print("|" +  "2.  Login".ljust(30) + "|")
        print("|" +  "3.  Exit".ljust(30) + "|")
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

#obj=authentication()   
#obj.menu()
       




 



    

