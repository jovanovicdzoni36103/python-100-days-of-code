# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "Invalid input"
#
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name(input("Enter your first name: "), input("Enter your last name: ")))



# LEAP YEAR
# Write a program that returns True or False for whether a given year is a leap year.
#
# A normal year has 365 days, a leap year has 366, with an extra day in February.
#
# Rules, in this order:
#   - every year divisible by 4 with no remainder is a leap year
#   - except every year divisible by 100 with no remainder, which is not
#   - unless the year is also divisible by 400 with no remainder, which is
#
# Example, year 2000:
#   2000 / 4   = 500    (leap)
#   2000 / 100 = 20     (not leap)
#   2000 / 400 = 5      (leap)
#   So 2000 IS a leap year.
#
# Example, year 2100:
#   2100 / 4   = 525    (leap)
#   2100 / 100 = 21     (not leap)
#   2100 / 400 = 5.25   (not leap)
#   So 2100 is NOT a leap year.
#
# Warning: the function must RETURN a boolean, not print it.
# Output must match exactly, including spelling and capitalisation.
#
# Example input 1: 2400   ->  return True
# Example input 2: 1989   ->  return False
#
# Note: the Udemy exercise has no console, so input() is not allowed there.
# The function is called with hard-coded values, for example is_leap_year(2024).
# Function name must be is_leap_year and it takes one parameter, year.

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap_year(2000))
print(is_leap_year(2100))
print(is_leap_year(2400))
print(is_leap_year(1989))