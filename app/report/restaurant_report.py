import datetime
import json



class Order_complete_weekly:
  def weekly_report(self):
    try:
        with open(r"app/database/app/database/sale_report_weekly.json", "r") as file:
            data = json.load(file)
    except:
        print("No sales data found")
        return

    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)

    total = 0
    count = 0
    daily = {}

    for sale in data:
        sale_date = datetime.datetime.strptime(sale["date"], "%Y-%m-%d").date()

        if sale_date >= week_ago:
            total += sale["amount"]
            count += 1

            day = sale_date.strftime("%A")
            daily[day] = daily.get(day, 0) + sale["amount"]

    print("\n WEEKLY REPORT")
    print("-"*40)
    print(f"Total Orders: {count}")
    print(f"Total Sales: ₹{total}")
    print("-"*40)


  def save_sale(self, total_amount):
    try:
        with open("app/database/app/database/sale_report_weekly.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    sale = {
        "date": str(datetime.date.today()),
        "amount": total_amount
    }

    data.append(sale)

    with open("app/database/app/database/sale_report_weekly.json", "w") as file:
        json.dump(data, file, indent=4)    