from enum import Enum
import sys
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from BurgerMachineExceptions import InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0
    def __repr__(self) -> str:
        return self.name

class Bun(Usable):
    pass

class Patty(Usable):
    pass

class Topping(Usable):
    pass

class STAGE(Enum):
    Bun = 1
    Patty = 2
    Toppings = 3
    Pay = 4

class BurgerMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 15
    MAX_PATTIES = 3
    MAX_TOPPINGS = 3


    buns = [Bun(name="No Bun", cost=0), Bun(name="White Burger Bun", cost=1), Bun("Wheat Burger Bun", cost=1.25),Bun("Lettuce Wrap", cost=1.5)]
    patties = [Patty(name="Turkey", quantity=10, cost=1), Patty(name="Veggie", quantity=10, cost=1), Patty(name="Beef", quantity=10, cost=1)]
    toppings = [Topping(name="Lettuce", quantity=10, cost=.25), Topping(name="Tomato", quantity=10, cost=.25), Topping(name="Pickles", quantity=10, cost=.25), \
    Topping(name="Cheese", quantity=10, cost=.25), Topping(name="Ketchup", quantity=10, cost=.25),
    Topping(name="Mayo", quantity=10, cost=.25), Topping(name="Mustard", quantity=10, cost=.25),Topping(name="BBQ", quantity=10, cost=.25)] 


    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_patties = MAX_PATTIES
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_burgers = 0

    inprogress_burger = []
    currently_selecting = STAGE.Bun

    # rules
    # 1 - bun must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - patties can't exceed max
    # 4 - toppings can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more burgers can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_burgers should increment properly after a payment
    

    def pick_bun(self, choice):
        if self.currently_selecting != STAGE.Bun:
            raise InvalidStageException
        for c in self.buns:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_burger.append(c)
                return
        raise InvalidChoiceException

    def pick_patty(self, choice):
        if self.currently_selecting != STAGE.Patty:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_patties <= 0:
            raise ExceededRemainingChoicesException
        for f in self.patties:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_burger.append(f)
                self.remaining_patties -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_toppings(self, choice):
        if self.currently_selecting != STAGE.Toppings:
            raise InvalidStageException
        if self.remaining_toppings <= 0:
            raise ExceededRemainingChoicesException
        for t in self.toppings:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_burger.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        self.remaining_patties = self.MAX_PATTIES
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_burger = []
        self.currently_selecting = STAGE.Bun

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_bun(self, bun):
        self.pick_bun(bun)
        self.currently_selecting = STAGE.Patty

    def handle_patty(self, patty):
        if patty == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_patty(patty)

    def handle_toppings(self, toppings):
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == "{:.2f}".format(expected):
            print("Thank you! Enjoy your burger!")
            self.total_burgers += 1
            self.total_sales += expected # only if successful
            print(f"Total sales so far ${self.total_sales:.2f}")
            self.reset()
        else:
            raise InvalidPaymentException
        
    def print_current_burger(self):
        print(f"Current Burger: {','.join([x.name for x in self.inprogress_burger])}")

    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_burger
        cost = 0
        for i in range(len(self.inprogress_burger)):
            temp = self.inprogress_burger[i].cost * 100
            cost = cost + temp
        return cost/100
    """bag27:3/16/2023  To calculate cost, a for loop iterates through the inprogress_burger list
    and retrieves the cost for every item chosen and stores it in a temp int. the temp int
    is added to the cost int which represents the total cost of the burger. the temp cost
    is multiplied by 100 to avoid any float operation errors. the total cost is divided by 100
    at the end to show the cost in dollar format."""

    def run(self):
        try:
            if self.currently_selecting == STAGE.Bun:
                bun = input(f"What type of bun would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.buns))))}?\n")
                self.handle_bun(bun)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Patty:
                patty = input(f"Would type of patty would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.patties))))}? Or type next.\n")
                self.handle_patty(patty)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Toppings:
                toppings = input(f"What topping would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                self.handle_toppings(toppings)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                # show expected value as currency format
                # require total to be entered as currency format
                total = input(f"Your total is ${expected:.2f}, please enter the exact value.\n")
                self.handle_pay(expected, total)
                #bag27:3/16/2023    format of output to show dollar value
                
                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    #exit() in recursive functions creates stackoverflow
                    # use return 1 to exit
                    print("Quitting the burger machine")
                    return 1
        except KeyboardInterrupt:
            # quit
            print("Quitting the burger machine")
            sys.exit()
        # handle OutOfStockException
            # show an appropriate message of what stage/category was out of stock
        except OutOfStockException:
            if self.currently_selecting == STAGE.Bun:
                print(f'The item you selected for BUN is out of stock, please select a different option.')
            elif self.currently_selecting == STAGE.Patty:
                print(f'The item you selected for PATTY is out of stock, please select a different option.')
            elif self.currently_selecting == STAGE.Toppings:
                print(f'The item you selected for TOPPINGS is out of stock, please select a different option.')
            pass
            """bag27:3/20/2023
            The outofstockexception is thrown when the user asks for an item that is out of stock.
            The exception handler determines which stage the user is in, and provides an error
            message informing the user that the item they have chosen for that stage is out of stock.
            The user is then allowed to select a different option"""
        # handle NeedsCleaningException
            # prompt user to type "clean" to trigger clean_machine()
            # any other input is ignored
            # print a message whether or not the machine was cleaned
        except NeedsCleaningException:
            while True:
                clean = input('Machine is dirty. Type \'clean\' to clean the machine (All lowercase). \n')
                if clean == "clean":
                    self.clean_machine();
                    print(f'Machine has been cleaned.')
                    break
                else:
                    print('Machine is dirty.')
            pass
            """bag27:3/20/2023
            The needscleaningexception is thrown when the machine runs out of uses. It temporarily
            breaks the program and prompts the user to input 'clean' in order to clean the machine.
            The while loop will ask the user for input until it gives the correct input and cleans the machine,
            at which point the user can resume their order"""
        # handle InvalidChoiceException
            # show an appropriate message of what stage/category was the invalid choice was in
        except InvalidChoiceException:
            if self.currently_selecting == STAGE.Bun:
                print(f'You have chosen an invalid selection for BUN, please select a different option.')
            elif self.currently_selecting == STAGE.Patty:
                print(f'You have chosen an invalid selection for PATTY, please select a different option.')
            elif self.currently_selecting == STAGE.Toppings:
                print(f'You have chosen an invalid selection for TOPPINGS, please select a different option.')
            pass
            """bag27:3/20/2023
            The invalidchoiceexception is thrown when the user selects an invalid choice for the stage
            they are at. The handler gives them a message informing them that they have chosen an invalid
            option, and gives them a chance to select a valid option."""
        # handle ExceededRemainingChoicesException
            # show an appropriate message of which stage/category was exceeded
            # move to the next stage/category
        except ExceededRemainingChoicesException:
            if self.currently_selecting == STAGE.Bun:
                print(f'You have exceeded the amount of choices for BUN, moving on.')
                self.currently_selecting = STAGE.Patty
            elif self.currently_selecting == STAGE.Patty:
                print(f'You have exceeded the amount of choices for PATTY, moving on.')
                self.currently_selecting = STAGE.Toppings
            elif self.currently_selecting == STAGE.Toppings:
                print(f'You have exceeded the amount of choices for TOPPINGS, moving on.')
                self.currently_selecting = STAGE.Pay
            pass
            """bag27:3/20/2023
            The exceededremainingchoicesexception is thrown when the user inputs too many
            choices for the stage they are on. It informs them that they have chosen
            too many options and automatically moves onto the next stage."""
        # handle InvalidPaymentException
            # show an appropriate message
        except InvalidPaymentException:
            print(f'You have input an invalid payment, please pay the exact amount shown (exclude dollar sign).')
            pass
            """bag27:3/20/2023
            The invalidpaymentexception is thrown when the user inputs a payment that is 
            no exactly the same as the amount displayed, excluding the dollar sign. The program
            asks for input until the correct amount is input."""
        except:
            # this is a default catch all, follow the steps above
            print("Something went wrong")
        
        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    bm = BurgerMachine()
    bm.start()