##Please hand in a Jupyter notebook named LastName_FirstInitial_Mod3.ipynb with at least two parts for each question: 

1. A markdown chunk that explains the logic of your answer.

2. A python coding chunk that has the code for your answer (with any comments). 

-----------------------------------

## PLEASE SUBMIT FOR YOUR DAY 3 Completion activity: 

##Question 1. 

A. Using a for loop turn the following sequence (it can be hard-coded into your cell and it should be the same sequence as for Day 1 and Day 3) into a list of codons:  5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'. You should end up with a list that prints ["ATC","GAT", etc].

B.  An "Open Reading Frame" provides a heuristic for a potential gene. Here is a definition on wikipedia:
https://en.wikipedia.org/wiki/Open_reading_frame
We will use our sequence and use conditional statements to apply general rules to the sequence to identify any
open reading frames. Remember that this sequence has known introns so you will want to remove those as well 
(we did this as part of Module 1B):

5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'
    i. Is there a start codon which is the sequence "ATG"?
    ii. Is there a stop codon (any of the following: "TGA", "TAA", TAG") present
    iii. Is the number of nucleotides between any start and any stop codon divisible by 3? 

If these conditions are met, print out "there is a possible ORF in this sequence". If the conditions are not met, print out
"There is no possible reading frame in this sequence". 

2. The following contains 5 DNA sequences, one per line. You will need to copy and paste these sequences into one plain text
3.  file in the same directory as your Jupyter notebooks so that you can open the file in your Jupyter notebook.
   

ATTCGATTATAAGCTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT
ATTCGATTATAAGCATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC
ATTCGATTATAAGCACTATCGATGATCTAGCTACGATCGTAGCTGTA
ATTCGATTATAAGCACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTCA

Each sequence starts with the same 14 base pair fragment (ATTCGAT at is a sequencing adapter that needs to be removed. 
Write a program to do two things: 

1.    Trim this adapter and using a 'for loop'  write all five of the cleaned sequences to one new file, one cleaned sequence per line.
2.    Print the length of the trimmed sequences to the screen.

