from data import MENU
import lib


def run():
    choice = input("What would you like? (espresso, latte, cappuccino) ☕: ").lower()

    if choice == "off":
        exit()
    elif choice == "report":
        lib.report(True)
        run()
    elif choice in MENU:
        if not lib.check_resources(choice):
            print("Sorry there's not enough resources to make that drink")
            exit()
        
        inserted = lib.process_coins(lib.insert_coins())
        if not lib.process_purchase(inserted, choice):
            run()
        
        lib.make_drink(choice)
        run()
    else:
        print("Sorry. I don't have that drink.")
        run()

run()
        
