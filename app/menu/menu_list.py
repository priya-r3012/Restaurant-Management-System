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
               {"id": 11 , "name": "Chapati (2 pcs)","type": "Lunch" , "half": 30, "full": 60},
        

           
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

    #with open("app\database\menu_items.json",'w') as json_file:
        #json.dump(self.menu,json_file,indent=4)

    def display_menu(self):
        print("\n-------------------------- FULL MENU -------------------------------")
        print("ID\t\tName\t\t\t\tType\t\t\tHalf\t\t\tFull")
        print("-" * 68)


        for item in self.menu:
            print(f"{item['id']}\t\t{item['name']}\t\t\t{item['type']}\t\t\t₹{item['half']}\t\t\t₹{item['full']}")

        print("-" * 68)

    def order_item(self):
        total=0
        while True:
            self.display_menu()

            try:
                item_id=int(input("\nEnter Item ID you want to order: "))
            except:
                print("Invalid input") 
                continue
            plate=input("Half or Full(h/f): ").lower()
            found= False

            for item in self.menu:
                if item["id"] ==item_id:
                    found=True
                    if plate=='h':
                        price=item["half"]
                        plate_type="Half" 
                    elif plate=='f':
                        price=item["full"]
                        plate_type="Full" 
                    else:
                        print("Invalid choice")
                        break
                    
                    print(f"Added: {item['name']} ({plate_type})=₹{price}") 
                    total+=price
                    break

                if not found:
                  print("Item not found")

                more=input("You want to add more items?(y/n): ").lower()
                if more!='y':
                    break
obj=Menu_Rms()
obj.order_item()

