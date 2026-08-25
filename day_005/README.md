# Day 5

Two parts today, git and loops.

## Git

I forced a merge conflict twice on purpose and resolved it. Some of it was familiar because I had practised the basic commands a few days earlier and saw them visually, but I still did not understand it fully going in.

I made `merge_vezba.txt` and changed it on two sides. I worked out where a conflict actually comes from, how to resolve it, why git inserts those `<<<<<<<` and `>>>>>>>` lines, and why `checkout` matters, because it decides which version of the files you are looking at. There is no special command for resolving, you just edit the file and commit it like any other change. After the first round I still was not sure I had understood it, so I did the whole thing a second time. Useful detail: PyCharm shows a `Merging main` bar on its own and offers to accept or reject.

## Loops

For loops went fast, I have done them before. Same with finding the largest number in a list.

FizzBuzz slowed me down a bit. I knew I needed `%` and that the whole thing is about remainders, so I played with the if branches until it came out right. Good to refresh it.

The Password Generator was the interesting one. I spent a lot of time on for loops and range. I knew straight away that I needed to start with an empty password and fill it from inside the loop, but it kept repeating characters, so I tried different ways to fix that. I knew `random.choice` had to go inside the loop, and once it clicked, it clicked: for every letter, symbol and number it picks at random from the list above and adds it to the password as many times as the user asked for.

Then the hard version. I needed `shuffle` and I deliberately did not use AI for it, I went to Google and found it myself. Then I saw my password was coming out as a list, so I looked up how to turn it into a plain string and that is `.join`. I had known that one too and forgotten it.

Most of this is stuff I half know already. I am not in the habit of coding, so going through it from the start suits me. Best day so far.

Tomorrow: Day 6, Functions and Karel, and this time lesson by lesson instead of jumping to the project.
