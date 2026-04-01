from app.auth.signup import User
from app.auth.login import login_user
from app.dashboard.admin import Admin_dashboard
from app.dashboard.staff import Staff_dashboard


class Authentication:
 
   def menu(self):
    while True:
        print("-"*32)
        print("------- PICKWICK REGISTRATION MENU--------")
        print("="*32)
        print( "1.  Signup")
        print( "2.  Login")
        print( "3.  Exit")
        print("-"*32)
        self.user_input()

   def user_input(self):
    
    
        option=int(input("Select Any option: "))    
    

        if option == 1:
            User().sign_up()
           

        elif option == 2:
            user_role=login_user()

            if user_role=="admin":
                obj=Admin_dashboard()
                obj.admin_menu()
                return

            elif user_role=="staff":
                obj=Staff_dashboard() 
                obj.staff_menu() 
                return 
        elif option == 3:
            exit()

        else:
            print("invalid option")   






 



    

