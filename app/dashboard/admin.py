from app.menu.menu_list import Menu_Rms
from app.booking.table_menu import Table
from app.report.restaurant_report import Order_complete_weekly
from app.billing.customer_bill import Bill


class Admin_dashboard:
    
    def __init__(self,cart):
        self.cart=cart

    def admin_menu(self):
       while True: 
        print("-"*32)
        print("ADMIN MENU - RMS")
        print("1. Display menu")
        print("2. Order")
        print("3. Booking")
        print("4. Report")
        print("5. Show Bill")
        print("6. Exit")
        print("-"*32)
        self.admin_input()

    def admin_input(self):
        option=int(input("Select any Option: "))    
    
        if option == 1:
             Menu_Rms().display_menu()

        elif option == 2:
             Menu_Rms().select_item()

        elif option == 3:
             Table().tablemenu()
             
        elif option == 4:
             Order_complete_weekly().weekly_report()

        elif option == 5:
             Bill(cart=self.cart).generate_bill()

        elif option == 6:
             exit() 
             return
                 
        else:
             print("invalid option")  

   