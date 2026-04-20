## Please hand in a Jupyter notebook named LastName_FirstInitial_Mod2.ipynb with at least two parts for each question: 

1. A markdown chunk that explains the logic of your answer.

2. A python coding chunk that has the code for your answer (with any comments). 

-----------------------------------
What this assignment tests
•	if/elif/else — conditional logic and Boolean operators
•	Dictionaries — key:value lookup (the codon table)
•	Combining tools — loops + conditions + file I/O + dictionaries together
Questions 1 and 2 form a pair — Q1 detects the ORF, Q2 translates it. Solve them in order.

-----------------------------------
## Question 1: ORF detection
1.	An “Open Reading Frame” provides a heuristic for a potential gene. Here is the definition on Wikipedia: https://en.wikipedia.org/wiki/Open_reading_frame.
We will use our sequence and use conditional statements to apply general rules to the sequence to identify any open reading frames. Remember that this sequence has known introns so you will want to remove those as well (you already did this in Module 1):
**5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'**

A.	Is there a start codon which is the sequence "ATG"?

B.	Is there a stop codon (any of the following: "TGA", "TAA", TAG") present **and is the stop codon AFTER the start codon**?

C.	Is the number of nucleotides between any start and any stop codon divisible by 3? 

If these conditions are met, print out "there is a possible ORF in this sequence". If the conditions are not met, print out a specific message that identifies which condition was not met, for example "There is no possible reading frame in this sequence because there was no start codon". 
*Note: In Python II you will convert this code into a function called ORFadviser() that returns a different string for each failure mode. If you write descriptive messages now (not just 'No ORF found'), that refactoring will be much easier.*


## Question 2: Codon translation
Use the dictionary given to you in Module4B to __translate the ORF from your sequence in question 1 into a string of Amino Acids__. 
Hint:  To solve this problem easily, you need to first recognize that there are three major components/sub-problems that you have to solve. 
1. You need to split the nucleotide sequence into codons.     
-    we have already learned how to ‘pull out’ parts of strings - now we just need to ‘automate’  process
-    recognize that each codon is three nucleotides long
-    you already solved this step in Module 3, Q3 - feel free to reuse that!
2. Translate each codon into the appropriate amino acid
-    The given dictionary would come in handy here!
-    remember the .get() method
3. Create a protein by adding all the amino acids together

## Question 3: Filtering gene data. You only need to pick one!
Pick any one of the questions (a through e) to answer and submit. **You do not need to do them all**; just complete one and label it so that I know which one you picked! Write your program to work with any file that has the same structure (species, sequence, gene name, expression), not just the specific values in data.csv. Use variables for column indices and thresholds. This is good practice for real data science work.

We created the **“data.csv”** in a previous module that should be in your files. The file contains four columns corresponding to species name, nucleotide sequence, gene name and expression level of gene. There are 6 rows with four different species of Melanogaster indicated.
You will want to make this program work for any file that has the same type of structure as data.csv (that is the first column is species, the second column is sequence, the third columns is name and the fourth column is expression) that it is given so you will likely need if conditions imposed. Hint: remember that the .split () method can use “,” as the criteria for splitting.

a. Print out all the gene names for all genes belong to Drosophila melanogaster OR Drosophila simulans to two different external files (one for melanogaster and one for simulans). You can name them melanogaster and simulans.

b. Print out all the gene names for genes between 90 and 110 bases long (inclusive at both ends so, for example, a gene that was 89 bases long wouldn't be included but that is 90 base pairs long would be include) .

c. Print out all the gene names for the genes whose AT content is less than 0.5 AND whose expression level is greater than n .)

d. Print out the gene names for all genes whose name begins with “k” or “h” EXCEPT those belonging to Drosophila melanogaster.

e. For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65). To a separate file, print the genes whose AT content is greater than 0.5 AND whose expression level is greater than 200. For each gene that meets these criteria, include a line in the file that gives the gene name and the percentage of length.

*Note: In Python II Module 5, you will run SQL queries against a relational database that ask identical questions to (a)–(e) above — SELECT ... WHERE species = '...'. Compare how much shorter the SQL version is. That contrast is the point.*
