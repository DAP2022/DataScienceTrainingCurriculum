Section 1A Question:

A DNA string is called an open reading frame (ORF) if it begins with 'ATG', ends with 'TGA', 'TAG', or 'TAA', and has a length that is a multiple of 3. ORFs are interesting because they can encode proteins.
1. Write a function called ORFadviser(DNA) that takes a USER PROVIDED string called DNA as input and works as follows:

The function returns the string 'This is an ORF.' if the input string satisfies **all three** of the conditions required of ORFs.
Otherwise, if the first three symbols are not 'ATG', the function returns the string 'The first three bases are not ATG.'.
Otherwise, if the string does not end with 'TGA', 'TAG', or 'TAA', the function returns the string 'The last three bases are not a stop codon.'. Otherwise, the function returns the string 'The string is not of the correct length'.

Test case: "ATGAAATTTTGA"

2. Place this function into a module and call it from the module (not the main body of the code)
   
3. Use the provided dictionary to translate it into amino acids.

Section 1B questions:

Question 1: We worked through the first four of the REGEX questions (see Module_1BPOSTclass notebook). Please complete the remaining four questions (their solutions will look similar to the ones we did in class).

Question 2: Use regex to solve the following question:

Using a for loop turn the following sequence (it can be hard-coded into your cell) into a list of codons:  5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'. You should end up with a list that prints ["ATC","GAT", etc].
