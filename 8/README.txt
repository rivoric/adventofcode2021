     111   0 = 1,2,4,5,6,7 (6)
    2   6  1 = 6,7 (2)
    2   6  2 = 1,6,3,4,5 (5)
    2   6  3 = 1,6,3,7,5 (5)
     333   4 = 2,3,6,7 (4)
    4   7  5 = 1,2,3,7,5 (5)
    4   7  6 = 1,2,3,4,5,7 (6)
    4   7  7 = 1,6,7 (3)
     555   8 = 1,2,3,4,5,6,7 (7)
           9 = 1,2,3,5,6,7 (6)

Take the numbers with 5 segments (2, 3 and 5) and compare with the number 1.
Only 3 has both segments in so if we have a number 1 we can always work out a number 3
Reverse that logic for numbers with 6 segments (0, 6 and 8), only number 6 does not have both segments so we can always work out a number 6

If we don't have a 1 but we have a 4 and a 7, then the two characters common to both give us a 1

If we have a 4 as well then this gives us the ability to work out the other 2 numbers in a similar way.
The two segments that appear in a 4 but not in a 1 (2,3) can be used.
The only appear in the number 5 (for 5 segments)
The don't both appear in the number 0 (for 6 segments)

This gives us the a way of working out all numbers if the line contains either a 1 and a 4 or a 4 and a 7 (or a 4 and either a 1 or 7)
And it lends itself to using sets

length 2
   = 1
length 3
   = 7
length 4
   = 4
length 5
   1 is subset = 3
   L is subset = 5
   else = 2
length 6
   not 1 is subset = 6
   not L is subset = 0
   else = 9
length 7
   = 8

