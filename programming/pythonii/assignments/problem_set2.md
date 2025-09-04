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

Solve the Fibonacci sequence using recursion (see Module_2A). 

## Question 3:

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

