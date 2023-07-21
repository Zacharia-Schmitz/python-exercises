#1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    """
    Returns True if the input is equal to the integer 2 or the string 'two', and False otherwise.

    Parameters:
    x (int or str): The input to check.

    Returns:
    bool: True if x is equal to 2 or 'two', and False otherwise.
    """
    # Check if x is equal to the integer 2 or the string 'two'
    if str(x) == '2' or str(x) == 'two':
        # If x is equal to 2 or 'two', return True
        return True
    else:
        # If x is not equal to 2 or 'two', return False
        return False

# Test the is_two function with various inputs
assert is_two(2) == True
assert is_two('two') == True
assert is_two(3) == False
assert is_two('three') == False
assert is_two('2') == True
assert is_two(1) == False
assert is_two('2.0') == False

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    """
    Returns True if the input letter is a vowel (i.e., 'a', 'e', 'i', 'o', or 'u'), and False otherwise.

    Parameters:
    letter (str): The letter to check.

    Returns:
    bool: True if the letter is a vowel, and False otherwise.
    """
    # Check if the letter is in the tuple ('a', 'e', 'i', 'o', 'u')
    if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
        # If the letter is a vowel, return True
        return True
    else:
        # If the letter is not a vowel, return False
        return False


# Test the is_vowel function with various inputs
assert is_vowel('E') == True
assert is_vowel('A') == True
assert is_vowel('a') == True
assert is_vowel('e') == True
assert is_vowel('i') == True
assert is_vowel('o') == True
assert is_vowel('u') == True
assert is_vowel('b') == False
assert is_vowel('c') == False
assert is_vowel('d') == False
assert is_vowel('f') == False
assert is_vowel('') == False

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    """
    Returns True if the input x is a consonant (i.e., a non-vowel letter), and False otherwise.

    Parameters:
    x (str): The letter to check.

    Returns:
    bool: True if x is a consonant, and False otherwise.
    """
    # Check if x is an empty string
    if x == '':
        # If x is an empty string, it is not a consonant, return False
        return False
    # Check if is_vowel(x) is False
    elif is_vowel(x) == False:
        # If x is not a vowel, it is a consonant, return True
        return True
    # Check if is_vowel(x) is True
    elif is_vowel(x) == True:
        # If x is a vowel, it is not a consonant, return False
        return False

# Assertion Test
assert is_vowel('E') == True
assert is_vowel('A') == True
assert is_vowel('a') == True
assert is_vowel('e') == True
assert is_vowel('i') == True
assert is_vowel('o') == True
assert is_vowel('u') == True
assert is_vowel('b') == False
assert is_vowel('c') == False
assert is_vowel('d') == False
assert is_vowel('f') == False
assert is_vowel('') == False
assert is_vowel('0') == False
assert is_vowel('1') == False
assert is_vowel('2') == False

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_if_consonant(firstletter):
    """
    Returns the input string with the first letter capitalized if it is a consonant, and the original string otherwise.

    Parameters:
    firstletter (str): The string to check.

    Returns:
    str: The input string with the first letter capitalized if it is a consonant, and the original string otherwise.
    """
    # Check if the first letter of firstletter is a consonant using the is_consonant function
    if is_consonant(firstletter[0]) == True:
        # If the first letter is a consonant, capitalize it using the capitalize method and return the result
        return firstletter.capitalize()
    else:
        # If the first letter is not a consonant, return the original string
        return firstletter


assert capitalize_if_consonant('apple') == 'apple'
assert capitalize_if_consonant('banana') == 'Banana'

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(bill_total, tip_percent_decimal=0.2):
    """
    Calculates the tip amount based on the tip percentage and bill total.

    Parameters:
    tip_percent_decimal (float): The tip percentage as a decimal (e.g., 0.15 for 15%).
    bill_total (float): The total bill amount.

    Returns:
    float: The tip amount as a float if the input tip percentage is valid, and 'Invalid entry.' otherwise.
    """
    # Check if x is greater than 0 and less than 1
    if tip_percent_decimal > 0 and tip_percent_decimal < 1:
        # If x is a valid percentage, calculate the tip by multiplying x and y and return the result
        return float(tip_percent_decimal * bill_total)
    # Check if x is less than or equal to 0 or greater than or equal to 1
    elif tip_percent_decimal <= 0 or tip_percent_decimal >= 1:
        # If x is not a valid percentage, print an error message
        return ('Invalid entry.')

assert calculate_tip(100, 0.3) == 30
assert calculate_tip(100) == 20
assert calculate_tip(100, 0.4) == 40

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount_percentage):
    """
    Calculates the price after a discount based on the input original price and discount percentage.

    Parameters:
    original_price (float): The original price of the item.
    discount_percentage (float): The discount percentage as a decimal (e.g., 0.15 for 15%).

    Returns:
    float: The price after the discount has been applied.
    """
    # Calculate the discount amount by multiplying the original price by the discount percentage (as a decimal)
    amount_to_discount = original_price * (discount_percentage / 100)
    # Subtract the discount amount from the original amount to get the price after discount
    discounted_price = original_price - amount_to_discount
    # Return the discounted price
    return discounted_price

assert apply_discount(100, 50) == 50
assert apply_discount(100, 15) == 85
assert apply_discount(150, 50) == 75

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(numstring):
    """
    Removes any commas from the input number string and returns the result as a float.

    Parameters:
    numstring (str): The number string to remove commas from.

    Returns:
    float: The input number string with commas removed and converted to a float.
    """
    # Remove any commas from the number string
    numstring = str(numstring).replace(",", "")
    # Convert the number string to a float and return it
    return int(numstring)
    
assert handle_commas('1,234') == 1234
assert handle_commas('10,123') == 10123

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(score):
    """
    Returns the letter grade corresponding to the input score.

    Parameters:
    score (int): The score to convert to a letter grade.

    Returns:
    str: The letter grade corresponding to the input score, or an error message if the input is invalid.
    """
    # Check if score is not a numeric string or if it is outside the range of 1 to 100
    if isinstance(score, int) == False or score < 1 or score > 100:
        # If score is not valid, return an error message
        return 'Please input a number from 1 - 100.'
    # Check if score is within the range for an A+
    elif score <= 100 and score >= 97:
        return(f'{score} is an A+.')
    elif score <= 96 and score >= 93:
        return(f'{score} is an A.')    
    elif score <= 92 and score >= 90:
        return(f'{score} is a A-.')
    elif score <= 89 and score >= 87:
        return(f'{score} is a B+.')
    elif score <= 86 and score >= 83:
        return(f'{score} is a B.')
    elif score <= 82 and score >= 80:
        return(f'{score} is a B-.')
    elif score <= 79 and score >= 77:
        return(f'{score} is a C+.')
    elif score <= 76 and score >= 73:
        return(f'{score} is a C.')
    elif score <= 72 and score >= 70:
        return(f'{score} is a C-.')
    elif score <= 69 and score >= 67:
        return(f'{score} is a D+.')
    elif score <= 66 and score >= 65:
        return(f'{score} is a D.')
    elif score < 65:
        return(f'{score} is an F.')
    
assert get_letter_grade(65) == '65 is a D.'
assert get_letter_grade(75) == '75 is a C.'
assert get_letter_grade(100) == '100 is an A+.'

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    """
    Removes all vowels (both upper and lowercase) from the input string and returns the modified string.

    Parameters:
    string (str): The string to remove vowels from.

    Returns:
    str: The input string with all vowels removed.
    """
    # Define a list of vowels, both upper and lowercase
    vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    # Remove all vowels from the string
    for vowel in vowels:
        string = string.replace(vowel, '')
    # Return the modified string
    return string

assert remove_vowels('Banana') == 'Bnn'
assert remove_vowels('apple') == 'ppl'
assert remove_vowels('Mississippi') == 'Msssspp'

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# Examples: Name -> name, First Name -> first_name, % Completed -> completed
def normalize_name(string):
    """
    Normalizes the input string by removing non-alphanumeric characters, replacing spaces with underscores,
    removing leading/trailing whitespace, and converting to lowercase.

    Parameters:
    string (str): The string to normalize.

    Returns:
    str: The normalized string.
    """
    # Remove any non-alphanumeric characters and replace spaces with underscores
    string = ''.join(e for e in string if e.isalnum() or e == ' ')
    # Remove any leading or trailing whitespace
    string = string.strip()
    # Convert the string to lowercase
    string = string.lower()
    # Replace any internal spaces remaining
    string = string.replace(' ', '_')
    # Return the modified string
    return string

assert normalize_name('AAAaaa%4$$') == 'aaaaaa4'
assert normalize_name('@@##$$123FFggGh') == '123ffgggh'
assert normalize_name('% Completed') == 'completed'

# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(numbers):
    """
    Returns a list that is the cumulative sum of the input list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    list: A list that is the cumulative sum of the input list of numbers.
    """
    # Initialize an empty list to store the cumulative sum
    cumulative = []
    # Initialize a variable to store the running sum
    running_sum = 0
    # cumulative, running_sum = [], 0     # Can also assign multiple variables on one line
    # Iterate over the numbers in the input list
    for number in numbers:
        # Add the current number to the running sum
        running_sum += number
        # Append the running sum to the cumulative list
        cumulative.append(running_sum)
    # Return the cumulative list
    return cumulative

assert cumulative_sum([1, 1, 1]) == [1, 2, 3]
assert cumulative_sum([1, 2, 3, 4]) == [1, 3, 6, 10]

# ADDITIONAL: Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

# BONUS: Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
def twelveto24(time):
    """
    Converts a time string in 12-hour format to 24-hour format.

    Parameters:
    time (str): A time string in 12-hour format (e.g., '10:45am').

    Returns:
    str: The input time string converted to 24-hour format (e.g., '1045').
    """
    # Check if the time is in AM or PM format
    if 'am' in time:
        # Remove the colon and AM indicator from the time string
        time = time.replace(':','')
        time = time.replace('am','')
        # If the time is greater than or equal to 10:00 AM, return it as a string
        if int(time) >= 1000:
            return str(time)
        # If the time is less than 10:00 AM, add a leading zero and return it as a string
        if int(time) < 1000:
            return str(f'0{time}')
    else:
        # Remove the colon and PM indicator from the time string
        if 'pm' in time:
            time = time.replace(':','')
            time = time.replace('pm','')
            # If the time is less than 12:00 PM, add 12 hours and return it as a string
            if int(time) < 1200:
                return str(int(time) + 1200)
            # If the time is greater than or equal to 12:00 PM, return it as a string
            if int(time) >=1200:
                return str(time)
            
assert twelveto24('9:00am') == '0900'
assert twelveto24('10:00am') == '1000'
assert twelveto24('3:00pm') == '1500'

# BONUS: write a function that does the opposite.

def twentyfourto12(miltime):
    milhours = str(miltime)[:2]
    minutes = str(miltime)[2:]
    if int(milhours) > 12:
        hours = int(milhours) - 12
        time = (f'{hours}:{minutes}pm')
    elif int(milhours) < 10:
        hours = str(milhours)[1]
        time = (f'{hours}:{minutes}am')
    elif int(milhours) < 12:
        hours = str(milhours)
        time = (f'{hours}:{minutes}am')
    else:
        time = (f'{milhours}:{minutes}pm')
    return time

assert twentyfourto12(2300) == '11:00pm'
assert twentyfourto12('0900') == '9:00am'
assert twentyfourto12(1000) == '10:00am'

### BONUS: Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.

def col_index(col_name):
    """
    Returns the index number of a spreadsheet column given its name.

    Parameters:
    col_name (str): The name of the column.

    Returns:
    int: The index number of the column.
    """
    col_num = 0
    for i, c in enumerate(col_name[::-1]):
        col_num += (ord(c) - 64) * (26 ** i)
    return col_num - 1

assert col_index("A") == 0
assert col_index("B") == 1
assert col_index("Z") == 25
assert col_index("AA") == 26
assert col_index("AB") == 27
assert col_index("BA") == 52
assert col_index("ZZ") == 701
assert col_index("AAA") == 702
assert col_index("AAB") == 703

print('Ran successfully')