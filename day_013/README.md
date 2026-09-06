# Day 13: Debugging

| | |
|---|---|
| Learning Day | 15 |
| Course Day | Angela Yu Day 13 |
| Topic | Debugging, breakpoints, stepping through code, watching variables |
| Status | Completed |

This day has no project of its own. The lesson is a set of drills, and the one that mattered was run against the Blackjack program from day_011, so there is no new script in this folder.

## What debugging actually is

Reading the code and guessing is not debugging. Debugging is stopping the program while it runs and looking at the real values it holds at that moment. The guess and the reality are often different, and the point is to find where they stop agreeing.

## Breakpoint

A breakpoint is a mark on a line, the red dot in the PyCharm gutter, that tells the program to stop before it runs that line. It changes nothing about the code. A breakpoint only works if the program is started with Debug, the bug icon next to the green Run arrow. Running the file with plain Run ignores every breakpoint in the project.

## The Debugger panel

When execution stops, the Debugger panel opens at the bottom. The Variables list shows every name that exists in the current frame and what it holds right now. A name that has not been assigned yet is simply not in the list, which is itself information.

## Step Over

Step Over, F8, runs the current line and stops on the next one in the same function. Unlike Step Into it does not descend into a function call, so it is the right tool when you want to watch one function's own variables change line by line.

## The drill on sum_score

The line to stop on was total = sum(hand) inside sum_score. Stopping there shows hand already filled and total not yet existing, because the debugger stops before the line runs. One Step Over executes the assignment and total appears in the Variables list with the score of that hand.

Repeating that through the Ace loop below it is what makes the rule visible. While the score is over 21 and an 11 is still in the hand, one 11 becomes a 1 and the score is recalculated. Seeing that happen in the panel is the difference between believing the loop terminates and watching it terminate.
