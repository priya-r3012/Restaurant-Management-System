
import json
class Menu_Rms:

    def __init__(self):
        self.menu = [
               {"id": 1 , "name": "Aloo Paratha", "type": "Breakfast" , "half": 40 , "full": 80},
               {"id": 2 , "name": "Paneer Paratha", "type": "Breakfast" , "half": 60 , "full": 100},
               {"id": 3 , "name": "Poha", "type": "Breakfast" , "half": 30 , "full": 60},
               {"id": 4 , "name": "Upma", "type": "Breakfast" ,"half": 35 , "full": 70},
               {"id": 5 , "name": "Tea", "type": "Breakfast" , "half": 20 , "full": 40},
               {"id": 6 , "name": "Dahi", "type": "Breakfast" , "half": 40 , "full": 80},            
               {"id": 7 , "name": "Veg Thali", "type": "Lunch" ,"half": 120, "full": 200},
               {"id": 8 , "name": "Dal Rice","type": "Lunch" , "half": 80, "full": 150},
               {"id": 9 , "name": "Rajma Rice", "type": "Lunch" ,"half": 90, "full": 160},
               {"id": 10 , "name": "Paneer Butter Masala","type": "Lunch" , "half": 140, "full": 260},
               {"id": 11 , "name": "Chappati (2 pcs)","type": "Lunch" , "half": 30, "full": 60},          
               {"id": 12 , "name": "Butter Chicken","type": "Dinner" , "half": 180, "full": 320},
               {"id": 13 , "name": "Kadhai Paneer","type": "Dinner" , "half": 150, "full": 280},
               {"id": 14 , "name": "Tandoori Roti","type": "Dinner" , "half": 20, "full": 40},
               {"id": 15 , "name": "Jeera Rice", "type": "Dinner" ,"half": 80, "full": 140},
               {"id": 16 , "name": "Dal Makhani","type": "Dinner" , "half": 120, "full": 220},       
               {"id" : 17 , "name": "Paneer Tikka" ,"type": "Veg" , "half": 150, "full": 280},
               {"id" : 18 , "name": "Veg Manchurian" ,"type": "Veg" , "half": 120, "full": 220},
               {"id" : 19 , "name": "Spring Roll","type": "Veg" , "half": 100, "full": 180},
               {"id" : 20 , "name": "Chilli Paneer","type": "Veg" , "half": 140, "full": 260},
               {"id" : 21 , "name": "Hara Bhara Kabab","type": "Veg" , "half": 130, "full": 240},          
               {"id" : 22 , "name": "Chicken Tikka","type": "Non-Veg" , "half": 180, "full": 320},
               {"id" : 23 , "name": "Chicken Lollipop", "type": "Non-Veg" ,"half": 170, "full": 300},
               {"id" : 24 , "name": "Fish Fry", "type": "Non-Veg" ,"half": 200, "full": 350},
               {"id" : 25 , "name": "Mutton Kabab","type": "Non-Veg" , "half": 220, "full": 380},
               {"id" : 26 , "name": "Chicken","type": "Non-Veg" ,"half": 160, "full": 290},           
               {"id" : 27 , "name": "Veg Soup" , "type": "Soups" ,"half": 80, "full": 140},
               {"id" : 28 , "name": "Tomato Soup", "type": "Soups" ,"half": 70, "full": 130},
               {"id" : 29 , "name": "Sweet Corn Soup",  "type": "Soups" ,"half": 90, "full": 150},
               {"id" : 30 , "name": "Chicken Soup",  "type": "Soups" ,"half": 100, "full": 170},
               {"id" : 31 , "name": "Hot & Sour Soup", "type": "Soups" , "half": 85, "full": 145},                  
               {"id" : 32 , "name": "Masala Papad", "type": "Appetizers" , "half": 40, "full": 70},
               {"id" : 33 , "name": "French Fries", "type": "Appetizers" ,  "half": 90, "full": 150},
               {"id" : 34 , "name": "Cheese Balls", "type": "Appetizers" ,  "half": 120, "full": 200},
               {"id" : 35 , "name": "Garlic Bread", "type": "Appetizers" ,  "half": 110, "full": 180},
               {"id" : 36 , "name": "Veg Cutlet", "type": "Appetizers" ,  "half": 100, "full": 170},                      
               {"id" : 37 , "name": "Cold Coffee" , "type": "Tea & Coffee" ,  "half": 90, "full": 150},
               {"id" : 38 , "name": "Hot Coffee", "type": "Tea & Coffee" ,"half": 70, "full": 120},
               {"id" : 39 , "name": "Tea", "type": "Tea & Coffee" ,"half": 30, "full": 50},
               {"id" : 40 , "name": "Green Tea","type": "Tea & Coffee" , "half": 40, "full": 60},
               {"id" : 41 , "name": "Lemon Tea","type": "Tea & Coffee" , "half": 50, "full": 80},                  
               {"id": 42 , "name": "Banana Shake", "type": "Shakes & Juice" ,"half": 80, "full": 140},
               {"id": 43 , "name": "Chocolate Shake", "type": "Shakes & Juice" ,"half": 100, "full": 160},
               {"id": 44 , "name": "Strawberry Shake","type": "Shakes & Juice" , "half": 100, "full": 160},
               {"id": 45 , "name": "Pineapple Juice", "type": "Shakes & Juice" ,"half": 90, "full": 150},
               {"id": 46 , "name": "Orange Juice", "type": "Shakes & Juice" ,"half": 90, "full": 150},
               {"id": 47 , "name": "Apple Juice","type": "Shakes & Juice" , "half": 100, "full": 160},
               {"id": 48 , "name": "Watermelon Juice", "type": "Shakes & Juice" ,"half": 80, "full": 140},
               {"id": 49 , "name": "Grapes Juice","type": "Shakes & Juice" , "half": 90, "full": 150},
               {"id": 50 , "name": "Butter Milk","type": "Shakes & Juice" , "half": 50, "full": 80},
               {"id": 51 , "name": "Lassi", "type": "Shakes & Juice" ,"half": 70, "full": 120},
               {"id": 52 , "name": "Mango Shake","type": "Shakes & Juice" , "half": 90, "full": 150},       
               {"id" : 53 , "name": "Coke","type": "Cold Drink" , "half": 40, "full": 70},
               {"id" : 54 , "name": "Pepsi", "type": "Cold Drink" ,"half": 40, "full": 70},
               {"id" : 55 , "name": "Sprite","type": "Cold Drink" , "half": 40, "full": 70},
               {"id" : 56 , "name": "Fanta","type": "Cold Drink" , "half": 40, "full": 70},
               {"id" : 57 , "name": "Thumbs Up","type": "Cold Drink" , "half": 40, "full": 70},
               {"id" : 58 , "name": "Mineral Water","type": "Cold Drink" , "half": 20, "full": 30},
               {"id" : 59 , "name": "Fresh Lime Soda","type": "Cold Drink" , "half": 60, "full": 100},
               {"id" : 60 , "name": "Ice Cream Vanilla","type": "Dessert" , "half": 60, "full": 100},
               {"id" : 61 , "name": "Ice Cream Chocolate", "type": "Dessert" ,"half": 70, "full": 110},
               {"id" : 62 , "name": "Gulab Jamun","type": "Dessert" , "half": 50, "full": 90},
               {"id" : 63 , "name": "Rasgulla","type": "Dessert" , "half": 50, "full": 90},
               {"id" : 64 , "name": "Brownie","type": "Dessert" , "half": 90, "full": 150},
               {"id" : 65 , "name": "Falooda","type": "Dessert" , "half": 100, "full": 160},
               {"id" : 66 , "name": "Kulfi","type": "Dessert" , "half": 60, "full": 100},        
               {"id" : 67 , "name": "Boondi Raita" ,"type": "Raita" , "half": 50, "full": 100},
               {"id" : 68 , "name": "Boondi Raita" ,"type": "Raita" , "half": 50, "full": 100},
               {"id" : 69 , "name": "Boondi Raita" , "type": "Raita" ,"half": 50, "full": 100}

        ]
        self.cart = []
        self.total = 0

    def load_menuu(self):
     try:
      with open(r"app\database\menu_items.json",'r') as json_file:
        self.menu=json.load(json_file)
     except:
        print("Error during load menu") 


    
        self.cart=[]

    def display_menu(self):
        print("\n--------------------------------- PICKWICK FULL MENU -----------------------------------------------")

        print("-" * 100)

        types={}

        for item in self.menu:
            if item["type"] not in types:
                types[item["type"]] = []
            types[item["type"]].append(item)

        for t,items in types.items():
         
            print("-"*100)
            print(f"Category : {t}")
            print("-"*100)
            print(f"{'ID':<30}{'Name':<35}{'Half':<30}{'Full':<30}")    
            print("-"*100) 
            for item in items:
             print(f"{item['id']:<30}{item['name']:<35}₹{item['half']:<30}₹{item['full']:<30}")

        print("-" * 100)

    def select_item(self):
        print("\n------- SELECT ITEM -------")
        while True:
            try:
                user_input = input("\nEnter Item ID: ")
                item_id = int(user_input)
                
                if item_id == 0: break

             
                item = next((i for i in self.menu if i["id"] == item_id), None)

                if item:
                    option = input(f"Select plate for {item['name']} (h=Half / f=Full): ").lower()
                    price = item['half'] if option == 'h' else item['full']
                    plate = "Half" if option == 'h' else "Full"

                    
                    self.cart.append({
                        'id': item['id'],
                        'name': item['name'],
                        'plate': plate,
                        'price': price
                    })
                    self.total += price
                    print(f"Added: {item['name']} ({plate}) - ₹{price}")
                else:
                    print(" Invalid Item ID!")

            except ValueError:
                print(" Please enter a valid number!")

    def cancel_item(self):
        if not self.cart:
            print("\nYour cart is empty.")
            return

        while True:
            print("\n--- Your Cart ---")
            for i, item in enumerate(self.cart, 1):
                print(f"{i}. {item['name']} ({item['plate']}) - ₹{item['price']}")
            
            print(f"Current Total: ₹{self.total}")
            
            cancel = input("\nRemove an item? (y/n): ").lower()
            if cancel == 'y':
                try:
                    num = int(input("Enter item number to remove: "))
                    if 1 <= num <= len(self.cart):
                        removed = self.cart.pop(num - 1)
                        self.total -= removed['price']
                        print(f" Removed: {removed['name']}")
                    else:
                        print(" Invalid number")
                except ValueError:
                    print(" Invalid input")
            else:
                break

    def update_item(self, cart, total):

        while True:
            print("\nYour Cart:")

            i = 0
            for item in cart:
                print(i + 1, ".", item[1], "(", item[2], ")")
                i += 1

            update = input("\nDo you want to update any item? (y/n): ")

            if update == 'y':
                try:
                    num = int(input("Enter item number to update: "))

                    if num >= 1 and num <= len(cart):

                        item = cart[num - 1]

                        total -= item[3]

    
                        new_choice = input("Enter new plate (h/f): ").lower()

                        if new_choice == 'h':
                            item[2] = "Half"
                            item[3] = self.menu[item[0]]['half']
                        else:
                            item[2] = "Full"
                            item[3] = self.menu[item[0]]['full']

                        
                        total += item[3]

                        print("🔄 Updated:", item[1], "(", item[2], ")")

                    else:
                        print(" Invalid number")

                except:
                    print(" Wrong input")

            else:
                break
    def save_menu(self):
      with open(r"app\database\menu_items.json",'w') as json_file:  
        json.dump(self.menu,json_file,indent=4)

        
""" obj=Menu_Rms()

while True:
        print("-"*32)
        print("=======STAFF MENU - RMS=========")
        print("-"*32)
        print("/" + "1.  View Menu")
        print("/" + "2.  Take Order")
        print("/" + "3.  Update")
        print("/" + "4.  Cancel Order")
        print("/" + "5.  Exit")
        print("-"*32)
        
   
        option=int(input("Select any Option: "))    
    
        if option == 1:
            obj.display_menu()
        elif option == 2:
            obj.select_item()
        elif option == 3:
            obj.update_item()
        elif option == 4:
            obj.cancel_item()
        elif option == 5:
            exit()
        else:
            print("invalid option")  


   


 """
