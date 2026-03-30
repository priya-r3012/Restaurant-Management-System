from app.menu.menu_list import Menu_Rms

class Staff_dashboard:

    def menu(self):
        print("-"*32)
        print("=======STAFF MENU - RMS=========")
        print("-"*32)
        print("/" + "1.  View Menu")
        print("/" + "2.  Take Order")
        print("/" + "3.  Update")
        print("/" + "4.  Cancel Order")
        print("/" + "5.  Exit")
        print("-"*32)
        self.staff_input()

    def staff_input(self):
        option=int(input("Select any Option: "))    
    
        if option == 1:
             Menu_Rms().display_menu()
        elif option == 2:
             Menu_Rms().select_item()
        elif option == 3:
             Menu_Rms().update_item()
        elif option == 4:
             Menu_Rms().cancel_item()
        elif option == 5:
             exit()
        else:
            print("invalid option")  

