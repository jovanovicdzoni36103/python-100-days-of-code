# Mini Quiz Game

## What this project is about

I wanted to build a simple Python quiz for day 17 of the course, but instead of throwing everything into one single file and making a huge mess, I split the logic into five smaller pieces using object oriented programming principles. The app asks for your name, shows questions one by one in the terminal, tracks your score, and displays your final results along with your game statistics at the very end.

Honestly, it looked super easy on paper, but I tripped up over a few silly mistakes before getting everything to work smoothly.

## Where I got stuck and what gave me trouble

First, I made a mistake in the main quiz class because I tried to pass the starting score and current question index right into the initialization method from the outside. Once the code threw an error, I realized how unnecessary that was. It makes no sense to pass a zero score when someone creates a brand new quiz, so that starting state should just live inside the class itself.

The second thing that completely threw me off was running the script and seeing every single question and answer printed in the terminal before I even typed my name. I was staring at the screen wondering what went wrong. It turns out that as soon as you import data from another file, Python automatically executes that whole file from top to bottom. Since I left some test print statements inside my question data file, they all executed during the import process. I had to strip all helper files completely clean of any leftover print statements.

Then I got annoyed because my method was returning both text and a boolean value together inside parentheses, which printed out looking ugly with brackets and quotes instead of a clean string. On top of all that, right when the quiz finally worked, the program crashed on the very last line because I tried passing a score argument into the player stats function, completely forgetting that the function did not take any outside arguments at all.

## Lessons learned and conclusion

In the end, I polished up the whole codebase so everything runs clean and smooth. The biggest takeaway for me is that helper modules must stay completely free of test prints, and breaking code down into separate files makes finding bugs a hundred times easier than hunting through one massive script.