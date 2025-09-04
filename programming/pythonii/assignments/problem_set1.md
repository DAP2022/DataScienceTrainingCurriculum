## Question 1:

A DNA string is called an open reading frame (ORF) if it begins with 'ATG', ends with 'TGA', 'TAG', or 'TAA', and has a length that is a multiple of 3. ORFs are interesting because they can encode proteins.

A. Write a function called ORFadviser(DNA) that takes a user-defined string called DNA as input and works as follows:
•	The function returns the string 'This is an ORF.' if the input string satisfies all three of the conditions required of ORFs
•	Otherwise, if the first three symbols are not 'ATG', the function returns the string 'The first three bases are not ATG.'
•	Otherwise, if the string does not end with 'TGA', 'TAG', or 'TAA', the function returns the string 'The last three bases are not a stop codon.'
•	Otherwise, the function returns the string 'The string is not of the correct length.'
Use the following test case for your code: "ATGAAATTTTGA"
   
B. Use the provided dictionary to translate it into amino acids.
Note: this is a question that is recycled from an earlier module but asks you to bundle your code solution (that has if/elif/else conditions) into a function format that will work with any sequence. 

Using a for loop turn the following sequence (it can be hard-coded into your cell) into a list of codons:  5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'. You should end up with a list that prints ["ATC","GAT", etc].
