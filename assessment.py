"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def is_hometown(town_name):
    """Takes the name of a town as a string and determines if the town is my
    hometown.
    """
    return town_name == "Indianapolis"

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def get_full_name(first_name, last_name):
    """Takes a first name and last name as arguments, and concatenates them with
    a space to return a full name.
    """
    return first_name + " " + last_name

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.


def greet_informedly(home_town, first_name, last_name):
    """Takes the name of a home town, a first name, and a last name as arguments
    and calls the functions get_full_name() and is_hometown(). Prints "Hi, 'full
    name here' we're from the same place!" if is_hometown() evaluates to `True`.
    Prints "Hi 'full name here', where are you from?" if not.
    """
    full_name = get_full_name(first_name, last_name)
    if is_hometown(home_town) is True:
        print "Hi, {}, we're from the same place!".format(full_name)
    else:
        print "Hi, {}, where are you from?".format(full_name)


###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""
    fruits_list = ["strawberry", "cherry", "blackberry"]
    return fruit in fruits_list

# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.


def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""
    berry_status = is_berry(fruit)
    if berry_status is True:
        return 0
    elif berry_status is False:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.


def append_to_list(nums_list, new_last_num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""
    nums_list.append(int(new_last_num))
    return nums_list

# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.


def calculate_price(base_price, state_abbrev, percent_tax='.05'):
    """When provided with an item's price, the state where it's being purchased,
    and (optionally) the state's sales tax (as a two-digit decimal), returns
    the total cost including price, taxes, and any state-specific fees.
    """
    price_before_fees = base_price + base_price * float(percent_tax)

    if state_abbrev == 'CA':
        fees = .03 * price_before_fees
    elif state_abbrev == 'PA':
        fees = 2
    elif state_abbrev == 'MA':
        if base_price < 100:
            fees = 1
        else:
            fees = 3
    elif len(state_abbrev) > 2 or not state_abbrev.isalpha():
        print "You must enter a two-digit abbreviation for your state."
        return
    else:
        fees = 0

    total_price = price_before_fees + fees

    return total_price


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.

# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def add_to_list(your_list, *add_ons):
    """Takes a list and any number of additional arguments and returns the list
    with the arguments as new items added sequentially to the end of the list.
    """
    for add_on in add_ons:
        your_list.append(add_on)
    return your_list

# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.


def make_three(word):
    """Takes a word, passes the word through three_words(), and returns the
    word along with the word repeated three times in a row.
    """

    def multiply_by_three(your_word):
        return your_word * 3

    three_words = multiply_by_three(word)
    print word + ', ' + three_words

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
