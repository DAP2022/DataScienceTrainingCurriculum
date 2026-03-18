# Module 4
What this assignment tests: 
1. **NumPy arrays**: creating, slicing, axis-awareness operations
2. **Pandas DataFrames**: groupby, filtering, plotting with Matplotlib

## Question 1- NumPy
Hint: You should be able to solve it using similar tools to the 10X10 array that we set up in class and manipulated. 

In the following table we have expression values for 5 genes at 4 time points. These are completely made up data. Although, some of the questions can be easily answered by looking at the data, microarray data generally come in much larger tables and if you can figure out the strategy here for a small data set the same code will work for an entire gene chip with LOTS of data! Note: you don't need to make your code robust or able to handle a table of a different size than the simple one given below for your assignment.

|Gene name|	4h|	12h|	24h|	48h|
|:-------:|:---:|:---:|:---:|:---:|
|A2M |	0.20 |	0.14|	0.05	|0.01
|FOS |	0.01|	0.05|	0.13 |	0.16|
|BRCA2 |	0.02|	0.03|	0.03 |	0.02|
|CPOX|	0.05|	0.09|	0.11 |	0.09|

- Create a single NumPy array for the data (4x4) (Note: you will read the values from the above into the array directly, not use a random number generator).
- Find the mean expression value per gene (these are the rows)
- Find the mean expression value per time point (these are the columns)
- Identify which gene has the maximum mean expression value
- sort the gene names by the max expression value and print them to the screen. 
