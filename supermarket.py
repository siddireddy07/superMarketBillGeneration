from datetime import datetime

name = input("Enter your name:")

lists = """
Rice     Rs 20/kg
Sugar    Rs 30/kg
Salt     Rs 20/kg
Oil      Rs 80/liter
Maggi    Rs 50/kg
Books    Rs 40/each
Boost    Rs 90/each
Soap     Rs 40/each
"""

totalprice = 0
finalprice = 0


item_list = []

items = {
    'Rice': 20, 'Sugar': 30, 'Salt': 20,
    'Oil': 80, 'Maggi': 50, 'Books': 40, 'Boost': 90,
    'Colgate': 85, 'Soap': 40
}


options = int(input("For a list of items, press 1: "))

if options == 1:
    print(lists)

sno = 0

while True:
    inp1 = int(input("If you want to buy, press 1 or press 2 to exit: "))

    if inp1 == 2:
        print("Thanks for your time")
        break
    elif inp1 == 1:
        item = input("Enter your items: ").capitalize()

        quantity = int(input("Enter quantity: "))
        if item in items.keys():

            price = quantity * items[item]
            sno += 1

            item_list.append((sno, item, quantity, price))
            totalprice += price

            gst = (totalprice * 5) / 100

            finalamount = gst + totalprice
        else:
            print("Sorry, the item you entered is not available")

        inp = input("Can I bill the items? (yes or no): ")

        if inp == "yes":
            if finalamount != 0:
                print(35 * "=", "More Supermarket", 40 * "=")
                print(35 * " ", "visakhapatnam")
                print(name, 55 * " ", "Date:",          datetime.now())
                print(100 * "-")
                print("s.no", 5 * "\t", "items", 6 * "\t", "Quantity", 4* "\t", "Price")
                for sno, item, quantity, price in item_list:
                    print(sno, 6 * "\t", item,7 * "\t", quantity, 5* "\t", price)
                print(100 * "-")
                print(20 * "\t", "Total Amount: ", totalprice)
                print(20 * "\t", "GST: ", gst)
                print(100 * "-")
                print(20 * "\t", "Final Amount: ", finalamount)
                print(100 * "-")
                print(30 * " ", "Thanks for Shopping")
                print(100 * "-")
                print()
        elif inp== "no":
            pass
        else:
            print("You have entered the wrong input")
    else:
        print("Thanks for your time")
        pass