##Please hand in a Jupyter notebook named LastName_FirstInitial_Mod3.ipynb with at least two parts for each question: 

1. A markdown chunk that explains the logic of your answer.

2. A python coding chunk that has the code for your answer (with any comments). 

-----------------------------------

## PLEASE SUBMIT FOR YOUR DAY 3 Completion activity: 

## Question 1. 
Open the Module3_Example.txt file (it is in the data folder), remove the first line of the FASTA file.
If you get stuck, you can hand-in pseudocode that includes a breakdown of the logic of how you are trying to solve the problem along with some pieces of code. We will discuss expectations for pseudocode in lecture.
The file will now contain only the following sequence (the sequence should be the same as the one from Assignment 1 - we will continue to use this particular sequence in subsequent assignments, unless explicitly told otherwise):
## 5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'
Introns are the noncoding parts of a DNA sequence that are spliced out (removed) from the sequence before it is translated into a chain of amino acids. In the following sequence, there are two exons and one intron. The first exon runs from the start of the sequence to the 63rd character. The second exon runs from the 91st character to the end of the sequence. (hint: in the following sequence of numbers what would the 3rd character: 0 1 2 3 4). 

Write a program that will split the genomic DNA into coding and non-coding (intron) parts and __write these to two different files__ (a file for exons/coding and a file for the spliced out introns/non-coding). You should be able to have a flexible program that works with any sequence provided by a user but you can assume that the user knows the positions (locations) where the intron/exons are located. 


## Question 2:
The following contains 5 DNA sequences, one per line. You will need to copy and paste these sequences into one plain text file in the same directory as your Jupyter notebooks so that you can open the file in your Jupyter notebook.
   

ATTCGATTATAAGCTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT
ATTCGATTATAAGCATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC
ATTCGATTATAAGCACTATCGATGATCTAGCTACGATCGTAGCTGTA
ATTCGATTATAAGCACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTCA

Each sequence starts with the same 14 base pair fragment (ATTCGAT at is a sequencing adapter that needs to be removed. Write a program to do two things: 

1.    Trim this adapter and using a 'for loop'  write all five of the cleaned sequences to one new file, one cleaned sequence per line.
2.    Print the length of the trimmed sequences to the screen.

## Question 3:
Using a for loop turn the following sequence (it can be hard coded into your cell) into a list of codons (this is the same sequence as in previous questions): 
5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'
You should end up with a list that prints [“ATC”,”GAT”,etc.]

