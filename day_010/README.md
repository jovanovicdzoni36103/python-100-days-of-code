# Day 010 Functions with Outputs

Today was about `return`. I thought I already knew what it does, and it turned out I only knew half of it. `return` hands back whatever value stands after it. If that is `7 + 3`, the function gives back an int. If it is a comparison, the function gives back `True` or `False`, because the comparison itself is already a boolean. `return` does not decide anything on its own, it just passes the value on.

That mattered in the Leap Year exercise. I first wrote the check as an `if` that returned `True` and an `else` that returned `False`. Then I saw that the condition was already `True` or `False` before the `if` even ran, so the `if/else` was turning True into True and False into False and adding nothing. Four lines became one.

My condition also worked only because Python evaluates `and` before `or`. It was correct, but it relied on a rule I had not written down anywhere. I added brackets so the intention is visible instead of implied.

Where I got stuck was seeing that a comparison is a value in its own right. I needed a pointer for that, and after it I carried on.

What is in this folder: functions with outputs, functions that return values, and a docstring used as extra explanation. The Calculator project is not done yet. That is the first thing I do tomorrow, before I start Day 11.