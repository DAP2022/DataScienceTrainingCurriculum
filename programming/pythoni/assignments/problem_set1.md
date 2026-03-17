## Please hand in a Jupyter notebook named LastName_FirstInitial_Mod1.ipynb with at least two parts for each question: 

**1. A markdown chunk that explains the logic of your answer.**

**2. A python coding chunk that has the code for your answer (with any comments).**

----------
This assignment includes the following skills: 
 1. **Variable Assignment**: naming and storing variables
 2. **String Slicing**: extracting substrings with [start:stop:by] format
 3. **Concatenation**: joining strings using **+**
Your answers to question 1-4 shjould collectively demonstrate all three of these tools. If you find yourself solving all sections with the same tools, try a different approach on at least one.
----------
## Question 1
For the sequence given below:

 5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'

Introns are the noncoding parts of a DNA sequence that are spliced out (removed) from the sequence before it is translated into a chain of amino acids. In the following sequence, there are two exons and one intron. The first exon runs from the start of the sequence to the 63rd character. The second exon runs from the 91st character to the end of the sequence. *Hint: in the following sequence of numbers: 0 1 2 3 4, what is the 3rd character? It is "2" not "3" because the 1st character is "0".*

1. **Extract the coding sequence**: Write a program that prints out JUST the coding regions of the DNA sequence to the screen (ie. removes the introns). You should use variable assignment, slicing, and concatenation in your answer.
   
2. **Calculate the coding percentage**: Using the results of 1, write a program that will calculate what percentage of the DNA sequence that is coding. You should use variable assignment, and string formatting in your answer.
   
3. **Label exons vs. introns visually**: Write a program that will print out the original genomic DNA sequence coding bases in UPPERCASE letters and the intronic (non-coding) bases in lowercase. Hint: Built-in methods can make solving this problem more straight forward and efficient. 

4. **Store coding and non-coding separately**: Write a program that will split the genomic DNA into coding and non-coding  parts. 

-------------
Note: The exon/intron splitting you've written here will be recycled in Python II Module 1 — where you'll be asked to bundle this exact logic into a reusable function called ORFadviser(). Keep your solution clear and commented; you'll thank yourself later!
