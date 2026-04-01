from app.booking.table_booking import Booking_table

class Table:
   def tablemenu(): 
    print("\n===== TABLE BOOKING =====")
    print("1. Show Tables")
    print("2. Book Table")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        Booking_table().show_tables()

    elif choice == '2':
        Booking_table().book_table()

    elif choice == '3':
        Booking_table().cancel_booking()

    elif choice == '4':
        print(" Thank you!")

    else:
        print(" Invalid choice")

   