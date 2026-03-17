##Please hand in a Jupyter notebook named LastName_FirstInitial_Mod3.ipynb with at least two parts for each question: 

1. A markdown chunk that explains the logic of your answer. If you get stuck, you can hand-in pseudocode that includes a breakdown of the logic of how you are trying to solve the problem along with some pieces of code. 

2. A python coding chunk that has the code for your answer (with any comments). 

-----------------------------------
**What this assignment tests**
   - **For loops** — iteration over sequences and file lines
   - **File I/O** — open, read, write, close
   - **String methods** — .strip(), .split(), slicing on real file content
------------------------------------
## PLEASE SUBMIT FOR YOUR DAY 3 Completion activity: 

## Question 1.  Parse a FASTA file and write exon/intron files
 - Open the file **Module3_Example.txt** from the data folder.
 - The first line is a FASTA header (starts with >) — strip it so you are left with only the DNA sequence, which is the same running sequence from Module 1. **5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'**

Write a program that:
 - Reads the sequence from the file **Module3_Example.txt**. This should not be hard-coded into your code, it should read from a file.
 - Splits it into coding and non-coding regions using the same positions from Module 1
 - Writes the **exon sequence** to **one file** and the **intronic sequence** to a **separate file**

You should be able to have a flexible program that works with any sequence provided by a user but you can assume that the user knows the positions (locations) where the intron/exons are located. You will need to use: open(), file methods, .strip(), slicing, close()


## Question 2: Adaptor Trimming
The following contains 5 DNA sequences, one per line. You will need to copy and paste these sequences into one plain text file in the same directory as your Jupyter notebooks so that you can open the file in your Jupyter notebook.
   

ATTCGATTATAAGCTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT
ATTCGATTATAAGCATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC
ATTCGATTATAAGCACTATCGATGATCTAGCTACGATCGTAGCTGTA
ATTCGATTATAAGCACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTCA

Each sequence starts with the same 14 base pair fragment (ATTCGAT at is a sequencing adapter that needs to be removed. Write a program to do two things: 

1.    Trim this adapter using slicing
2.    Write all five of the cleaned (Trimmed) sequences to one single new file, one cleaned sequence per line. You will use a for loop to do this.
3.    Print the length of the trimmed sequences to the screen.

## Question 3: Split sequence into codons using a for loop
Using a for loop turn the following sequence (it can be hard coded into your cell) into a list of codons (this is the same sequence as in previous questions): 
5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'
You should end up with a list that prints [“ATC”,”GAT”,etc.]

*Note: this problem will appear in Module 5 where you will solve it using regex instead - you can compare which approach you find more readable!
