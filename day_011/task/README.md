# Day 011 The Blackjack Capstone Project

A command line Blackjack game against the computer. House rules: the deck is unlimited, Jack, Queen and King count as 10, and the Ace counts as 11 or 1.

The program is built from three functions. `deal_card()` returns one random card. `sum_score(hand)` returns the score of a hand and applies the Ace rule. `compare_scores(user_hand, bot_hand)` returns the result as text.

The hardest part was `sum_score`. It combines a `while` loop, a list and the Ace rule all at once, and I had to take it apart before I could write it. First I made it return the plain sum. Then I added the Ace rule: while the score is over 21 and there is still an 11 in the hand, replace one 11 with a 1 and add the score up again. That last step is the one that matters. Without recalculating the score inside the loop the condition never changes and the loop never ends.

Functions themselves were not new to me. What was new was seeing why `deal_card()` returns one card and not two. At the start of the game I call it twice, and later, every time the player asks for another card, I call it once. If it dealt two cards it would only be usable at the start. I had practised the same shape earlier in the Reeborg exercises with move and jump.

In `compare_scores` I check for Blackjack before I check for a bust. That order is safe, because Blackjack is exactly 21 and a bust is over 21, so the two can never both be true.

## Known limitations

PyCharm reports three warnings of the type "shadows name from outer scope". The program runs correctly and meets every requirement, but the warnings are real and they point at variable scope, which is the topic of the next lesson. I left them in on purpose and will come back to them.

The game plays a single round and then ends. There is no option to play again, and the input is not validated.
