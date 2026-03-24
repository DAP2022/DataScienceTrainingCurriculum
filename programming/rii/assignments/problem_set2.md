Please hand in an .rmd file in the format: **lastname_firstinitial_day2.qmd.** Include markdown chunks with information about the question and, if appropriate, a general outline of your approach to solving it. Also use comments in your R coding chunks. Use a blank qmd notebook (it should not include the default chunks that are automatically rendered when you create a new .qmd file).

-------------------------------

## Question 1: Use built in data set iris to tackle this question.

- Is this data 'tidy'? Why or why not? How might you demonstrate that it follows the conventions of "tidy" data? Demonstrate that it follows (or violates) the three rules of tidy data in a Markdown chunk, with supporting code.
- We want to conduct a selective breeding experiment using only the individuals with the largest 2 Petal.Lengths from each species. Create a tibble called "largestPetalSize" that contains the 6 individuals that fulfill this criteria. What do you notice about the output and what does this suggest about how tied values are resolved?
- Compute the mean Sepal.Length for each iris species using group_by() and summarize().
- Compute mean Sepal.Length for each iris species using **tapply()**. Compare the output to the results using group_by that you calculate above. Are the results identical? Which syntax do you find more readable?
- Add a new column to this dataframe that is the area of the petals. We will make some approximations and claim that petals are exactly rectangular shapes so that area is simply Petal.Length*Petal.Width.
- Finally, we want to graph out a boxplot of only the smallest 10 Petal.Lengths of each species. We will repeat this command in ggplot2 in Module 3.

## Question 2: Tidy Thinking with the Bumpus Dataset
1.	Load the Bumpus dataset and convert it to a tibble. Is it tidy? Identify any columns that might need reshaping for a ggplot2 visualization.
2.	Use dplyr to recreate your tapply() result from R I Module 3 Q2: mean and SD of a numeric trait, grouped by sex AND survival. Write both the base R and the dplyr versions side by side in your .qmd. Which is more readable? Which would be easier to extend if you added a third grouping variable?


## Question 3: Rediscovering the Bumpus Dataset with ggplot2
This question directly builds on R I Module 4. Retrieve the same numeric trait you analyzed to answer that question.

------
(Here is the question from RI, Module 4 to refresh your memory): Choose ONE numeric trait from the Bumpus dataset (e.g., total length, wing chord, weight, head width, humerus length). Use the same trait throughout this question.

- Using two different plot types, visually assess whether your chosen variable appears normally distributed. Which plot type do you find more informative and why? (Hint: a histogram AND one other type are expected.)
- Create a boxplot of your chosen variable grouped by BOTH sex AND survival simultaneously (four groups: female survived, female died, male survived, male died). Describe in a Markdown chunk what the boxplot suggests about sex differences and survival differences in this trait.
- Create a mosaic plot showing the proportion of female vs. male birds that survived vs. died. Describe what conditional probability the mosaic plot is communicating. Does sex appear to be associated with survival?

--------
- Recreate your R I Module 4 histogram using ggplot2 (geom_histogram()). Add a meaningful binwidth, fill color, and theme. Compare it to your base R version; describe at least two improvements the ggplot2 version offers.
- Recreate your grouped boxplot (sex × survival) using ggplot2. Use fill = to color by sex. Add a title, axis labels, and flip coordinates if appropriate for readability. Superimpose the raw data points using geom_jitter() with low alpha. What does showing the raw data add to the boxplot?
- Recreate the mosaic plot as a stacked proportional bar chart using geom_bar(position = "fill"). Add a horizontal line at y = 0.5 using geom_hline() to make the 50/50 reference visible. Does this ggplot2 version communicate the same information more or less clearly than the base R mosaic plot?
- Direct comparison: Write a 3–5 sentence critique in Markdown comparing the two approaches on: code readability, visual quality, and ease of modification.

## Question 4: msleep — A Full ggplot2 Workflow
- Use the msleep dataset (we used it in R2, Module 1).

- Create a scatterplot of total sleep time vs. body weight, colored by vore. Use a log10 scale on the x-axis (scale_x_log10()). Add geom_smooth(method = "lm") per group. Do heavier animals sleep more or less?
- Create a faceted histogram (facet_wrap(~ vore)) of brain weight (log-transformed). Which diet groups show the most variable brain sizes?
