# Day 7: Hangman

| | |
|---|---|
| Learning Day | 9 |
| Course Day | Angela Yu Day 7 |
| Topic | Guided project, list indexing by position |
| Status | Completed |

Honestly, after yesterday I thought this was gonna be a breeze. Boy was I wrong. Building a full game with actual moving parts proved that I still make dumb logic errors pretty easily. But hey, we got there in the end.

---

## TODO-1 & TODO-2: Smooth Start, Dumb Error

Picking the random word with `random.choice()` and getting input via `.lower()` was super easy. But when I tried to generate the blanks, I passed `chosen_word` directly into `range()` instead of using its length. Python instantly screamed `TypeError` at me because you can't pass a string straight into `range()`. Quick facepalm moment, fixed it by wrapping it with `len()`, and appended `"_"` to the list properly.

---

## TODO-3: The Nightmare (Where I Spent 80% of My Time)

This is where everything went downhill. TODO-3 was an absolute brick wall and ate almost all of my time today.

I needed to check if the guessed letter was in the word and replace the exact `_` in my `blanks` list. My first instinct was a simple `for letter in chosen_word:` loop, but that only gave me the letters themselves—not their positions. I had zero idea how to tell Python to change the element in `blanks` at that exact spot.

After trying random stuff and getting syntax errors for like 40 minutes, I gave up and turned to Google:

* *"python iterate over string with index"*
* *"python replace item in list at position"*

That's when I learned about combining `range(len())` with index access. Once it clicked, I was able to check the character at each position index and update `blanks[position]` whenever it matched `guess`.

### Dumb bugs I made along the way:

* **The duplicate letter bug:** For words like "aardvark", my first attempt only replaced the first 'a' it found instead of all of them. Using the index loop fixed that.
* **Overwriting my own variable:** At one point I used `" ".join(blanks)` to print the hidden word nicely, but I assigned it back to `chosen_word`. Boom. My original secret word got completely wiped out and replaced by a string of blanks. Spent a good 30 minutes wondering why my loop stopped matching letters after the first round.

---

## Finishing the Game Loop

Once TODO-3 was finally working, the rest was actually pretty chill:

* Set `lives = 6`.
* Wrapped everything inside a `while not end_of_game:` loop.
* Checked for the win condition using `if "_" not in blanks` and loss with `if lives == 0`.

---

## Final Thoughts

TODO-3 completely fried my brain today, but honestly, struggling through it, breaking my code, and googling the index trick taught me way more about list indexing than reading theory ever could. On to Day 8!
