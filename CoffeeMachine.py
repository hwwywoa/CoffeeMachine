class CoffeeMachine:
    coffee_type = None  # coffee type to be selected
    coffee_requirements = []
    status = "idle"
    espresso_requirements = [250, 0, 16, 1, 4]  # requirements [water, milk, coffee beans, disposable cups, price]
    latte_requirements = [375, 75, 20, 1, 7]
    cappuccino_requirements = [200, 100, 12, 1, 6]

    def __init__(self, water, milk, coffee_beans, d_cups, money):  # for initial supply values
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.d_cups = d_cups
        self.money = money

    def select_coffee(self):  # set coffee requirements for selected coffee type
        if self.coffee_type == "1":
            self.coffee_requirements = self.espresso_requirements
        elif self.coffee_type == "2":
            self.coffee_requirements = self.latte_requirements
        elif self.coffee_type == "3":
            self.coffee_requirements = self.cappuccino_requirements

    def supply_check(self):  # check if it is enough supplies for coffee
        if self.water < self.coffee_requirements[0]:
            print("Sorry, not enough water!")
            self.status = "idle"
        elif self.milk < self.coffee_requirements[1]:
            print("Sorry, not enough milk!")
            self.status = "idle"
        elif self.coffee_beans < self.coffee_requirements[2]:
            print("Sorry, not enough coffee beans!")
            self.status = "idle"
        elif self.d_cups < self.coffee_requirements[3]:
            print("Sorry, not enough disposable cups!")
            self.status = "idle"
        else:
            self.status = "ready!"

    def make_coffee(self):  # making coffee. supplies reduced
        self.water -= self.coffee_requirements[0]
        self.milk -= self.coffee_requirements[1]
        self.coffee_beans -= self.coffee_requirements[2]
        self.d_cups -= self.coffee_requirements[3]
        self.money += self.coffee_requirements[4]
        print("I have enough resources, making you a coffee!")

    def fill(self):  # refilling supplies
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee_beans += int(input("Write how many g of coffee beans do you want to add:"))
        self.d_cups += int(input("Write how many disposable cups do you want to add: "))

    def take(self):  # money withdraw
        print(f"I gave you ${self.money}")
        self.money = 0

    def remaining(self):  # show remaining supplies
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.d_cups} of disposable cups")
        print(f"{self.money} of money")


start = CoffeeMachine(400, 540, 120, 9, 550)  # creating instance with initial supply values
request = ""
while request != "exit":
    request = input("Write action (buy, fill, take, remaining, exit):")
    if request == "buy":
        start.coffee_type = input("What do you want to buy? 1 - espresso, 2- latte, 3 - cappuccino, back - to main menu:")
        if start.coffee_type == "back":
            continue
        start.select_coffee()
        start.supply_check()
        if start.status == "ready!":
            start.make_coffee()
    elif request == "fill":
        start.fill()
    elif request == "take":
        start.take()
    elif request == "remaining":
        start.remaining()
