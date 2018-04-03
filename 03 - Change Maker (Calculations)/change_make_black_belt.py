import random, os, subprocess, platform


class Register(object):

    drawer_count = 500

    negative_ans = ["buy", "quit", "exit", "no", "no thanks", "no thank you", "nope",
                 "that's all", "nah", "nothing", "that's it"]

    ask_if_more = ["What else can I get for you?", "Anything else?", "Do you want more?",
                   "Is there anything else you want to get?", "How about some desert?", "Are you getting anything else?"]

    def __init__(self):

        self.drawer = Drawer()
        self.printer = Printer()

        self.drawer_count = Register.drawer_count

    @staticmethod
    def _tender(total):
        tendered = 0
        while tendered < total:
            tendered = input("How much do you have to pay?\t$")
            tendered = float(tendered)
            if tendered == total:
                print("Thank you, your change is $0.00.")
            elif tendered > total:
                Drawer._make_change(tendered, total)
                pass
            else:
                print("\nYour total is ${0:>5.2f}, and you only gave me ${1:>5.2f}. \n"
                      "You need at least ${2:>5.2f} more. Please try again.\n".format(
                    total, tendered, total-tendered
                ))

    def order(self):
        order_is_done = False
        Menu._print_menu()
        while order_is_done is not True:
            food = input("\nType your order here please:\t").lower()
            if food.lower() == "spam":
                print("No spam!")
                continue
            if food in Register.negative_ans:
                total = Bill._total_order()
                Register._tender(total)
                order_is_done = True
            elif food in Menu._menu.keys():
                Bill._add_item(food)
                print("\n" + random.choice(Register.ask_if_more))
            else:
                print("I'm sorry I don't recognize that. Please check your spelling and try again")
        get_receipt = ""
        while get_receipt == "":
            get_receipt = input("Would you like your receipt?").lower()
            if get_receipt == "no":
                print("Ok have a nice day!")
            elif get_receipt == "yes":
                Printer._print_receipt()


class Menu(object):

    _menu = {"hamburger": 5,
             "soda": 1,
             "fries": 2,
             "ice cream": 2.5,
             "salad": 4,
             "chicken fingers": 3.5,
             "pizza slice": 3}

    @staticmethod
    def _print_menu():
        print("\nHere is our menu, please take your time\n")
        for item in Menu._menu.keys():
            print(item.capitalize()+("." * (25 - len(item))) + "$ {0:>4.2f}".format(Menu._menu[item]))


class Bill(object):

    _sub_total = 0

    @staticmethod
    def _add_item(food):
        menu_food, menu_price = list(Menu._menu.items())[list(Menu._menu.keys()).index(food)]
        Bill._sub_total += float(menu_price)
        bill = open("receipt.txt", 'a')
        bill.write(menu_food.capitalize() + ("." * (20 - len(menu_food))) + "$ {0:>4.2f}\n".format(menu_price))
        bill.close()

    @staticmethod
    def _total_order():
        Bill._total = float(Bill._sub_total) * 1.07
        print("Thank you, your total is ${:>5.2f}".format(Bill._total))
        return Bill._total


class Drawer(object):

    change_types = {"twenties": 2000, "tens": 1000, "fives": 500, "ones": 100,
                    "quarters": 25, "dimes": 10, "nickles": 5, "pennies": 1}

    @staticmethod
    def _make_change(tendered, total):
        change = tendered - total
        change_left = int(round(change * 100))
        print("Here is your change(${:.2f}), in the following denominations:\n".format(change))
        for pair in Drawer.change_types.items():
            denom_type, div_num = pair
            num_of_type = change_left // div_num
            change_left %= div_num
            print(denom_type.capitalize() + ": " + str(int(num_of_type)))
        print("\n")
        Receipt._write_receipt(Bill._sub_total, tendered, change)


class Receipt(object):

    @staticmethod
    def _write_receipt(total, tendered, change):
        with open("receipt.txt", 'r') as receipt:
            itemized = receipt.read()
        with open("receipt.txt", 'w') as receipt:
            receipt.write("\t\tFood Shop\n")
            receipt.write("\n")
            info_line = "Table:\t1\tChk#:\t1111\tGuest:\t1\n"
            receipt.write("-" * 40 + "\n" + info_line + "-" * 40 + "\n")
            receipt.write("\n")
            receipt.write(itemized)
            receipt.write("_" * 35 + "\n")
            subtotal = total
            subtotal_str = (" " * (20 - (len("Sub-total: ")))) + "${:>5.2f}\n".format(subtotal)
            receipt.write("\nSub-total: " + subtotal_str)
            tax = float(total) * .07
            tax_str = (" " * (20 - (len("Tax: ")))) + "${:>5.2f}\n".format(tax)
            receipt.write("Tax: " + tax_str)
            total_str = (" " * (20 - (len("Total: ")))) + "${:>5.2f}\n".format(total + tax)
            receipt.write("Total: " + total_str)
            receipt.write("\n")
            tendered_str = (" " * (20 - (len("Tendered: "))) + "${:>5.2f}\n".format(tendered))
            receipt.write("Tendered: " + tendered_str)
            change_str = (" " * (20 - (len("Change Due: "))) + "${:>5.2f}\n".format(change))
            receipt.write("Change Due: " + change_str)
            receipt.write("\n\nTHANKS FOR DINING WITH US!\nPLEASE COME AGAIN\n")


class Printer(object):

    @staticmethod
    def _print_receipt():
        file="receipt.txt"
        if platform.system() == "Windows":
            os.startfile(file["open"])
        elif platform.system() == "Darwin" or "Linux":
            subprocess.call(["open", file])
        else:
            print("Sorry we were not able to print your receipt:( Try on a Windows or Mac please.")

register1 = Register()
while register1.drawer_count > 0:
    print("\nWelcome to Food Shop! Where you can satisfy all your hunger needs!")
    register1.order()
    break
