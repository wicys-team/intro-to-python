# Python has a print statement
print "I'm Python. Nice to meet you!"  # => I'm Python. Nice to meet you!

# Simple way to get input data from console
input_string_var = raw_input(
    "Enter some data: ")  # Returns the data as a string
input_var = input("Enter some data: ")  # Evaluates the data as python code
# Warning: Caution is recommended for input() method usage
# Note: In python 3, input() is deprecated and raw_input() is renamed to input()

# No need to declare variables before assigning to them.
some_var = 5  # Convention is to use lower_case_with_underscores
some_var  # => 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
# some_other_var  # Raises a name error

# if can be used as an expression
# Equivalent of C's '?:' ternary operator
"yahoo!" if 3 > 2 else 2  # => "yahoo!"

