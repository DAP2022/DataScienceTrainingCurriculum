## Question 1: ORF --> Bundling your Python I solution into a function

A DNA string is called an open reading frame (ORF) if it begins with 'ATG', ends with 'TGA', 'TAG', or 'TAA', and has a length that is a multiple of 3. ORFs are interesting because they can encode proteins.

**1.** Write a function called ORFadviser(DNA) that takes a user-defined string called DNA as input and works as follows:
- Is there a start codon which is the sequence "ATG"?
- Is there a stop codon (any of the following: "TGA", "TAA", TAG") present
- Is the number of nucleotides between any start and any stop codon divisible by 3 **and is the stop codon AFTER the start codon**?
If these conditions are met, print out "there is a possible ORF in this sequence". If the conditions are not met, print out a specific message that identifies which condition was not met, for example "There is no possible reading frame in this sequence because there was no start codon". 
- **Use the following test cases for your code:**
  
  A. "ATGAAATTTTGA" <-- this should pass (start codon separated by a unit of 3 from a stop codon)

  B. "AAATGTGA" <-- this should also pass (it doesn't start with a start codon, but one is present and it is divisible by a unit of 3 from a stop codon since they are side by side)

  C. "TGATTTTAA" <--- this should not pass (no start codon)

  D. "atgaaataa"<--- this is lowercase, but otherwise fulfills the criteria.

  E. Include a couple of other test cases that should pass and fail in your code and explain them. **Trying to break your own code with test cases that are increasingly challenging is a crucial aspect of creating robust logic and code!**
  
   
**2.** Use the provided dictionary to translate it into amino acids.
Note: this is a question that is recycled from an earlier module but asks you to bundle your code solution (that has if/elif/else conditions) into a function format that will work with any sequence. AS part of your solution, you should use a for loop turn the following sequence (with introns removed, as you did in Intro to Python I) into a list of codons:  5’- ATCGATCGATCGATCGACTGACTAATCATAGCTATGCATGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTAACATCGATCGATATCGATGCATCGACTAGTACTAT-3'. You should end up with a list that prints ["ATC","GAT", etc].

**You can reuse your codon-splitting loop from Python I Module 3, Question 3 inside of this solution. Remember: Good code often gets reused so it is worth it to comment it well!**
