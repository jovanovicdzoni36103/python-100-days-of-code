# Day 10: Calculator

| | |
|---|---|
| Learning Day | 12 |
| Course Day | Angela Yu Day 10 |
| Topic | Functions with outputs, return, a dictionary of functions |
| Status | Completed |

Today was about `return`. I thought I already knew what it does, and it turned out I only knew half of it. `return` hands back whatever value stands after it. If that is `7 + 3`, the function gives back an int. If it is a comparison, the function gives back `True` or `False`, because the comparison itself is already a boolean. `return` does not decide anything on its own, it just passes the value on.

That mattered in the Leap Year exercise. I first wrote the check as an `if` that returned `True` and an `else` that returned `False`. Then I saw that the condition was already `True` or `False` before the `if` even ran, so the `if/else` was turning True into True and False into False and adding nothing. Four lines became one.

My condition also worked only because Python evaluates `and` before `or`. It was correct, but it relied on a rule I had not written down anywhere. I added brackets so the intention is visible instead of implied.

## Calculator project

The first part was the easy one: four functions, and a dictionary with "+", "-", "*" and "/" as the keys. The value stored in the dictionary is the function itself, `add` and not `add()`, because `add` is a value and `add()` is a call.

After that I spent most of the time on the main part and kept getting the indentation wrong. It took me a while to see that everything I was writing had to sit inside one `calculator()` function.

The `while` loop held me up the longest. In the end I understood that the answer to "do you want to continue" has to be caught in a variable, `choice`, and compared there. A value you do not catch does not exist, which is the same lesson as `return`.

At the end `calculator()` is called both inside itself and outside it, so the program always continues. The only difference is which number becomes `num1`, the previous result or a fresh one the user types.

The logo from `art.py` was the last piece. I did not know the command for importing from another file. I got a worked example with different content and applied it here.

## Known limitations

The program does not validate input. If the operator is not one of the four keys, the dictionary lookup fails. If the second value is empty or not a number, `float()` fails. The task did not ask for validation, so it is not there.
