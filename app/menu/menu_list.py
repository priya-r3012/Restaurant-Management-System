class Menu_Rms:

    def __init__(self):
        self.menu.items = {


           "Breakfast": [
               {"id": 1 , "name": "Aloo Paratha", "half": 40, "full": 80},
               {"id": 2 , "name": "Paneer Paratha", "half": 60, "full": 100},
               {"id": 3 , "name": "Poha", "half": 30, "full": 60},
               {"id": 4 , "name": "Upma", "half": 35, "full": 70},
               {"id": 5 , "name": "Tea", "half": 20, "full": 40},
               {"id": 6 , "name": "Dahi", "half": 40, "full": 80}
            ],

           "Lunch": [
               {"id": 7 , "name": "Veg Thali", "half": 120, "full": 200},
               {"id": 8 , "name": "Dal Rice", "half": 80, "full": 150},
               {"id": 9 , "name": "Rajma Rice", "half": 90, "full": 160},
               {"id": 10 , "name": "Paneer Butter Masala", "half": 140, "full": 260},
               {"id": 11 , "name": "Chapati (2 pcs)", "half": 30, "full": 60}
            ],

           "Dinner": [
               {"id": 12 , "name": "Butter Chicken", "half": 180, "full": 320},
               {"id": 13 , "name": "Kadhai Paneer", "half": 150, "full": 280},
               {"id": 14 , "name": "Tandoori Roti", "half": 20, "full": 40},
               {"id": 15 , "name": "Jeera Rice", "half": 80, "full": 140},
               {"id": 16 , "name": "Dal Makhani", "half": 120, "full": 220}
            ],

           "Veg":[
               {"id" : 17 , "name": "Paneer Tikka" , "half": 150, "full": 280},
               {"id" : 18 , "name": "Veg Manchurian" , "half": 120, "full": 220},
               {"id" : 19 , "name": "Spring Roll", "half": 100, "full": 180},
               {"id" : 20 , "name": "Chilli Paneer", "half": 140, "full": 260},
               {"id" : 21 , "name": "Hara Bhara Kabab", "half": 130, "full": 240},
            ],

           "Non-Veg": [
               {"id" : 22 , "name": "Chicken Tikka", "half": 180, "full": 320},
               {"id" : 23 , "name": "Chicken Lollipop", "half": 170, "full": 300},
               {"id" : 24 , "name": "Fish Fry", "half": 200, "full": 350},
               {"id" : 25 , "name": "Mutton Kabab", "half": 220, "full": 380},
               {"id" : 26 , "name": "Chicken","half": 160, "full": 290},
            ],

           "Soups":[
               {"id" : 27 , "name": "Veg Soup" , "half": 80, "full": 140},
               {"id" : 28 , "name": "Tomato Soup","half": 70, "full": 130},
               {"id" : 29 , "name": "Sweet Corn Soup", "half": 90, "full": 150},
               {"id" : 30 , "name": "Chicken Soup", "half": 100, "full": 170},
               {"id" : 31 , "name": "Hot & Sour Soup", "half": 85, "full": 145},
           ],

           "Appetizers":[
               {"id" : 32 , "name": "Masala Papad", "half": 40, "full": 70},
               {"id" : 33 , "name": "French Fries", "half": 90, "full": 150},
               {"id" : 34 , "name": "Cheese Balls", "half": 120, "full": 200},
               {"id" : 35 , "name": "Garlic Bread", "half": 110, "full": 180},
               {"id" : 36 , "name": "Veg Cutlet", "half": 100, "full": 170},
           ],

           "Tea & Coffee":[
               {"id" : 37 , "name": "Cold Coffee" , "half": 90, "full": 150},
               {"id" : 38 , "name": "Hot Coffee", "half": 70, "full": 120},
               {"id" : 39 , "name": "Tea", "half": 30, "full": 50},
               {"id" : 40 , "name": "Green Tea", "half": 40, "full": 60},
               {"id" : 41 , "name": "Lemon Tea", "half": 50, "full": 80},
           ],

           "Shakes & Juice":[
               {"id": 42 , "name": "Banana Shake", "half": 80, "full": 140},
               {"id": 43 , "name": "Chocolate Shake", "half": 100, "full": 160},
               {"id": 44 , "name": "Strawberry Shake", "half": 100, "full": 160},
               {"id": 45 , "name": "Pineapple Juice", "half": 90, "full": 150},
               {"id": 46 , "name": "Orange Juice", "half": 90, "full": 150},
               {"id": 47 , "name": "Apple Juice", "half": 100, "full": 160},
               {"id": 48 , "name": "Watermelon Juice", "half": 80, "full": 140},
               {"id": 49 , "name": "Grapes Juice", "half": 90, "full": 150},
               {"id": 50 , "name": "Butter Milk", "half": 50, "full": 80},
               {"id": 51 , "name": "Lassi", "half": 70, "full": 120},
               {"id": 52 , "name": "Mango Shake", "half": 90, "full": 150}
           ],
    
           "Cold Drink":[
               {"id" : 53 , "name": "Coke", "half": 40, "full": 70},
               {"id" : 54 , "name": "Pepsi", "half": 40, "full": 70},
               {"id" : 55 , "name": "Sprite", "half": 40, "full": 70},
               {"id" : 56 , "name": "Fanta", "half": 40, "full": 70},
               {"id" : 57 , "name": "Thumbs Up", "half": 40, "full": 70},
               {"id" : 58 , "name": "Mineral Water", "half": 20, "full": 30},
               {"id" : 59 , "name": "Fresh Lime Soda", "half": 60, "full": 100},
           ],

           "Dessert":[
               {"id" : 60 , "name": "Ice Cream Vanilla", "half": 60, "full": 100},
               {"id" : 61 , "name": "Ice Cream Chocolate", "half": 70, "full": 110},
               {"id" : 62 , "name": "Gulab Jamun", "half": 50, "full": 90},
               {"id" : 63 , "name": "Rasgulla", "half": 50, "full": 90},
               {"id" : 64 , "name": "Brownie", "half": 90, "full": 150},
               {"id" : 65 , "name": "Falooda", "half": 100, "full": 160},
               {"id" : 66 , "name": "Kulfi", "half": 60, "full": 100}
           ],

           "Raita":[
               {"id" : 67 , "name": "Boondi Raita" , "half": 50, "full": 100},
               {"id" : 68 , "name": "Boondi Raita" , "half": 50, "full": 100},
               {"id" : 69 , "name": "Boondi Raita" , "half": 50, "full": 100},
           ],

           "Special Thali":[
               {
                   "id": 70,
                   "name": "Special Thali",
                   "items":[
                       "Shahi Paneer",
                       "Dal Tadka",
                       "Mix Veg",
                       "Naan",
                       "Rice",
                       "Salad",
                       "Raita",
                       "Gulab Jamun"
                   ],
                   "price": 200
               }
               
           ]


        }

    def display_menu(self):
        print("\n------ FULL MENU ------")
        print("ID\tName\tHalf\tFull")
        print("-" * 50)

        for id, item in self.menu.items():
            print(f"{id}\t{item['name']}\t₹{item['half']}\t₹{item['full']}")

        print("-" * 50)

    def order_item(self):
        self.display_menu()

        item_id = int(input("Enter Item ID: "))
        plate = input("Half or Full (h/f): ")

        if item_id in self.menu:
            item = self.menu[item_id]

            if plate.lower() == 'h':
                price = item['half']
                plate_type = "Half"
            else:
                price = item['full']
                plate_type = "Full"

            print(f"\n {item['name']} - ₹{price}")
        else:
            print("Invalid item!")

obj=Menu_Rms()
obj.display_menu()
obj.order_item()
