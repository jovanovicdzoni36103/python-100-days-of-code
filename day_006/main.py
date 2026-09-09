"""
============================================================
TASK 01 — Say Hello
Difficulty: ⭐
Topic: Functions
============================================================

Create a function called say_hello().

The function should print:

Hello!

Then call the function once.
"""

def say_hello():
    print("Hello!")


say_hello()


"""
============================================================
TASK 02 — Greet the User
Difficulty: ⭐
Topic: Functions + Input
============================================================

Create a function called greet_user().

Ask the user:

What is your name?

Then print:

Hello, Nikola!

if the user enters Nikola.
"""

def greet_user():
    name = input("What is your name? ")
    print("Hello, " + name)


greet_user()


"""
============================================================
TASK 03 — Double the Number
Difficulty: ⭐
Topic: Functions + Input + Numbers
============================================================

Create a function called double_number().

Ask the user to enter a number.

Multiply the number by 2 and print the result.

Example:

Enter a number: 7
14
"""

def double_number():
    number = int(input("Enter a number: "))
    print(number * 2)


double_number()


"""
============================================================
TASK 04 — Check the Number
Difficulty: ⭐⭐
Topic: Functions + If Statements
============================================================

Create a function called check_number().

Ask the user to enter a number.

If the number is greater than 10, print:

Big number!

Otherwise, print:

Small number!
"""

def check_number():
    number = int(input("Enter a number: "))

    if number > 10:
        print("Big number!")
    else:
        print("Small number!")


check_number()


"""
============================================================
TASK 05 — Count to Ten
Difficulty: ⭐⭐
Topic: Functions + For Loops
============================================================

Create a function called count_to_ten().

When the function is called, print the numbers from 1 to 10.

Expected output:

1
2
3
4
5
6
7
8
9
10
"""

def count_to_ten():
    for number in range(1, 11):
        print(number)


count_to_ten()


"""
============================================================
TASK 06 — Repeat a Message
Difficulty: ⭐⭐
Topic: Functions + For Loops + Input
============================================================

Create a function called repeat_message().

Ask the user:

How many times should I print the message?

Then print:

Hello!

exactly that many times.

Example:

How many times should I print the message? 3
Hello!
Hello!
Hello!
"""

def repeat_message():
    times = int(input("How many times should I print the message? "))

    for i in range(times):
        print("Hello!")


repeat_message()


"""
============================================================
TASK 07 — Calculate the Sum
Difficulty: ⭐⭐
Topic: For Loops + Variables
============================================================

Create a function called calculate_sum().

Calculate the sum of all numbers from 1 to 100.

Print the final result.

Expected output:

5050
"""

def calculate_sum():
    total = 0

    for number in range(1, 101):
        total += number

    print(total)


calculate_sum()


"""
============================================================
TASK 08 — Print Even Numbers
Difficulty: ⭐⭐⭐
Topic: For Loops + If Statements
============================================================

Create a function called print_even_numbers().

Print every even number from 1 to 20.

Expected output:

2
4
6
8
10
12
14
16
18
20
"""

def print_even_numbers():
    for number in range(1, 21):
        if number % 2 == 0:
            print(number)


print_even_numbers()


"""
============================================================
TASK 09 — Password Attempts
Difficulty: ⭐⭐⭐
Topic: For Loops + If Statements + Input
============================================================

The correct password is:

python123

Give the user 3 attempts to enter the correct password.

If the password is correct, print:

Access granted!

If all 3 attempts are incorrect, print:

Access denied!
"""

def password_attempts():
    correct_password = "python123"

    for i in range(3):
        password = input("Enter password: ")

        if password == correct_password:
            print("Access granted!")
            break
    else:
        print("Access denied!")


password_attempts()


"""
============================================================
TASK 10 — Count to Ten with While
Difficulty: ⭐⭐⭐
Topic: While Loops
============================================================

Print the numbers from 1 to 10 using a while loop.

Do not use a for loop.

Expected output:

1
2
3
4
5
6
7
8
9
10
"""

number = 1

while number <= 10:
    print(number)
    number += 1


"""
============================================================
TASK 11 — Countdown
Difficulty: ⭐⭐⭐
Topic: While Loops
============================================================

Use a while loop to print:

10
9
8
7
6
5
4
3
2
1
Go!
"""

number = 10

while number >= 1:
    print(number)
    number -= 1

print("Go!")


"""
============================================================
TASK 12 — Keep Asking Until "no"
Difficulty: ⭐⭐⭐
Topic: While Loops + Input
============================================================

Keep asking the user:

Enter "no" to stop:

Continue running until the user enters:

no

After the user enters "no", print:

Goodbye!
"""

answer = ""

while answer != "no":
    answer = input('Enter "no" to stop: ')

print("Goodbye!")


"""
============================================================
TASK 13 — Unlimited Password Attempts
Difficulty: ⭐⭐⭐
Topic: While Loops + Conditions
============================================================

The correct password is:

python123

Keep asking:

Enter password:

until the user enters the correct password.

When the password is correct, print:

Access granted!
"""

correct_password = "python123"

password = ""

while password != correct_password:
    password = input("Enter password: ")

print("Access granted!")


"""
============================================================
TASK 14 — Number Guessing Game
Difficulty: ⭐⭐⭐⭐
Topic: While Loops + If Statements
============================================================

Create a variable:

secret_number = 7

Keep asking the user to guess the number until they get it
correct.

If the guess is incorrect, print:

Try again!

If the guess is correct, print:

You got it!
"""

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess != secret_number:
        print("Try again!")

print("You got it!")


"""
============================================================
TASK 15 — Basic Hurdle
Difficulty: ⭐⭐⭐⭐
Topic: Functions + If Statements
============================================================

Imagine a robot moving through a course.

Create two functions:

move()
jump()

The robot should:

1. Move forward.
2. Check whether there is a hurdle.
3. Jump if there is a hurdle.

Use a Boolean variable to represent whether a hurdle exists.
"""

def move():
    print("Move forward")


def jump():
    print("Jump!")


hurdle = True

move()

if hurdle:
    jump()


"""
============================================================
TASK 16 — Hurdles with a While Loop
Difficulty: ⭐⭐⭐⭐
Topic: While Loops + Functions + Conditions
============================================================

Imagine the robot has to cross 6 positions.

At every position, the robot should:

1. Move forward.
2. Check whether there is a hurdle.
3. Jump if necessary.
4. Continue until all 6 positions are completed.

Use a while loop.
"""

def move():
    print("Move forward")


def jump():
    print("Jump!")


position = 0

while position < 6:
    move()

    hurdle = position % 2 == 1

    if hurdle:
        jump()

    position += 1


"""
============================================================
TASK 17 — Hurdles with Functions
Difficulty: ⭐⭐⭐⭐⭐
Topic: Functions + While Loops
============================================================

Create these functions:

def move():
    ...

def jump():
    ...

def run_course():
    ...

The run_course() function should control the complete course.

The robot should continue moving until the course is finished.
"""

def move():
    print("Move forward")


def jump():
    print("Jump!")


def run_course():
    position = 0

    while position < 6:
        move()

        hurdle = position % 2 == 1

        if hurdle:
            jump()

        position += 1


run_course()


"""
============================================================
TASK 18 — Variable Hurdle Heights
Difficulty: ⭐⭐⭐⭐⭐
Topic: Variables + Conditions + Functions
============================================================

Create:

max_jump_height = 3

Create a variable representing the height of a hurdle:

obstacle_height

The robot can jump over the hurdle if its height is 3 or less.

If the robot can jump, print:

Jump!

Otherwise, print:

Too high!
"""

max_jump_height = 3
obstacle_height = int(input("Enter obstacle height: "))

if obstacle_height <= max_jump_height:
    print("Jump!")
else:
    print("Too high!")


"""
============================================================
TASK 19 — Multiple Hurdles
Difficulty: ⭐⭐⭐⭐⭐
Topic: Lists + While Loops + Conditions
============================================================

Use the following list:

hurdles = [2, 1, 4, 3, 2, 5]

The robot can jump over hurdles up to height 3.

Go through every hurdle and:

- Print the current hurdle height.
- Print "Jump!" if the robot can jump over it.
- Print "Too high!" if the hurdle is too high.

Use a while loop.
"""

hurdles = [2, 1, 4, 3, 2, 5]
max_jump_height = 3

index = 0

while index < len(hurdles):
    current_hurdle = hurdles[index]

    print("Hurdle:", current_hurdle)

    if current_hurdle <= max_jump_height:
        print("Jump!")
    else:
        print("Too high!")

    index += 1


"""
============================================================
TASK 20 — Hurdles Course
Difficulty: ⭐⭐⭐⭐⭐⭐
Topic: Functions + While Loops + Lists + Conditions
============================================================

Create a complete hurdles program.

Use:

hurdles = [1, 3, 2, 5, 2, 1, 4]

The robot can jump over hurdles up to:

max_jump_height = 3

Create these functions:

def move():
    ...

def jump(height):
    ...

def run_course():
    ...

The run_course() function should:

1. Go through every hurdle.
2. Display the current hurdle height.
3. Decide whether the robot can jump over it.
4. Call the appropriate function.
5. Continue until the entire course is completed.

Example output:

Approaching hurdle: 1
Jumping over hurdle!

Approaching hurdle: 3
Jumping over hurdle!

Approaching hurdle: 5
Hurdle is too high!

...

At the end, print:

Course completed!

Requirements:

- Use functions.
- Use a while loop.
- Use the hurdles list.
- Use max_jump_height.
- Check every hurdle individually.
- Do not manually write separate code for every hurdle.
"""

hurdles = [1, 3, 2, 5, 2, 1, 4]
max_jump_height = 3


def move():
    print("Moving forward")


def jump(height):
    print("Jumping over hurdle of height", height)


def run_course():
    index = 0

    while index < len(hurdles):
        current_hurdle = hurdles[index]

        print("Approaching hurdle:", current_hurdle)

        move()

        if current_hurdle <= max_jump_height:
            jump(current_hurdle)
        else:
            print("Hurdle is too high!")

        index += 1

    print("Course completed!")


run_course()