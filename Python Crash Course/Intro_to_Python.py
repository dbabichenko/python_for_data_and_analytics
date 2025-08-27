import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Introduction

    * Why do we care about Python?
    * Introspection (what is this thing in my code?)
    * Everything is an Objective
    * Scaler Types in Python
    * Control flow
    * Data structures - lists, dictionaries
    * Functions
    * Working with text files
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Why do we care about Python?

    **Federalist papers**

    Alexander Hamilton, James Madison, or John Jay?  For more than 150 years, historians argued over the authorship of the 12 essays in _The Federalist Papers_. It wasn't until 1963 that the mystery was solved by Frederick Mosteller of Harvard University and David Wallace of the University of Chicago. [Nabokov's Favorite Word Is _Mauve_ by Ben Blatt]

    Full text of _The Federalist Papers_ is available at http://www.gutenberg.org/ebooks/1404
    """
    )
    return


@app.cell
def _():
    # Path to our data file (source file)
    source_file_name = 'federalist_papers.txt'

    fed_papers_file = open(source_file_name, 'r')


    # We can read all text at once
    all_text = fed_papers_file.read()
    #print(all_text)
    return (all_text,)


@app.cell
def _(all_text):
    # There are a couple of ways we could find frequencies of the words "while" and "whilst".  
    # For now, let's convert our chunk of text into a list of words

    word_list = all_text.split(" ")
    return


@app.cell
def _(all_text):
    punctuation_marks = ['!', '.', ',', ':', ';', '?', '-', '\n']
    for pm in punctuation_marks:
        all_text_1 = all_text.replace(pm, ' ')
    return (all_text_1,)


@app.cell
def _(all_text_1):
    all_text_2 = all_text_1.lower()
    word_list_1 = all_text_2.split(' ')
    return (word_list_1,)


@app.cell
def _(word_list_1):
    freq_while = 0
    freq_whilst = 0
    for word in word_list_1:
        if word == 'while':
            freq_while = freq_while + 1
        if word == 'whilst':
            freq_whilst = freq_whilst + 1
    print("The frequency of 'while' is: " + str(freq_while))
    print("The frequency of 'whilst' is: " + str(freq_whilst))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Question: Why do we care about the frequency of words in text? What can we do with it?""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Introspection
    In IPython or Jupyter Notebook
    Using a question mark (?) before or after a variable will display some general information about the object.
    """
    )
    return


app._unparsable_cell(
    r"""
    b = [1,2,3]
    dir(b)
    b?
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Everything is an Object
    An important characteristic of Python is its *object model*.

    Every number, string, data structure, function, class, module, and so on in Python is an Object. Each Python object has an associated type (i.e. *integer*, *string*, or *function*) and internal data.

    In practice, this makes the language very flexible. Even functions can be treated like any other object.
    """
    )
    return


@app.cell
def _():
    print("Hellow World!") # Print() is a very useful build-in function in Python
    print(print.__doc__) # But it's also an object, and it has a docstring (documentation string)
    print()
    print(print, 'is an object of type', type(print))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Each Python object exists in the Python interpreter in its own "box". When assigning a variable or name in Python, we are actually creating a *reference* to the object shown on the righthand side of the equal sign. We can call the lefthand side as *variable name*""")
    return


@app.cell
def _():
    a = [1,2,3] # This means the list [1,2,3] is assigned to the variable a; It's different from the mathematical equation.
    b = a # We can create a new variable b and assign it to the same object as a, not the value of a.
    print(a, b)
    a.append(4) # We can change the object a is pointing to, and b will also be changed.
    print(" var a is", a, "\n var b is", b)
    return


@app.cell
def _():
    a_1 = [1, 2, 3]
    b_1 = a_1.copy()
    a_1.append(4)
    print(' var a is', a_1, '\n var b is', b_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    When we pass objects as arguments to a function (or object), new local variables are created referencing the original objects without copying.

    However, if we assign a new object to a variable inside a function, this operation will not overwrite the variable of the same name in the **scope** outside of the function (the **parent scope**). This is particular helpful when we need to alter the internals of a mutable (changeable) argument.
    """
    )
    return


@app.cell
def _():
    def append_element(target_list, element):
        data = '123abc'
        target_list.append(element)
        print("inside the function, data is", data)

    data = [1,2,3]
    append_element(data, 4)
    print(data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Strong Types, Dynamic reference
    As the example shown earlier, variables in Python have no inherent type associated with them. A variable can refer to different types of object simply by doing an assignment operation. Variables are just names for objects within a particular scope (**namespace**), the type information is stored in the object itself. Python is in fact a strongly typed language. Every object has a specific type (class), and implicit conversions will occur only in certain permitted circumstances. 

    Since Python 3.5, type annotation has been supported in Python. However, the Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.
    """
    )
    return


@app.cell
def _():
    a_2 = 5
    print(type(a_2))
    b_2 = 6
    a_2 = '5'
    print(type(a_2))
    c = a_2 + b_2
    return


@app.cell
def _():
    def moon_weight(earth_weight: float) -> str:
        return f'On the moon, you would weigh {earth_weight * 0.166} kilograms.'
    a_3 = 500
    b_3 = 500.0
    print(isinstance(a_3, float))
    print(moon_weight(a_3))
    print(moon_weight(b_3))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Variable/Reference/Memory Allocation – a metaphor**

    ![](imgaes/variables/address.jpeg)
    <!-- <img src="images/variables/address.jpeg" /> -->

    The address _5818 Phillips Avenue, Pittsburgh, PA 15217_ maps to georgraphic coordinates of _40.432392,-79.922378_ -- it is essentially a label for a specific latitude and longitude.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Scalar Types in Python
    Python has a small set of basic built-in types for handling numerical data, strings, Boolean(```True``` or ```False```) values, and dates and time. Sometimes they are referred to as "scalar types" or "primitive types". These types form the foundation for more complex data structures and are essential for various operations in Python.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### 1. Numeric Types (int, float, complex)
    There are three distinct numeric types: integers, floating point numbers, and complex numbers. Integers have unlimited precision. Floating point numbers are usually implemented using double in C. Complex numbers have a real and imaginary part, which are each a floating point number.

    We can do all kinds of mathematical operations with numeric types. Some operations may also result in implicit type conversions.
    """
    )
    return


@app.cell
def _():
    a_4 = 172
    b_4 = 1.0
    c_1 = 1j
    c_ = 1 + 2j
    print(type(a_4), type(b_4), type(c_1), type(c_))
    aa = a_4 ** a_4
    print(aa)
    import sys
    print(sys.float_info)
    return


@app.cell
def _():
    # Mathematical Operations Examples
    x = 5
    y = 10
    print(f'x + y = {x + y}') # addition
    print(f'x - y = {x - y}') # subtraction
    print(f'x * y = {x * y}') # multiplication
    print(f'x / y = {x / y}') # division -> float
    print(f'x ** y = {x ** y}') # x to the power of y
    print(f'x // y = {x // y}') # floor division -> integer
    print(f'x % y = {x % y}') # modulo -> remainder of the division
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### 2. String Type (str)
    Python strings are immutable, meaning that you cannot change a string like in other programming language.
    """
    )
    return


@app.cell
def _():
    # we can use single or double quotes to define a string
    name = "Bob"
    car = 'Ford Pinto'

    # multiline string
    address = """
    5818 Phillips Avenue, 
    Pittsburgh, 
    PA 15217
    """

    print(address.count('\n')) # there are 4 lines in the address
    return


@app.cell
def _():
    # Combining strings
    full_name = 'John' + ' ' + 'Doe' # => 'John Doe'
    print(full_name)
    return (full_name,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Strings are a sequence of Unicode characters and therefore can be treated like other sequences, for instance slicing [0:4]""")
    return


@app.cell
def _(full_name):
    print(full_name[0]) # => 'J'
    print(full_name[-1]) # => 'e'
    print(full_name[:4]) # => 'John'
    full_name[1] = '0' # This will raise an error because strings are immutable
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Sometimes strings may need to contain certain special characters, we will be using "\" as the *escape character* to specify special characters like newline "\n" or Unicode characters. 

    "\" itself is also a special character.
    """
    )
    return


@app.cell
def _():
    Special_char = "backslash\\; \nUnicode characters like: \u00A7, \u00A9, \u2030;\nor emojis: \u263A"
    print(Special_char)

    # if you need to use a lot of special characters (i.e. "\"), you can use a raw string.
    raw_string = r"backslash\; \nUnicode characters like: \u00A7, \u00A9, \u2030;\nor emojis: \u263A"
    print(raw_string)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In Python 3.6, a new feature named *f-string* (short for *formatted string literals*) was introduced. It allows for a very convenient way to create formatted strings. 

    To use f-string, simply write the "f" immediately preceding a string. Within the string, enclose Python expressions in curly braces to subsitute the value of the expression into the formatted string. We can also add format specifiers after each expression. To learn more, consult the [official Python documentation](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
    """
    )
    return


@app.cell
def _():
    FG_attempts = 46
    FG_made = 28
    print(f"Kobe shot {FG_made}-for-{FG_attempts} ({FG_made / FG_attempts:.2f} percent) from the field that game.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### 3. Booleans (bool)""")
    return


@app.cell
def _():
    x_1 = True
    y_1 = False
    return x_1, y_1


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Boolean Truth Table**

    <img src='images/variables/truth_table.png' />
    """
    )
    return


@app.cell
def _(x_1, y_1):
    print(x_1 and y_1)
    print(x_1 or y_1)
    print(x_1 and (not y_1))
    print(not x_1)
    print(x_1 is True)
    return


@app.cell
def _():
    # none is a special constant in Python that represents the absence of a value or a null value
    z = None

    print(z is None) # => True
    if z:
        print('z is not None')
    else:
        print('z is None')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### 4. Typecasting: converting from one data type to another""")
    return


@app.cell
def _():
    x1 = 5
    y_2 = str(x1)
    x2 = '5'
    y_2 = int(x2)
    x_2 = '5'
    y_2 = float(x_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Exercise: Pythagorean Theorem**

    This program accepts two input values from the user, one for each
    side of a right-angle triangle.  The program uses the Pythagorean
    theorem (c^2 = a^2 + b^2) to calculate the length of the triangle's
    hypotenuse.
    """
    )
    return


@app.cell
def _():
    import math
    return (math,)


@app.cell
def _():
    # Get user input for Side A
    inputSideA = input("Enter length of side A ")

    print("Side A: " + str(inputSideA))
    return (inputSideA,)


@app.cell
def _():
    # Get user input for Side B
    inputSideB = input("Enter length of side B ")

    print("Side B: " + str(inputSideB))
    return (inputSideB,)


@app.cell
def _(inputSideA, inputSideB):
    # Values entered through user input are stored as strings (String data type).  We need to
    # convert sides' lengths from String to float
    sideA = float(inputSideA)
    sideB = float(inputSideB)
    return sideA, sideB


@app.cell
def _(sideA, sideB):
    # Calculate square of side A
    # Note that ** (double asterisk) is an exponent operand.  It performs exponential (power) calculation on operators
    squareSideA = sideA ** 2

    # Calculate square of side B
    squareSideB = sideB ** 2
    return squareSideA, squareSideB


@app.cell
def _(math):
    # Use Pythagorean theorem to calculate the length of the triangle's hypotenuse.
    # math.sqrt(a) function calculates the square root of the argument "a"
    def hypotenuse(squareA: int, squareB: int):
        return math.sqrt(squareA + squareB)
    return (hypotenuse,)


@app.cell
def _(hypotenuse, sideA, sideB, squareSideA, squareSideB):
    # Print out the results
    print(f"Given that side A is {sideA} and side B is {sideB}, the hypotenuse is {hypotenuse(squareSideA, squareSideB)}")
    return


@app.cell
def _():
    z_1 = input('Insert a')
    if str(z_1).isdigit():
        print('IS DIGIT')
    else:
        print('not digit')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Challenge

    Modify the program to accept input for the lengths of one adjacent side and the hypotenuse of a right triangle. Calculate the second adjacent side.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Step 1:** Get user input for Side A""")
    return


@app.cell
def _():
    inputSideA_1 = input('Enter length of side A ')
    print('Side A: ' + str(inputSideA_1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Step 2:** Get user input for Hypothenuse""")
    return


@app.cell
def _():
    # Write Step 2 code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Step 3:** Remember that values entered through user input are stored as strings (String data type).  You will need to convert sides' lengths from _String_ to _float_""")
    return


@app.cell
def _():
    # Write Step 3 code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Step 4:** Calculate squares of side A and of hypothenuse""")
    return


@app.cell
def _():
    # Write Step 4 code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Step 5:** Use Pythagorean theorem to calculate the length of Side B

    _Hint: Side B = square root of square of Hypotenuse - square of Side A)_
    """
    )
    return


@app.cell
def _():
    # Write Step 5 code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Step 6**: Print results""")
    return


@app.cell
def _():
    # Write Step 6 code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Pythagorean Theorem Challenge Solution""")
    return


@app.cell
def _():
    inputSideA_2 = input('Enter length of side A ')
    print('Side A: ' + str(inputSideA_2))
    return (inputSideA_2,)


@app.cell
def _():
    # Get user input for hypotenuse
    inputHypotenuse = input("Enter length of the hypotenuse ")

    print("Hypotenuse: " + str(inputHypotenuse))
    return (inputHypotenuse,)


@app.cell
def _(inputHypotenuse, inputSideA_2):
    sideA_1 = float(inputSideA_2)
    hypotenuse_1 = float(inputHypotenuse)
    return hypotenuse_1, sideA_1


@app.cell
def _(hypotenuse_1, sideA_1):
    squareSideA_1 = sideA_1 ** 2
    squareHypotenuse = hypotenuse_1 ** 2
    return squareHypotenuse, squareSideA_1


@app.cell
def _(math, squareHypotenuse, squareSideA_1):
    sideB_1 = math.sqrt(squareHypotenuse - squareSideA_1)
    return (sideB_1,)


@app.cell
def _(hypotenuse_1, sideA_1, sideB_1):
    print('Given that side A is ' + str(sideA_1) + ' and the hypotenuse is ' + str(hypotenuse_1) + ', side B is ' + str(sideB_1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Control Flow
    Python uses serveral built-in keywords for conditional logic, loops, and other standard control flow concepts found in other programming languages.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### 1. if, elif, and else""")
    return


@app.cell
def _():
    # Pay close attention to the equal sign (=)
    # When we use the equal sign to assign a value to a variable, Python treats it as an "ASSIGNMENT" operator
    # In the line of code below, we are assigning the value of "True" to the boolean variable "condition"
    condition = True
    condition2 = False

    # When we need to compare two values, we have to use a double equal sign (==), which is a "COMPARISON" operator
    # In the line of code below we compare the value already stored in the boolean varialbe "condition" to "True"
    if condition == True or condition2 != False:
        print("The code inside if block gets executed")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Chained "_if_" statements**""")
    return


@app.cell
def _():
    condition_1 = True
    if condition_1 == True:
        print('The code inside if block gets executed')
    if condition_1 == False:
        print('The code inside this block will not be executed')
    if condition_1 == True:
        print('The code inside if block gets executed')
    else:
        print('The code inside this block will not be executed')
    return


@app.cell
def _():
    # Let's try the same thing, but this time with user input

    user_input_str = input("Please enter a number: \n")
    user_input_num = int(user_input_str)
    if user_input_num > 10:
        print("You entered number " + str(user_input_num) + ". That number is greater than 10")

    if user_input_num < 10:
        print("You entered number " + str(user_input_num) + ". That number is less than 10")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Is there anything wrong with the code above?**""")
    return


@app.cell
def _():
    user_input_str_1 = input('Please enter a number: \n')
    user_input_num_1 = int(user_input_str_1)
    if user_input_num_1 > 10:
        print('You entered number ' + str(user_input_num_1) + '. That number is greater than 10')
    else:
        print('You entered number ' + str(user_input_num_1) + '. That number is less than or equal to 10')
    return


@app.cell
def _():
    user_input_str_2 = input('Please enter a number: \n')
    user_input_num_2 = int(user_input_str_2)
    if user_input_num_2 > 10:
        print('You entered number ' + user_input_str_2 + '. That number is greater than 10')
    elif user_input_num_2 == 10:
        print('You entered number ' + user_input_str_2 + '. That number equals to 10')
    else:
        print('You entered number ' + user_input_str_2 + '. That number is less than 10')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ##### Exercise

    **Lucky Number**

    Many cultures consider number 7 to be a lucky number.  This program takes a numeric
    input from a user and checks if the input is a "lucky" number.
    """
    )
    return


@app.cell
def _():
    # We will declare our lucky number 7 as a variable
    LUCKY_NUMBER = 7
    return (LUCKY_NUMBER,)


@app.cell
def _():
    # Ask user to input a number.  Note that even though the user will enter a number,
    # Python will treat the input as a string
    user_input = input("Please enter a number:")

    print("You entered: " + user_input)
    return (user_input,)


@app.cell
def _(user_input):
    # Now we need to convert the input string to a number.  In this case, we will convert the
    # input string to an integer
    num = int(user_input)
    return (num,)


@app.cell
def _(LUCKY_NUMBER, num):
    # Check if the number equals to 7.  Note that we are using a comparison operator
    # (double-equal sign ==) instead of the assignment operator (single equal sign =)
    # Also important to note that Python will not concatenate strings with other data types,
    # such as integers, so we need to cast / convert all non-string types to string during
    # concatenation
    if num == LUCKY_NUMBER:
        print("You entered the lucky number " + str(LUCKY_NUMBER) + "!")
    else:
        print("You entered number " + str(num) + ".  It may be a lucky number for you, but it's not the lucky number " + str(LUCKY_NUMBER) + "!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Lucky Number: Challenge 1**

    Some users will try to submit a blank input.  When user submits input without entering a value, input string will be empty, or equal to a blank string (""). Make sure to validate user inputs
    """
    )
    return


@app.cell
def _():
    LUCKY_NUMBER_1 = 7
    user_input_1 = input('Please enter a number:')
    print('You entered: ' + user_input_1)
    return


@app.cell
def _():
    # Write your challenge solution code here
    # Hint: Python has a built-in function that checks if the 
    # value is numeric.  Use Google to figure out the name of that function 
    # and how to use it.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Lucky Number: Challenge 1 Solution**""")
    return


@app.cell
def _():
    LUCKY_NUMBER_2 = 7
    user_input_2 = input('Please enter a number:')
    print('You entered: ' + user_input_2)
    return LUCKY_NUMBER_2, user_input_2


@app.cell
def _(LUCKY_NUMBER_2, user_input_2):
    if user_input_2.isdigit():
        num_1 = int(user_input_2)
        if num_1 == LUCKY_NUMBER_2:
            print('You entered the lucky number ' + str(LUCKY_NUMBER_2) + '!')
        else:
            print('You entered number ' + str(num_1) + ".  It may be a lucky number for you, but it's not the lucky number " + str(LUCKY_NUMBER_2) + '!')
    else:
        print('Hey, if you want us to tell you your lucky number, you actually have to enter one!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Lucky Number: Challenge 2**

    In Italy number **17** is also considered unlucky. The unluckiness of seventeen in Italian culture
    dates back to the Roman times.  Seventeen in Roman numnerals is XVII, which is an anagram for VIXI,
    which is Latin for "I Lived" and is a common marking on Roman tombstones.
    Modify the program below to not only check for lucky number 7, but also for unlucky numbers 13 and 17
    and to display appropriate messages.
    """
    )
    return


@app.cell
def _():
    LUCKY_NUMBER_3 = 7
    UNLUCKY_NUMBER1 = 13
    UNLUCKY_NUMBER2 = 17
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Step 1: **Get user input""")
    return


@app.cell
def _():
    # Write Step 1 code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Step 2: **Convert user input to integer""")
    return


@app.cell
def _():
    # Write Step 2 code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Step 3: **Check if the number equals to 7 or 13 or 17. Display appropriate messages""")
    return


@app.cell
def _():
    # Write Step 3 code here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**Lucky Number: Challenge 2 Solution**""")
    return


@app.cell
def _():
    LUCKY_NUMBER_4 = 7
    UNLUCKY_NUMBER1_1 = 13
    UNLUCKY_NUMBER2_1 = 17
    return LUCKY_NUMBER_4, UNLUCKY_NUMBER1_1, UNLUCKY_NUMBER2_1


@app.cell
def _():
    user_input_3 = input('Please enter a number:')
    print('You entered: ' + user_input_3)
    return (user_input_3,)


@app.cell
def _(user_input_3):
    num_2 = int(user_input_3)
    return (num_2,)


@app.cell
def _(LUCKY_NUMBER_4, UNLUCKY_NUMBER1_1, UNLUCKY_NUMBER2_1, num_2):
    if num_2 == LUCKY_NUMBER_4:
        print('You entered the lucky number ' + str(LUCKY_NUMBER_4) + '!')
    elif num_2 == UNLUCKY_NUMBER1_1 or num_2 == UNLUCKY_NUMBER2_1:
        print('You entered an extremely unlucky number of ' + str(num_2) + '! Be more careful with your inputs in the future.')
    else:
        print('You entered number ' + str(num_2) + ".  It may be a lucky number for you, but it's not the lucky number " + str(LUCKY_NUMBER_4) + '!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### 2. for loops
    ```for``` loops are for ierating over a collection (like a list or tuple) or an iterater.
    """
    )
    return


@app.cell
def _():
    sequence = [1, 2, None, 4, None, 5]
    total = 0
    for value in sequence:
        if value is None:
            continue
        total = total + value
    print(total)
    return (sequence,)


@app.cell
def _(sequence):
    for value_1 in sequence:
        print(value_1)
        if value_1 is None:
            break
    return


@app.cell
def _():
    # If we want to iterate over a certain amount of times, we can use the range function
    # range(10) will generate a sequence of numbers from 0 to 9
    for i in range(10):
        print(i)

    print()
    # we can also specify the starting point of the range, and the step
    for i in range(10, 2, -2):
        print(i)
    return


@app.cell
def _():
    # Range function generates a sequence of numbers, but it doesn't store them in memory
    range_10 = range(10)
    print(range_10)
    print(list(range_10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""If the elements in the collection or iterator are also sequences (tuples or lists, for instance), they can be conveniently unpacked into variables in the ```for``` loop statement.""")
    return


@app.cell
def _():
    dict = {'John': 37, 'Bob': 50, 'Jane': 29, 'Ann': 71}
    for key, value_2 in dict.items():
        print(key, value_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### 3. while loop
    A while loop specifies a condition and a block of code that is to be executed until the condition evaluates to ```False``` or the loop is explicitly ended with ```break```.
    """
    )
    return


@app.cell
def _():
    x_3 = 256
    total_1 = 0
    while x_3 > 0:
        if total_1 > 500:
            break
        total_1 = total_1 + x_3
        x_3 = x_3 // 2
    print(f'x = {x_3}, total = {total_1}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Data Structures""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Tuple
    A tuple is a fixed-lengeth, immutable sequence of Python objects which once assigned, cannot be changed.
    """
    )
    return


@app.cell
def _():
    tup = (4,5,6)
    print(tup)

    tup_ = 7,8,9 # This is another way to create a tuple
    print(tup_)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Lists

    **List data structure**

    * A Python list is a sequence of values
    * Values in a Python list can by of any datatype
    * Each element of a sequence is assigned a number - its position or index. The first index is zero, the second index is one, and so forth.
    """
    )
    return


@app.cell
def _():
    # Creating Lists
    list1 = ['apples', 'oranges', 'pears', 'peaches'];
    list2 = [1, 2, 3, 4, 5];
    list3 = ["a", "b", "c", "d"]
    # Note that the following list contains mixed data types
    list4 = [1, 2, "x", "y", "z", True]
    return


@app.cell
def _():
    # Accessing Values in Lists
    fruits = ['apples', 'oranges', 'pears', 'peaches', 'berries'];
    print(fruits[0]) # Get the first element of the list
    print(fruits[1:3]) # Get the first two elements of the list
    print(fruits[:3]) # Get everything before the element with index 3
    print(fruits[3:]) # Get everything starting with the element with index 3
    print(fruits[-1]) # Get the last element of the list
    return


@app.cell
def _():
    fruits_1 = ['apples', 'oranges', 'pears', 'peaches', 'berries']
    print('Value at index 2 is: ' + fruits_1[2])
    fruits_1[2] = 'bananas'
    print('New value at index 2 is : ' + fruits_1[2])
    return


@app.cell
def _():
    fruits_2 = ['apples', 'oranges', 'pears', 'peaches', 'berries']
    print(fruits_2)
    fruits_2.append('bananas')
    print(fruits_2)
    return


@app.cell
def _():
    fruits_3 = ['apples', 'oranges', 'pears', 'peaches', 'berries']
    print(fruits_3)
    del fruits_3[2]
    print(fruits_3)
    return


@app.cell
def _():
    fruits_4 = ['apples', 'oranges', 'pears', 'peaches', 'berries']
    print(fruits_4)
    fruits_4.remove('pears')
    print(fruits_4)
    return


@app.cell
def _():
    a_5 = [1, 2, 3, 4, 5, 6, 7, 3]
    print(a_5)
    a_5.remove(3)
    print(a_5)
    return


@app.cell
def _():
    fruits_5 = ['apples', 'oranges', 'pears', 'peaches', 'berries']
    vegetables = ['tomatoes', 'cucumbers', 'celery']
    food = vegetables + fruits_5
    print(food)
    return


@app.cell
def _():
    fruits_6 = ['apples', 'oranges', 'pears', 'peaches', 'berries']
    vegetables_1 = ['tomatoes', 'cucumbers', 'celery']
    print(fruits_6)
    fruits_6.append('apples')
    print(fruits_6)
    new_list = fruits_6 + vegetables_1
    print(new_list)
    return


@app.cell
def _():
    fruits_7 = ['apples', 'oranges', 'pears', 'peaches', 'berries']
    sorted_fruits = sorted(fruits_7)
    print(sorted_fruits)
    return


@app.cell
def _():
    str1 = "elvis"
    str2 = "lives"

    str1_sorted = sorted(str1)
    print(str1_sorted)
    str2_sorted = sorted(str2)
    print(str2_sorted)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Dictionaries

    **Dictionary Data Type:**
    * A dictionary is a collection of items
    * Each item consists of a key / value pair
    * The items are separated by commas
    * Each key is separated from its value by a colon (:)
    * An empty dictionary without any items is written with just two curly braces: {}.
    * Keys are unique within a dictionary while values may not be
    * The values of a dictionary can be of any type, but the keys must be strings or numbers.
    """
    )
    return


@app.cell
def _():
    dict_1 = {'John': 37, 'Bob': 50, 'Jane': 29, 'Ann': 71}
    return (dict_1,)


@app.cell
def _(dict_1):
    print(dict_1['John'])
    print(dict_1['Bob'])
    print(dict_1['Jane'])
    return


@app.cell
def _():
    account = {
        "1a" : 2000,
        "1b" : 1000000,
        "1c" : -200
    }
    return (account,)


@app.cell
def _(account):
    print(account)
    return


@app.cell
def _():
    account_1 = {}
    account_1['1a'] = 2000
    account_1['1b'] = 1000000
    account_1['1c'] = -200
    print(account_1)
    return


@app.cell
def _():
    dict_2 = {'John': 37, 'Bob': 50, 'Jane': 29, 'Ann': 71}
    dict_2['John'] = 389
    dict_2['Rose'] = 32
    print(dict_2)
    return


@app.cell
def _():
    dict_3 = {'John': 37, 'Bob': 50, 'Jane': 29, 'Ann': 71}
    del dict_3['John']
    dict_3.clear()
    del dict_3
    dict_3 = None
    return


@app.cell
def _():
    shopping_hist = {}

    shopping_hist["fruits"] = ['apples', 'oranges', 'pears', 'peaches', 'berries'];
    shopping_hist["vegetables"] = ['tomatoes', 'cucumbers', 'celery']
    print(shopping_hist)
    return


@app.cell
def _():
    {
        'fruits': ['apples', 'oranges', 'pears', 'peaches', 'berries'], 
        'vegetables': ['tomatoes', 'cucumbers', 'celery']
    }
    return


@app.cell
def _():
    # Lists of dictionaries
    employees = [
        {
            "first_name" : "John",
            "last_name" : "Smith",
            "age" : 50,
            "has_insurance" : False
        },
        {
            "first_name" : "Jane",
            "last_name" : "Doe",
            "age" : 37,
            "has_insurance" : True
        }
    ]
    return (employees,)


@app.cell
def _(employees):
    employees[1]["has_insurance"] = True
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise:

    ** Shopping List **

    This program creates a list called groceries and defines two dictionaries, stock and prices. Using these structures, it computes the bill for the list of groceries.
    """
    )
    return


@app.cell
def _():
    # First, create a list called shopping_list that contains the strings "banana", "orange", and "apple"
    shopping_list = ["banana", "orange", "apple"]
    return (shopping_list,)


@app.cell
def _():
    # Next, create the empty prices dictionary
    prices = {}

    # We can then add values to the dictionary
    prices["banana"] = 4
    prices["apple"] = 2
    prices["orange"] = 1.5
    prices["pear"] = 3
    return (prices,)


@app.cell
def _():
    # Next, create the stock dictionary
    # We will use a different method from before and simply create the dictionary all at once
    # Note that we use commas to separate items and a comma does not appear after the last item in the dictionary
    # Also note that the dictionary can be declared on one line or multiple
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    return (stock,)


@app.cell
def _(prices, stock):
    # To illustrate how to print out the items in a dictionary along with their associated values, 
    # we can use a loop like the one below
    for item in prices:
        print(item)
        print("price: " + str(prices[item]))
        print("stock: " + str(stock[item]))
    return


@app.cell
def _(prices, shopping_list, stock):
    grocery_bill = 0
    for item_1 in shopping_list:
        if stock[item_1] > 0:
            price = prices[item_1]
            grocery_bill = grocery_bill + price
            stock[item_1] = stock[item_1] - 1
        else:
            print(item_1 + 's are not in stock!')
    return (grocery_bill,)


@app.cell
def _(grocery_bill):
    # Finally, output the result
    print("Cost of groceries: " + str(grocery_bill))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ** Shopping List: Challenge 1**

    Write a loop to determine the value of the store's entire stock.
    """
    )
    return


@app.cell
def _():
    # Write challenge 1 solution here
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""** Shopping List: Challenge 1 Solution**""")
    return


@app.cell
def _():
    shopping_list_1 = ['banana', 'orange', 'apple']
    return (shopping_list_1,)


@app.cell
def _():
    prices_1 = {}
    prices_1['banana'] = 4
    prices_1['apple'] = 2
    prices_1['orange'] = 1.5
    prices_1['pear'] = 3
    return (prices_1,)


@app.cell
def _():
    stock_1 = {'banana': 6, 'apple': 0, 'orange': 32, 'pear': 15}
    return (stock_1,)


@app.cell
def _(prices_1, stock_1):
    for item_2 in prices_1:
        print(item_2)
        print('price: ' + str(prices_1[item_2]))
        print('stock: ' + str(stock_1[item_2]))
    return


@app.cell
def _(prices_1, shopping_list_1, stock_1):
    grocery_bill_1 = 0
    for item_3 in shopping_list_1:
        if stock_1[item_3] > 0:
            price_1 = prices_1[item_3]
            grocery_bill_1 = grocery_bill_1 + price_1
            stock_1[item_3] = stock_1[item_3] - 1
        else:
            print(item_3 + 's are not in stock!')
    print('Your total bill is', grocery_bill_1)
    return


@app.cell
def _(prices_1, stock_1):
    total_stock = 0
    for item_4 in stock_1:
        total_stock = total_stock + stock_1[item_4] * prices_1[item_4]
    print("The value of the store's stock is " + str(total_stock))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Functions

    [https://www.tutorialspoint.com/python/python_functions.htm]

    * A function is a block of organized, reusable code that is used to perform a single, related action. 
    * Functions provide better modularity for your application and a high degree of code reusing.

    ### Defining a Function

    * Function blocks begin with the keyword _def_ followed by the function name and parentheses _(  )_.
    * Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
    * The code block within every function starts with a colon (:) and is indented.
    * The statement _return [expression]_ exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

    ### Syntax
    def functionname( parameters ):

        function code
        more code
        even more code

        return [expression]
    """
    )
    return


@app.function
# Function name: add_two_numbers
# Parameter(s): num1, num2
# Description: This function adds two numbers
# Return: This function returns a sum of two numbers
def add_two_numbers(num1, num2):
    sum_of_two_numbers = num1 + num2
    return sum_of_two_numbers


@app.cell
def _():
    # Calling a function
    result = add_two_numbers(5, 7)
    print(result)
    return


@app.cell
def _():
    var1 = 10
    var2 = 20
    result_1 = add_two_numbers(var1, var2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **Important notes about functions**
    * A function name along with its parameters make up the functions **signature**
    * When calling a function, you must pass values for each parameter in EXACTLY the same order as it appears in the parameter list

    **Named parameters**
    * Sometimes, we want parameters to have default values (values that will be automatically assigned to a parameter)
    * Sometimes, we also want to pick and choose which parameters to pass into a function (have optional parameters)
    * To address these two use cases, we can create functions with **named** parameters

    **Syntax for functions with named parameters:**

    def functionname( parameter_1_name = parameter_1_value, parameter_2_name = parameter_2_value ):

        function code
        more code
        even more code

        return [expression]
    """
    )
    return


@app.function
# Note that "operation" is a named parameter.  
# It has a default value of "add" and can be skipped alltogether
def do_math_with_two_numbers(num1, num2, operation = "add"):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2
    return result


@app.cell
def _():
    # Call the function without the named parameter
    test = do_math_with_two_numbers(5, 10)
    print(test)

    # Call the function with the named parameter
    test = do_math_with_two_numbers(5, 10, operation="subtract")
    print(test)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Reading Text Files

    ### Working With CSV Files

    CSV files are used to store a large number of variables – or data. They are incredibly simplified spreadsheets – think Excel – only the content is stored in plaintext.

    And the CSV module is a built-in function that allows Python to parse these types of files.
    """
    )
    return


@app.cell
def _():
    # To parse CSV files, we use the csv module. CSV literally stands for comma separated value, 
    # where the comma is what is known as a "delimiter." The csv module provides a number of built-in
    # functions to make it easier to parse and iterate through CSV files.
    import csv
    return (csv,)


@app.cell
def _():
    # Open the diabetes file.  Note that when Python opens data files and stores them in variables,
    # the variables DO NOT actually contain text.  In the example below, the diabetes_file 
    # variable stores the file in a special format (one that Python can understand and interpret)
    diabetes_file = open("diabetes.csv")
    return (diabetes_file,)


@app.cell
def _(diabetes_file):
    # See what happens when we try to print the variable where the data file is stored
    # Essentially, the file is treated as an OBJECT - we'll learn about objects next week
    print(diabetes_file)
    return


@app.cell
def _(csv, diabetes_file):
    # Now we need to tell Python that the file stored in diabetes_file variable should be read as 
    # and interpreted as a CSV file.  We do that by calling on the reader() function of the csv module
    diabetes_data = csv.reader(diabetes_file)
    return (diabetes_data,)


@app.cell
def _(diabetes_data):
    # At this point, the entire CSV file is treated as a table - a collection of rows and columns
    # We can iterate (loop) through this table and get access to each individual row
    for row in diabetes_data:
        print(row)
    return


@app.cell
def _(diabetes_data, diabetes_file):
    diabetes_file.seek(0)
    for row_1 in diabetes_data:
        print(row_1[1])
    return


@app.cell
def _(diabetes_data, diabetes_file):
    cnt = 0
    diabetes_file.seek(0)
    for row_2 in diabetes_data:
        if cnt > 0:
            print(row_2[1])
        cnt = cnt + 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    **CSV files - Challenge 1**

    Calculate the _average_ and the _highest (max)_ cholesterol value based on the data available in the dataset.
    """
    )
    return


@app.cell
def _():
    # Step 1: Import csv module
    return


@app.cell
def _(csv):
    diabetes_file_1 = open('diabetes.csv')
    diabetes_data_1 = csv.reader(diabetes_file_1)
    return diabetes_data_1, diabetes_file_1


@app.cell
def _(diabetes_data_1, diabetes_file_1):
    cnt_1 = 0
    diabetes_file_1.seek(0)
    for row_3 in diabetes_data_1:
        if cnt_1 > 0:
            print(row_3[1])
        cnt_1 = cnt_1 + 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""**CSV files - Challenge 1 Solution**""")
    return


@app.cell
def _():
    # Step 1: Import csv module
    return


@app.cell
def _(csv):
    diabetes_file_2 = open('diabetes.csv')
    diabetes_data_2 = csv.reader(diabetes_file_2)
    return diabetes_data_2, diabetes_file_2


@app.cell
def _(diabetes_data_2, diabetes_file_2):
    cnt_2 = 0
    diabetes_file_2.seek(0)
    total_2 = 0
    for row_4 in diabetes_data_2:
        if row_4[1] != '':
            if cnt_2 > 0:
                total_2 = total_2 + int(row_4[1])
            cnt_2 = cnt_2 + 1
    print('Total: ', total_2)
    print('Count: ', cnt_2)
    avg_chol = total_2 / cnt_2
    print('Average: ', avg_chol)
    return


@app.cell
def _(diabetes_data_2, diabetes_file_2):
    cnt_3 = 0
    diabetes_file_2.seek(0)
    max_chol = 0
    for row_5 in diabetes_data_2:
        if row_5[1] != '':
            if cnt_3 > 0:
                if max_chol < int(row_5[1]):
                    max_chol = int(row_5[1])
            cnt_3 = cnt_3 + 1
    print('Maximum cholesterol: ', max_chol)
    return


if __name__ == "__main__":
    app.run()
