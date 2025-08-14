## Please hand in a Jupyter notebook named LastName_FirstInitial_Mod2.ipynb with at least two parts for each question: 

1. A markdown chunk that explains the logic of your answer.

2. A python coding chunk that has the code for your answer (with any comments). 

-----------------------------------

##Question 1: 

A. open the Module2_Example.txt file, remove the first line of the FASTA file.
If you get stuck, you can hand-in pseudocode that includes a breakdown of the logic of how you are trying to solve the problem
along with some pieces of code. We will discuss expectations for pseudocode in lecture.
The file will now contain only the following sequence (the sequence should be the same as the one from Assignment 1):
5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'
Introns are the noncoding parts of a DNA sequence that are spliced out (removed) from the sequence before it is translated into
a chain of amino acids. In the following sequence, there are two exons and one intron. The first exon runs from the start of 
the sequence to the 63rd character. The second exon runs from the 91st character to the end of the sequence.
(hint: in the following sequence of numbers what would the 3rd character: 0 1 2 3 4). 

B. Write a program that will split the genomic DNA into coding and non-coding (intron) parts and write these to two different
files (a file for exons/coding and a file for the spliced out introns/non-coding). You should be able to have a flexible 
program that works with any sequence provided by a user but you can assume that the user knows the positions (locations) 
where the intron/exons are located. 
