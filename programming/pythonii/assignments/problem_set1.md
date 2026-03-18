## Question 1: ORF --> Bundling your Python I solution into a function

A DNA string is called an open reading frame (ORF) if it begins with 'ATG', ends with 'TGA', 'TAG', or 'TAA', and has a length that is a multiple of 3. ORFs are interesting because they can encode proteins.

**1.** Write a function called ORFadviser(DNA) that takes a user-defined string called DNA as input and works as follows:
- The function returns the string 'This is an ORF.' if the input string satisfies all three of the conditions required of ORFs
- Otherwise, if the first three symbols are not 'ATG', the function returns the string 'The first three bases are not ATG.'
- Otherwise, if the string does not end with 'TGA', 'TAG', or 'TAA', the function returns the string 'The last three bases are not a stop codon.'
- Otherwise, the function returns the string 'The string is not of the correct length.'
- **Use the following test cases for your code:**
  
  A. "ATGAAATTTTGA" <-- this should pass (start codon separated by a unit of 3 from a stop codon)

  B. "AAATGTGA" <-- this should also pass (it doesn't start with a start codon, but one is present and it is divisible by a unit of 3 from a stop codon since they are side by side)

  C. "TGATTTTAA" <--- this should not pass (no start codon)

  D. Include a couple of other test cases that should pass and fail in your code and explain them. **Trying to break your own code with test cases that are increasingly challenging is a crucial aspect of creating robust logic and code!**
  
   
**2.** Use the provided dictionary to translate it into amino acids.
Note: this is a question that is recycled from an earlier module but asks you to bundle your code solution (that has if/elif/else conditions) into a function format that will work with any sequence. AS part of your solution, you should use a for loop turn the following sequence (with introns removed, as you did in Intro to Python I) into a list of codons:  5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'. You should end up with a list that prints ["ATC","GAT", etc].

**You can reuse your codon-splitting loop from Python I Module 3, Question 3 inside of this solution. Remember: Good code often gets reused so it is worth it to comment it well!**
