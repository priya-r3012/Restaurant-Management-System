class staff_dashboard():

    def staff_menu(self):
        print("-"*32)
        print("=======STAFF MENU - RMS=========")
        print("-"*32)
        print("|" + "1.  View Menu".ljust(30) + "|")
        print("|" + "2.  Take Order".ljust(30) + "|")
        print("|" + "3.  Booking".ljust(30) + "|")
        print("|" + "4.  Cancel Order".ljust(30) + "|")
        print("|" + "5.  Generate Bill".ljust(30) + "|")
        print("|" + "6.  Exit".ljust(30) + "|")
        print("-"*32)
        self.staff_input()

    def staff_input(self):
        option=int(input("Select any Option: "))    
    
        if option == 1:
             self.view_menu()
        elif option == 2:
             self.take_order()
        elif option == 3:
             self.booking()
        elif option == 4:
             self.cancel_order()
        elif option == 5:
             self.generate_bill()
        elif option == 6:
             exit()
        else:
            print("invalid option")  

