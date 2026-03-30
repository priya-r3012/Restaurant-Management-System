from app.menu.menu_list import Menu_Rms
from app.booking.table_booking import Booking_table
from app.report.restaurant_report import Order_complete_weekly
from app.billing.customer_bill import Bill

class Admin_dashboard:

    def menu(self):
        print("ADMIN MENU - RMS")
        print("1. Display menu")
        print("2. Order")
        print("3. Booking")
        print("4. Report")
        print("5. Show Bill")
        print("6. Exit")
        self.admin_input()

    def admin_input(self):
        option=int(input("Select any Option: "))    
    
        if option == 1:
             Menu_Rms().display_menu()

        elif option == 2:
             Menu_Rms().select_item()

        elif option == 3:
             Booking_table()
             
        elif option == 4:
             Order_complete_weekly().weekly_report()

        elif option == 5:
             Bill().generate_bill()

        elif option == 6:
             exit() 
                 
        else:
             print("invalid option")  

   