Please hand in an .rmd file in the format: lastname_firstinitial_day2.rmd. Include markdown chunks with information about the question and, if appropriate, a general outline of your approach to solving it. Also use comments in your R coding chunks. Use a blank rmd notebook (it should not include the default chunks that are automatically rendered when you create a new .rmd file).

-------------------------------

NB: I failed to mention that you should use the built in data set iris to tackle this question.

Is this data 'tidy'? Why or why not? How might you demonstrate that it follows the conventions of "tidy" data?
We want to do a selective breeding experiment using only the individuals with the largest 2 Petal.Lengths from each species. Create a tibble called "largestPetalSize" that contains the 6 individuals that fulfill this criteria. What do you notice about the output and what does this suggest about how tied values are resolved?
Now, we want to find the mean Sepal.Length of each of the iris species.
We want to add a new column to this dataframe that is the area of the petals. We will make some approximations and claim that petals are exactly rectangular shapes so that area is simply Petal.Length*Petal.Width.
Finally, we want to graph out a boxplot, using ggplot, of only the smallest 10 Petal.Lengths of each species. This should be one command.
