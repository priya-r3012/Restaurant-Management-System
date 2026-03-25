from app.menu.menu_list import Menu_Rms
class admin_dashboard():

    def admin_menu(self):
        print("ADMIN MENU - RMS")
        print("1. Manage menu")
        print("2. Order")
        print("3. Booking")
        print("4. Report")
        print("5. Exit")
        self.admin_input()

    def admin_input(self):
        option=int(input("Select any Option: "))    
    
        if option == 1:
             self.manage_menu()
        elif option == 2:
             self.order()
        elif option == 3:
             self.booking()
        elif option == 4:
             self.repor5()
        elif option == 5:
             exit()
        else:
             print("invalid option")  

   