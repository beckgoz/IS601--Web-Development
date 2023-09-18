import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException, InvalidPaymentException
#this is an example test showing how to cascade fixtures to build up state
@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm
# add required test cases below
def test_1(machine):
    with pytest.raises(InvalidStageException):
        machine.reset()
        machine.handle_toppings("mayo")
        machine.handle_patty("beef")
        machine.handle_bun("no bun")
        """bag27:3/20/2023
        Test 1 is looking for an InvalidStageException
        when a topping is chosen before a bun. This test
        tries to add a topping before the bun, and passes
        when an InvalidStageException is thrown."""

def test_2(machine):
    with pytest.raises(OutOfStockException):
        machine.reset()
        machine.patties[2].quantity = 1 #setting beef patty quantity to 1
        machine.handle_bun("no bun")
        machine.handle_patty("beef")
        machine.handle_patty("beef") #2nd beef patty, should throw outofstockexception
        """bag27:3/20/2023
        Test 2 ensures patties can only be addes if in stock. When a patty is 
        chosen that is out of stock, and outofstock exception is thrown. This
        test asserts true when that exception is thrown, ensuring that an 
        error will occur when a user tries to add a patty that is out of stock.
        I set the beef patty quantity to 1 for this test to reduce the amount
        of redundant code required to get a patty from quantity 10 to 0."""

def test_3(machine):
    with pytest.raises(OutOfStockException):
        machine.reset()
        machine.toppings[0].quantity = 1 #setting lettuce quantity to 1
        machine.handle_bun("no bun")
        machine.handle_patty("next")
        machine.handle_toppings("lettuce")
        machine.handle_toppings("lettuce")
        """bag27:3/20/2023
        Similar to test 2, test 3 ensures a topping can be added only if
        it is in stock. Using the same logic as test 2, this test asserts 
        true if an outofstockexception is thrown, ensuring users can only
        select in stock toppings. I also changed the lettuce topping quantity
        to 1 for the same reason as before."""

def test_4_all_3_patties(machine):
    machine.reset()
    machine.patties[2].quantity = 10
    machine.toppings[0].quantity = 10
    machine.handle_bun("no bun")
    machine.handle_patty("beef")
    machine.handle_patty("turkey")
    machine.handle_patty("veggie")
    if(machine.inprogress_burger[1].name.lower() == "beef") and (machine.inprogress_burger[2].name.lower() == "turkey") and (machine.inprogress_burger[3].name.lower() == "veggie"):
        assert True
    else:
        assert False
    """bag27:3/20/2023
    Test 4 tests that a burger can be made with 3 unique patties. This case creates a burger with 3 different patties, and ensures that they are all different
    and a part of the inprogress_burger using an if statement. If the if statement passes, the test asserts true and a burger can be made with 3 different
    patties."""

def test_4_over_3_patties(machine):
    with pytest.raises(ExceededRemainingChoicesException):
        machine.reset()
        machine.handle_bun("no bun")
        machine.handle_patty("beef")
        machine.handle_patty("turkey")
        machine.handle_patty("veggie")
        machine.handle_patty("beef")
    """bag27:3/20/2023
    The second part of test 4 ensures that a burger can only
    have 3 patties a time. If a user adds more than 3 patties,
    an exceededremainingchoicesexception is thrown. This test
    tries to add more than three patties and asserts true when 
    an exceededremainingchoicesexception is thrown, ensuring
    that the user can only add up to 3 patties."""

def test_5_all_3_toppings(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("mayo")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("lettuce")
    if(machine.inprogress_burger[2].name.lower() == "mayo") and (machine.inprogress_burger[3].name.lower() == "ketchup") and (machine.inprogress_burger[4].name.lower() == "lettuce"):
        assert True
    else:
        assert False
    """bag27:3/20/2023
    Similar to test 4, test 5 tests that a burger can be made with 3 unique toppingd. This case creates a burger with 3 different toppings, and ensures that 
    they are all different and a part of the inprogress_burger using an if statement. If the if statement passes, the test asserts true and a burger can be 
    made with 3 different toppings."""

def test_5_over_3_toppings(machine):
    with pytest.raises(ExceededRemainingChoicesException):
        machine.reset()
        machine.handle_bun("no bun")
        machine.handle_patty("beef")
        machine.handle_patty("next")
        machine.handle_toppings("mayo")
        machine.handle_toppings("ketchup")
        machine.handle_toppings("mustard")
        machine.handle_toppings("lettuce")
    """bag27:3/20/2023
    The second part of test 5 ensures that a burger can only
    have 3 toppings a time. If a user adds more than 3 toppings,
    an exceededremainingchoicesexception is thrown. This test
    tries to add more than three toppings and asserts true when 
    an exceededremainingchoicesexception is thrown, ensuring
    that the user can only add up to 3 toppings."""

def test_6(machine):
    try:
        machine.reset
        machine.handle_bun("lettuce wrap")
        machine.handle_patty("beef")
        machine.handle_patty("next")
        machine.handle_toppings("ketchup")
        machine.handle_toppings("mustard")
        machine.handle_toppings("done")
        machine.handle_pay(2.50, "2.50")

        machine.reset
        machine.handle_bun("white burger bun")
        machine.handle_patty("veggie")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("cheese")
        machine.handle_toppings("mayo")
        machine.handle_toppings("done")
        machine.handle_pay(3.50, "3.50")

        machine.reset
        machine.handle_bun("wheat burger bun")
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("tomato")
        machine.handle_toppings("lettuce")
        machine.handle_toppings("pickles")
        machine.handle_toppings("done")
        machine.handle_pay(3.00, "3.00")
    except InvalidPaymentException:
        assert False
    """bag27:3/20/2023
    Test 7 ensures that the machine properly
    calculates the correct cost for each burger
    based on the given costs. I added up the cost
    for 3 different burgers, and using the handle_pay
    method, I made sure the machine calculated
    the same correct cost. When the input payment
    (my calculated cost in correect format) is different from 
    the machine calculated cost, an invalidpaymentexception
    is thrown. This test asserts False if such exception
    is thrown, ensuring the accuracy of the machine's
    cost calculation"""

def test_7(machine):
    machine.reset
    machine.total_sales = 0
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("mustard")
    machine.handle_toppings("done")
    machine.handle_pay(2.50, "2.50")

    machine.reset
    machine.handle_bun("white burger bun")
    machine.handle_patty("veggie")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    machine.handle_pay(3.50, "3.50")

    machine.reset
    machine.handle_bun("wheat burger bun")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("tomato")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    machine.handle_pay(3.00, "3.00")
    if machine.total_sales == 9.0:
        assert True
    else:
        assert False
    """bag27:3/20/2023
    Test 7 tests the machines ability to keep track
    of the machine's total sales. To test this,
    I created 3 different burgers and added up their cost.
    I then compared it to the machine's total_sales variable.
    If they are the same, the test asserts true and the 
    machine correctly keeps track of total sales."""

def test_8(machine):
    machine.reset
    machine.total_burgers = 0
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("mustard")
    machine.handle_toppings("done")
    machine.handle_pay(2.50, "2.50")

    machine.reset
    machine.handle_bun("white burger bun")
    machine.handle_patty("veggie")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    machine.handle_pay(3.50, "3.50")

    machine.reset
    machine.handle_bun("wheat burger bun")
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("tomato")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    machine.handle_pay(3.00, "3.00")
    if machine.total_burgers == 3:
        assert True
    else:
        assert False
    """bag27:3/20/2023
    Test 8 tests the machines ability to keep track
    of the machine's total burger creations. To test this,
    I created 3 different burgers and compared 3 to the machines
    total_burger variable. If the variable does not equal 3, the 
    machine is not capabel of keeping track of the total number 
    of burgers created and the test asserts false."""
