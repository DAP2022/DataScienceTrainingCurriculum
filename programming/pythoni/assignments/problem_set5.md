## Please hand in a Jupyter notebook named LastName_FirstInitial_Mod5.ipynb with at least two parts for each question: 

1. A markdown chunk that explains the logic of your answer.

2. A python coding chunk that has the code for your answer (with any comments). 

-----------------------------------
What this assignment tests
- import re — your first module import (the same mechanism used in Python II for NumPy, Pandas, and your own modules)
- Regex pattern syntax: ., \d, ^, $, *, +, ?, [], ()
- Pattern matching vs. string methods — recognizing when each is the right tool
-----------------------------------

## PLEASE SUBMIT FOR YOUR DAY 5 Completion activity: 

## Question 1:
We worked through the first four of the REGEX questions using the following: 

accessions = ["Xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37d"]

Covered in class — make sure you understand these:
- Contain the number 5
- Contain the letter d or e
- Contain d and e in that specific order, but not necessarily adjacent
- Contain d and e with exactly one letter between them

Please complete the remaining four questions (their solutions will look similar to the ones we did in class).
- Contain both d and e in any order
- Start with x or y
- Start with x or y AND end with e
- Contain three or more consecutive digits

## Question 2: 
In Module 3 Question 3 you split the running sequence into codons using a for loop. Now solve the same problem using regex:
- Using a for loop turn the following sequence (it can be hard-coded into your cell) into a list of codons:  5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'. You should end up with a list that prints ["ATC","GAT", etc].
- In 2–3 sentences, compare the for loop approach from Module 3 with the regex approach. Which is more readable? Which would be easier to modify if codons were 4 bases long instead of 3?
