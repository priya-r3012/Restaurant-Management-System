from app.menu.menu_list import Menu_Rms

class Bill:
 
    def __init__(self,cart):
        self.cart=cart
     

    def generate_bill(self):
        

        print("\n------ BILL ------")
        total = 0

        for item in self.cart:
            print(f"{item['name']} ({item['plate']}) - ₹{item['price']}")
            total += item["price"]

        gst = total * 0.05  
        final_total = total + gst

        print("-" * 30)
        print(f"Subtotal: ₹{total}")
        print(f"GST (5%): ₹{gst:.2f}")
        print(f"Total Bill: ₹{final_total:.2f}")
        print("------------------")
