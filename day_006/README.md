# Day 6: Functions

| | |
|---|---|
| Learning Day | 8 |
| Course Day | Angela Yu Day 6 |
| Topic | Functions, while versus for, break |
| Status | Completed |

I started on reeborg.ca and went through all the exercises there. It was great for understanding because everything is shown visually, so I got through it fast. Still, I did not feel like I had really understood it, so I did 20 more practice tasks.

The first five tasks were easy because we had already covered that in the lesson. On task 6 I got stuck a bit on range() because I did not immediately get that the last number is not included. I looked at a few examples on Google and solved it.

Task 7 was the first one that gave me real trouble, because I did not know how to keep the sum through the whole for loop. I googled "python sum numbers in for loop" and saw the trick with total = 0 and total += number. After that it was clear how it works.

Task 8 was fine once I remembered the % operator. At first I thought about using range with a step, but since the point was to practice if, I googled "python check even number" and saw that you use number % 2 == 0.

Task 9 was already fairly tricky. I knew how to check the password, but I did not know how to break out of the loop when the user gets it right. I looked up "python break for loop" and worked out that I need break. After that I had a problem where access denied printed even when the password was correct, so I had to figure out how to fix it. That is where I saw for else for the first time, and it took me a while to understand why it works.

Task 10 was my first serious problem with a while loop. I forgot to change the number inside the loop and made an infinite loop. The program kept printing the same number. I googled "python while infinite loop" and realised I need number += 1.

Task 11 confused me because I first put the wrong condition in the while. I thought about when the loop should stop and then worked out that it should run while the answer is not "no", so !=. I only checked the difference between == and != on Google and solved it.

Task 12 was harder because I had to combine while and if. I set the loop condition wrong at first, so the program did not behave the way it should. Then I wrote down for myself "repeat while guess is not secret_number", and from that I got to while guess != secret_number. After that I just added the if for try again.

Task 13 gave me trouble because of the position variable. I knew what the robot had to do, but I did not immediately know where to put position += 1. I first put it in the wrong place and got the wrong order. Then I walked through the loop step by step and worked out that I have to handle the current position first and only then move to the next one.

Task 14 was simple once I tested concrete numbers. I first wrote < instead of <=, but then I tried height 3 and saw that the robot should be able to jump it. So I changed the condition to <=.

Task 15 was harder because it was the first time I combined a list, while and an index. I knew I had to start from 0, but I did not know how to take the current element out of the list. I googled "python while loop through list" and saw the trick with hurdles[index]. Then I forgot index += 1 again and made an infinite loop, so I understood why it matters.

Task 16 was the hardest because it pulled together everything we had done. First I made the list and the while loop, then I added the height check, and only then the functions. At one point I wanted to use for because it felt easier, but I went back to while because that was the point of the exercise. I also needed some googling about passing an argument into a function, and worked out that I can pass current_hurdle into jump(). In the end I solved it piece by piece and tested each piece separately until it worked.
