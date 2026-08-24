# Day 4

Today I built Rock Paper Scissors. So far this was the hardest project in the course.

First I greeted the user and explained that they pick rock, paper or scissors by typing a number, then I took their input. I skipped the ASCII art at that point and left it for the end. Then I used `random` so the computer could pick between 0, 1 and 2, and wrote the if branches for every combination. The number has to be between 0 and 2, anything else counts as invalid input, and the game only starts once the input is valid.

After that I went back and reminded myself what ASCII actually is, found ready made art for rock, paper and scissors on someone's GitHub, dropped it into my file and put the three of them into a list called `ascii_art`, which is what the branches use.

The thing that cost me the most time is not visible in the code, it is about order. I had the three variables holding the art, and further down I had the same three names holding plain words. The words were below the art, so they overwrote it, and the list picked up the words. The program runs top to bottom and the last assignment wins. It is the same rule I learned on day one with the two glasses, but this time there were fifty lines in between so I could not see it happening.

The project took me about 45 minutes. When I read the task I thought it would go easily, and it turned out harder than I expected.