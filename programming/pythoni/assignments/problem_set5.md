## Please hand in a Jupyter notebook named LastName_FirstInitial_Mod5.ipynb with at least two parts for each question: 

1. A markdown chunk that explains the logic of your answer.

2. A python coding chunk that has the code for your answer (with any comments). 

-----------------------------------

## PLEASE SUBMIT FOR YOUR DAY 5 Completion activity: 

## Question 1:
We worked through the first four of the REGEX questions. Please complete the remaining four questions (their solutions will look similar to the ones we did in class).

## Question 2: 
Use regex to solve the following question:
Using a for loop turn the following sequence (it can be hard-coded into your cell) into a list of codons:  5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'. You should end up with a list that prints ["ATC","GAT", etc].
## Question 3:
Note: This is a summative question about understanding code, tweaking it modestly, and explaining both the code and your improvement(s). You will recycle other people's code A LOT 'in the wild' (also known as: the 'real' world)! Use the **MCMC program discussed in class (and present in the Module5 notebook)** as a base to answer the following: I have written a terribly inefficient program that takes an original 4 nucleotide string and mutates it according to certain rules over a specified number of steps (approximately 1,000,000). At certain step numbers (1,100,1000, 10000) the program prints out what the 4 nucleotides have mutated into. Pick one of the options (a, b, or something from group c) to add to the MCMC code and write a paragraph explaining what the code is doing. 
a. You often want to be able to 'dip' into the simulation at certain time points and sample what the state of the 4 nucleotide string is at that point. In order to accomplish that, add in a counter that tracks the replication cycle and prints out both the cycle number and what the mutated four nucleotide sequence is at that time point. I have hard coded in four time points (1,100,1000,10000) but you want the user to be able to specify what time points are to be sampled so it needs to be passed in as an argument. You should ask your user for input when the function is called and have the user specify the sampling step numbers. 
b. Add in a feature that keeps track of when a mutation event happened, where in the four sequences it happened and what the mutation was. This only needs to have a simple print statement that identifies these things to the user (maybe at the end of the program?)
c. Add in one of the following features of your choosing:
•    Better encapsulation of the function by breaking it up into smaller functions that are called from within the main function. Compare the time that your program takes with better 'encapsulation' versus the original. Explain any difference in time.  
•    Replace the while loop with for loop(s) since while loops tend to be inefficient. Compare the time that your program takes between the while and for loops. If there is or is not improvement in time, suggest a reason. 
•     Allow user to specify as large of a nucleotide sequence as they want – instead of just 4 nucleotides, users could specify 8 or 1000 or whatever length that they want. 
•    You may have another idea to make this function more optimal - just include it in your comments/explanation so I know what it is. 
