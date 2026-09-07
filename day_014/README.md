# Day 14: Higher Lower Game

## What I built
A guessing game that compares follower counts between two accounts. I built the
comparison logic and a system that keeps the winner and moves it from position B
to position A for the next round.

## Where I got stuck
The hardest part was the difference between raw data and text formatted for the
screen. I kept trying to pull the follower count out of a plain string, instead of
out of the dictionary where the data actually lives.

format_data() builds a string from three fields and never touches follower_count.
So storing its return value meant the dictionary was gone, and with it the number
I needed. The fix was to store the dictionary itself and call format_data() only
at the moment of printing.

## Why while instead of if for duplicate accounts
The course solution checks once, with an if. If random happens to pull the same
account again, the program carries on with the bug. A while loop keeps pulling
until it gets a genuinely different account, and only then lets the game continue.

## Known limitations
- Invalid input (anything other than "a" or "b") counts as a wrong answer instead
  of asking the player to try again.
- If two accounts have the same follower count, "b" is always treated as correct.
- The screen is not cleared between rounds.
