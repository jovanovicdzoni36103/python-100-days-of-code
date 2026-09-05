# Day 012 Scope

Today was about scope. The idea itself was not new to me. I had run into it while debugging earlier exercises and worked out roughly how it behaves, but I did not know it had a name.

What I did not have before is the reason why `global` is almost never the answer. A function that changes something outside itself does it invisibly. Whoever reads the call sees nothing, and that kind of bug takes the longest to find. I had already written one of those in Blackjack, where `sum_score` modifies the hand it is given.

I finished all the small exercises for this lesson, including the prime number checker. The Number Guessing Game project is not done. That is the first thing tomorrow.