def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# It iterates through numbers starting at 1 and ending at 19.
# In Python, range(start, stop) is exclusive of the stop value, so range(1, 20) stops before 20.

# 2. When is the function meant to print "You got it"?
# When the loop variable i equals 20.

# 3. What are your assumptions about the value of i?
# The original code assumes that i will eventually reach 20 during the loop execution.
# However, i maxes out at 19, meaning the condition i == 20 is never True.
