# Day 12: Number Guessing Game

**Course Day:** 12  
**Learning Day:** 14  
**Topic:** Scope, local versus global, return instead of global  
**Status:** Completed

Today was about scope. The idea itself was not new to me. I had run into it while debugging earlier exercises and worked out roughly how it behaves, but I did not know it had a name.

What I did not have before is the reason why `global` is almost never the answer. A function that changes something outside itself does it invisibly. Whoever reads the call sees nothing, and that kind of bug takes the longest to find. I had already written one of those in Blackjack, where `sum_score` modifies the hand it is given.

I finished all the small exercises for this lesson, including the prime number checker. The Number Guessing Game project is not done. That is the first thing tomorrow.

## Number Guessing Game

The project is finished. The computer picks a number between 1 and 100, the player chooses easy or hard, which gives ten or five attempts, and after every guess the program says whether the guess was too high or too low.

Where I got stuck was changing the number of remaining attempts inside a function without reaching for a global variable. What unblocked me was seeing that the function should take the value in, work it out, and return it, and that the caller then overwrites its own old value with what came back. The same shape appears twice in this file, once for the difficulty and once for the check.

Three times in this project a function returned a value and I forgot to catch it. `set_difficulty()` was the last one, and by then I had already made the same mistake with `input()` and with `deal_card()` in Blackjack. A returned value exists only if you assign it to something.

### Known limitations

There is no input validation. If the player types a letter instead of a number, the program stops with a ValueError.

There is no option to play again. The script has to be started manually for a new game.

The difficulty is not validated either. Anything that is not `easy` silently gives the hard level.
