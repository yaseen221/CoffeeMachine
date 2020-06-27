class CoffeeMachine():
    
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.ui_method()

    def ui_method(self):
        print("Write action (buy, fill, take, remaining, exit):")
        choice = input()
        self.process_method(choice)

    def process_method(self, choice):
        if choice == "buy":
            self.buy()
        elif choice == "fill":
            self.fill()
        elif choice == "take":
            self.take()
        elif choice == "remaining":
            self.remaining()
        elif choice == "exit":
            exit()

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.ui_method()

    def take(self):
        print(f"I gave you ${self.money} \n")
        self.money = 0
        self.ui_method()

    def buy(self):
        cof = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        def espresso():
            if self.water < 250:
                print("\nSorry, not enough water!")
            elif self.beans < 16:
                print("\nSorry, not enough beans!")
            elif self.cups < 1:
                print("\nSorry, not enough cups!")
            else:
                print("\nI have enough resources, making you a coffee!")

                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
            self.ui_method()

        def latte():
            if self.water < 350:
                print("Sorry, not enough water!\n")
            elif self.beans < 20:
                print("Sorry, not enough beans!\n")
            elif self.cups < 1:
                print("Sorry, not enough cups!\n")
            elif self.milk < 75:
                print("Sorry, not enough milk!\n")
            else:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 350
                self.beans -= 20
                self.money += 7
                self.milk -= 75
                self.cups -= 1
            self.ui_method()

        def cappuccino():
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.beans < 12:
                print("Sorry, not enough beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            else:
                print("I have enough resources, making you a coffee!\n")
                self.water -= 200
                self.beans -= 12
                self.money += 6
                self.milk -= 100
                self.cups -= 1
            self.ui_method()

        if cof == "back":
            self.ui_method()
        elif cof == "1":
            espresso()

        elif cof == "2":
            latte()

        elif cof == "3":
            cappuccino()

    def remaining(self):
        print(f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of beans
{self.cups} of disposable cups
${self.money} of money
""")
        self.ui_method()


coffee = CoffeeMachine()
coffee.__init__()
