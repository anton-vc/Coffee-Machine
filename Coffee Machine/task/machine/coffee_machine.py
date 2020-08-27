class CoffeeMachine():
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money
        
    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print("$" + str(self.money), "of money")
        
    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups += int(input())
        
    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0
        
    def make_coffee(self, w, mi, c, mo):
        if self.water < w:
            print("Sorry, not enough water!")
        elif self.milk < mi:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < c:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= w
            self.milk -= mi
            self.coffee_beans -= c
            self.disposable_cups -= 1
            self.money += mo
            
    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_type = input()
        if coffee_type == "1":
            self.make_coffee(250, 0, 16, 4)
        elif coffee_type == "2":
            self.make_coffee(350, 75, 20, 7)
        elif coffee_type == "3":
            self.make_coffee(200, 100, 12, 6)
        elif coffee_type == "back":
            pass
        else:
            print("Invalid input")
            
    def execute(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            print("")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                break
            else:
                print("Invalid action")
            print("")

my_coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
my_coffee_machine.execute()
