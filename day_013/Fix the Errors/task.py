try:
    age = int(input("How old are you? "))
    if age > 18:
        print(f"You can drive at age {age}.")
    else:
        print("You are not old enough to drive yet.")
except ValueError:
    print("Please enter a valid numerical age.")