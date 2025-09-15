### Question 1:

In the following question (repeated below for your convenience), I want you to take previous answer to this question and: 
- Bundle the function (derived in Module 1 assignment) into a module and call it from a new cell in your ipynb (This should look like the example that we did in class).**

An "Open Reading Frame" provides a heuristic for a potential gene. Here is a definition on wikipedia: https://en.wikipedia.org/wiki/Open_reading_frameLinks to an external site. We will use our sequence and use conditional statements to apply general rules to the sequence to identify any open reading frames. Remember that this sequence has known introns so you will want to remove those as well (we did this as part of your Module 1 assignment):

5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'    

A. Is there a start codon which is the sequence "ATG"?    

B. Is there a stop codon (any of the following: "TGA", "TAA", TAG") present    

C. Is the number of nucleotides between any start and any stop codon divisible by 3? 

If these conditions are met, print out "there is a possible ORF in this sequence". If the conditions are not met, print out "There is no possible reading frame in this sequence". 

## Question 2: 
Note: This is a summative question about understanding code, tweaking it modestly, and explaining both the code and your improvement(s). You will recycle other people's code A LOT in the wild! Use the MCMC program discussed as a base to answer the following: I have written a terribly inefficient program that takes an original 4 nucleotide string and mutates it according to certain rules over a specified number of steps (approximately 1,000,000). At certain step numbers (1,100,1000, 10000) the program prints out what the 4 nucleotides have mutated into. Pick one of the options (a, b, or something from group c) to add to the MCMC code and write a paragraph explaining what the code is doing. 

You often want to be able to 'dip' into the simulation at certain time points and sample what the state of the 4 nucleotide string is at that point. In order to accomplish that, add in a counter that tracks the replication cycle and prints out both the cycle number and what the mutated four nucleotide sequence is at that time point. I have hard coded in four time points (1,100,1000,10000) but you want the user to be able to specify what time points are to be sampled so it needs to be passed in as an argument. You should ask your user for input when the function is called and have the user specify the sampling step numbers.
Add in a feature that keeps track of when a mutation event happened, where in the four sequences it happened and what the mutation was. This only needs to have a simple print statement that identifies these things to the user (maybe at the end of the program?)
Add in one of the following features of your choosing:

•    Better encapsulation of the function by breaking it up into smaller functions that are called from within the main function. Compare the time that your program takes with better 'encapsulation' versus the original. Explain any difference in time.  
•    Replace the while loop with for loop(s) since while loops tend to be inefficient. Compare the time that your program takes between the while and for loops. If there is or is not improvement in time, suggest a reason. 
•     Allow user to specify as large of a nucleotide sequence as they want – instead of just 4 nucleotides, users could specify 8 or 1000 or whatever length that they want. 
•    You may have another idea to make this function more optimal - just include it in your comments/explanation so I know what it is. 

## Question 3:

Solve the Fibonacci sequence using recursion (see Module_2A). 

## Question 4:

1. rewrite the following to make it "stateless": 

x=0
#x has state because we are setting it to be 0 and it is being modified depending on 
#where it is in the program. 
print(x)
for i in range(10):
    print(x, "becomes..." )
    x=x+i
    print(x, "Go through the loop again and the value of x has changed!")
print(x)

Assignment 3 will continue with higher level function conversions. 

