## Please hand in a Jupyter notebook named LastName_FirstInitial_Mod2.ipynb with at least two parts for each question: 

1. A markdown chunk that explains the logic of your answer.

2. A python coding chunk that has the code for your answer (with any comments). 

-----------------------------------
Skills you should use in your answers: 
1. **Iterating over a list of tuples using a for loop**
2. **Accessing nested data**: a tuple inside of a tuple!
3. **Pseudocode**: planning before coding. Pseudocode forces you to decompose the problem before you get distracted by syntax. This is the same skill you will use for every complex problem in this course. A good pseudocode answer earns full marks even if the Python isn't perfect yet.
------------------------------------
## Question 1: 
Building on the Pseudocode question in class: We all know that there is degeneracy in the universal genetic code. This means that every amino acid has one or more nucleotide codons. Given a nucleotide string: "ATGGCTTTC", and you want to translate it into amino acids using a list of codons (it is not a list with all the codons, just a subset).
A.	How would you break the string into codons (3 bases each)?
B.	How could you look up each codon in a list that maps codons to amino acids?
C.	Write pseudocode that shows the basic steps.

## Question 2:
You are given the following list of tuples, where each tuple contains a student name and a tuple of three exam scores:
expression_data = [("BRCA2",(0.02,0.03,0.02)),("FOS",(0.01,0.05,0.13)),("A2M",(0.20,0.14,0.05))]

A.	Iterate through this list and print each gene name and its three expression values.

B.	Calculate the mean expression for each gene and print it alongside the gene name.

C.	(Bonus) Build a new list of tuples in the form ("GeneName", mean_expression), sorted from highest to lowest mean.

* You will use this exact dataset again in Python II Module 4 (when we discuss and apply a package called NumPy). There, a 4×4 array will replace this list of tuples, and np.mean(axis=1) will replace your manual average calculation. Notice how much less code that requires!
