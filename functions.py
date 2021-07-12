
def is_two(x):
    """
    Return True if the passed input is either the number
        or the string 2, False otherwise.
    Args: str
    Output: bool
    """
    return True if int(x)==2 else False

def is_vowel(x):
    """
    Return True if the passed string is a vowel,
    False otherwise.
    Args: str
    Output: bool
    """
    return True if x.lower() in [c for c in 'aeiou'] else False


def is_cons(x):
    """
    Return True if the passed string is a consonant,
    False otherwise.
    Args: str
    Output: bool
    """
    return True if x.lower() in [c for c in 'qwrtypsdfghjklzxcvbnm'] else False

def capital_cons(x):
    """
    Capitalize the first letter of the word if the word
    starts with a consonant.
    Args: str
    Output: str
    """
    return x.capitalize() if is_cons(x[0]) else x

def calc_tip(tip, bill):
    """
    Accept a tip percentage between 0 and 1 and the
    bill total, and return the amount to tip.
    Args: float, float
    Output: float
    """
    return tip*bill

def discount(discount, price):
    """
    Accept a original price, and a discount percentage,
    and return the price after the discount is applied.
    Args: float, float
    Output: float
    """
    return price*(1-discount)

    '''Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
    Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
    Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
    Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
        anything that is not a valid python identifier should be removed
        leading and trailing whitespace should be removed
        everything should be lowercase
        spaces should be replaced with underscores
        for example:
            Name will become name
            First Name will become first_name
            % Completed will become completed
    Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
        cumulative_sum([1, 1, 1]) returns [1, 2, 3]
        cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
    '''

if __name__ == "__main__":
    print(is_two('2'))
    print(is_vowel('a'))
    print(is_vowel('L'))
    print(is_cons('L'))
    print(capital_cons('library'))
    print(capital_cons('apple'))
    print(calc_tip(.15,565.))
    print(discount(.15,565.))








