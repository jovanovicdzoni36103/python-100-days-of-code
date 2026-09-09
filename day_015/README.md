# Day 15: Coffee Machine

## What I built
A coffee machine that takes orders, checks whether it has the ingredients, counts
coins, gives change, deducts resources and keeps track of profit. Seven requirements
from the spec, all working.

## Where I got stuck
I started well with `elif choice in MENU` and thought the rest would be easy. It was
the hardest thing I have done so far.

The worst part was keeping straight which bracket held what: MENU holds a drink, the
drink holds ingredients, and ingredients holds the amount. Three levels deep, and I
kept losing track of whether `item` was the key or the value.

The check function took several tries. I had the comparison backwards, I looped
through the machine stock instead of the recipe, and my `return True` sat inside the
loop so the function quit after the first ingredient. Two of those bugs hid each
other: fixing the return made the program crash on espresso, because espresso has no
milk in its recipe.

Payments were easier. By then I was in the rhythm. Rounding the change to two decimals
still took me a while to get right.

## The autocomplete trap
At one point I pressed tab on a suggestion without reading it:

    resources[item] = order_ingredients[item]

The program ran fine. No error. But instead of subtracting the ingredients, it
overwrote the stock with the recipe amount, so after one latte the machine reported
200ml of water instead of 100ml. A bug that does not crash is harder to catch than
one that does. The tool offered a line that fit the syntax, not a line that solved my
problem.

## Global, again
Adding to profit inside a function threw UnboundLocalError. This is the same scope
problem I hit on Day 12, in a different project, and I did not recognise it. The
function needs `global profit` as its first line to be allowed to change a variable
that lives outside it.

## Known limitations
- Typing text instead of a number when inserting coins crashes the program.
- No way to cancel once the machine starts asking for coins.
- Change is reported as a number, the machine does not work out which coins to return.
