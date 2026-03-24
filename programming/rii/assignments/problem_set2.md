Please hand in an .rmd file in the format: **lastname_firstinitial_day2.qmd.** Include markdown chunks with information about the question and, if appropriate, a general outline of your approach to solving it. Also use comments in your R coding chunks. Use a blank qmd notebook (it should not include the default chunks that are automatically rendered when you create a new .qmd file).

-------------------------------

## Use built in data set iris to tackle this question.

- Is this data 'tidy'? Why or why not? How might you demonstrate that it follows the conventions of "tidy" data? Demonstrate that it follows (or violates) the three rules of tidy data in a Markdown chunk, with supporting code.
- We want to conduct a selective breeding experiment using only the individuals with the largest 2 Petal.Lengths from each species. Create a tibble called "largestPetalSize" that contains the 6 individuals that fulfill this criteria. What do you notice about the output and what does this suggest about how tied values are resolved?
- Compute the mean Sepal.Length for each iris species using group_by() and summarize().
- Compute mean Sepal.Length for each iris species using **tapply()**. Compare the output to the results using group_by that you calculate above. Are the results identical? Which syntax do you find more readable?
- Add a new column to this dataframe that is the area of the petals. We will make some approximations and claim that petals are exactly rectangular shapes so that area is simply Petal.Length*Petal.Width.
- Finally, we want to graph out a boxplot of only the smallest 10 Petal.Lengths of each species. We will repeat this command in ggplot2 in Module 3.

## Question 2: Tidy Thinking with the Bumpus Dataset
1.	Load the Bumpus dataset and convert it to a tibble. Is it tidy? Identify any columns that might need reshaping for a ggplot2 visualization.
2.	Use dplyr to recreate your tapply() result from R I Module 3 Q2: mean and SD of a numeric trait, grouped by sex AND survival. Write both the base R and the dplyr versions side by side in your .qmd. Which is more readable? Which would be easier to extend if you added a third grouping variable?
