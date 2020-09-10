class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.what_coffee = None
        self.add_water = None
        self.add_milk = None
        self.add_coffee = None
        self.add_cups = None
        self.while_exit = True

    def f_remaining(self):
        print('''The coffee machine has:
%d of water
%d of milk
%d of coffee beans
%d of disposable cups
$%d of money''' % (self.water, self.milk, self.coffee, self.cups, self.money))
        print('')

    def f_buy(self):
        self.what_coffee = input('''What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
> ''')
        if self.what_coffee == '1':
            if self.water >= 250 and self.coffee >= 16 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
                self.money += 4
            else:
                if self.water < 250:
                    print('Sorry, not enough water!')
                elif self.coffee < 16:
                    print('Sorry, not enough coffee!')
                elif self.cups < 1:
                    print('Sorry, not enough cup!')
        elif self.what_coffee == '2':
            if self.water >= 350 and self.milk >= 75 and self.coffee >= 20 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
                self.money += 7
            else:
                if self.water < 350:
                    print('Sorry, not enough water!')
                elif self.milk < 75:
                    print('Sorry, not enough milk!')
                elif self.coffee < 20:
                    print('Sorry, not enough coffee!')
                elif self.cups < 1:
                    print('Sorry, not enough cup!')
        elif self.what_coffee == '3':
            if self.water >= 200 and self.milk >= 100 and self.coffee >= 12 and self.cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
                self.money += 6
            else:
                if self.water < 200:
                    print('Sorry, not enough water!')
                elif self.milk < 100:
                    print('Sorry, not enough milk!')
                elif self.coffee < 12:
                    print('sorry, not enough coffee!')
                elif self.cups < 1:
                    print('Sorry, not enough cup!')
        elif self.what_coffee == 'back':
            return

        print('')

    def f_fill(self):
        self.add_water = input('''Write how many ml of water do you want to add:
> ''')
        self.add_milk = input('''Write how many ml of milk do you want to add:
> ''')
        self.add_coffee = input('''Write how many grams of coffee beans do you want to add:
> ''')
        self.add_cups = input('''Write how many disposable cups of coffee do you want to add:
> ''')
        self.water += int(self.add_water)
        self.milk += int(self.add_milk)
        self.coffee += int(self.add_coffee)
        self.cups += int(self.add_cups)
        print('')

    def f_take(self):
        print('I gave you $' + str(self.money))
        print('')
        self.money -= self.money

    def exit(self):
        self.while_exit = False

    def f_maine(self):
        while self.while_exit:
            action = input('''Write action (buy, fill, take, remaining, exit):
> ''')
            if action == "buy":
                self.f_buy()
            elif action == "fill":
                self.f_fill()
            elif action == "take":
                self.f_take()
            elif action == "remaining":
                self.f_remaining()
            elif action == "exit":
                self.exit()


terminator = CoffeeMachine()
terminator.f_maine()
