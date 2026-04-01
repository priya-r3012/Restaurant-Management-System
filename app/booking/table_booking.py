class Booking_table:

    def __init__(self):
       
        self.tables = {
            1: {"10AM": "Free", "1PM": "Free", "4PM": "Free", "8PM": "Free"},
            2: {"11AM": "Free", "2PM": "Free", "5PM": "Free", "9PM": "Free"},
            3: {"9AM": "Free", "12PM": "Free", "3PM": "Free", "7PM": "Free"}
        }

  
    def show_tables(self):
        print("\n------ TABLE ------")
        for t in self.tables:
            print("\nTable", t)
            for time in self.tables[t]:
                print(" ", time, ":", self.tables[t][time])
        print("--------------------------")

    def book_table(self):
        self.show_tables()

        try:
            t = int(input("Enter table number: "))
            time = input("Enter time (9AM/10AM/11PM/12PM/1PM/2PM/3PM/4PM/5PM/7PM/8PM/9PM): ")

            if t in self.tables and time in self.tables[t]:

                if self.tables[t][time] == "Free":
                    name = input("Enter customer name: ")
                    persons = int(input("Enter number of persons: "))

                   
                    self.tables[t][time] = name + " (" + str(persons) + " persons)"

                    print("Table", t, "booked at", time)

                else:
                    print(" Already booked!")

            else:
                print(" Invalid table/time")

        except:
            print(" Wrong input")

    def cancel_booking(self):
        self.show_tables()

        try:
            t = int(input("Enter table number: "))
            time = input("Enter time: ")

            if t in self.tables and time in self.tables[t]:

                if self.tables[t][time] != "Free":
                    print("Cancelled:", self.tables[t][time])
                    self.tables[t][time] = "Free"
                else:
                    print(" Already free!")

            else:
                print(" Invalid input")

        except:
            print(" Error")



""" obj = Booking_table()

while True:
    print("\n===== TABLE BOOKING =====")
    print("1. Show Tables")
    print("2. Book Table")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        obj.show_tables()

    elif choice == '2':
        obj.book_table()

    elif choice == '3':
        obj.cancel_booking()

    elif choice == '4':
        print(" Thank you!")
        break

    else:
        print(" Invalid choice")

    """