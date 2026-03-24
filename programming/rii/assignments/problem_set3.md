Remember: name your file with the following standard: **LastnameFirstInitial_RII_Module3.qmd**

## Question 1: Rediscovering the Bumpus Dataset with ggplot2

This question directly builds on R I Module 4. Retrieve the same numeric trait you analyzed then.

---------------------
(Here is the question from RI, Module 4 to refresh your memory): 
Choose ONE numeric trait from the Bumpus dataset (e.g., total length, wing chord, weight, head width, humerus length). Use the same trait throughout this question.
1.	Using two different plot types, visually assess whether your chosen variable appears normally distributed. Which plot type do you find more informative and why? (Hint: a histogram AND one other type are expected.)
2.	Create a boxplot of your chosen variable grouped by BOTH sex AND survival simultaneously (four groups: female survived, female died, male survived, male died). Describe in a Markdown chunk what the boxplot suggests about sex differences and survival differences in this trait.
3.	Create a mosaic plot showing the proportion of female vs. male birds that survived vs. died. Describe what conditional probability the mosaic plot is communicating. Does sex appear to be associated with survival?

---------------------

1.	Recreate your R I Module 4 **histogram** using ggplot2 (geom_histogram()). Add a meaningful binwidth, fill color, and theme. Compare it to your base R version; describe _at least two improvements the ggplot2 version offers._
2.	Recreate your grouped boxplot (sex × survival) using ggplot2. Use fill = to color by sex. Add a title, axis labels, and flip coordinates if appropriate for readability. Superimpose the raw data points using geom_jitter() with low alpha. What does showing the raw data add to the boxplot?
3.	Recreate the mosaic plot as a stacked proportional bar chart using geom_bar(position = "fill"). Add a horizontal line at y = 0.5 using geom_hline() to make the 50/50 reference visible. Does this ggplot2 version communicate the same information more or less clearly than the base R mosaic plot?
4.	Direct comparison:  Write a 3–5 sentence critique in Markdown comparing the two approaches on: code readability, visual quality, and ease of modification.

## Question 2: msleep — A Full ggplot2 Workflow
Use the msleep dataset (we used it in R2, Module 1).
1.	Create a scatterplot of total sleep time vs. body weight, colored by vore. Use a log10 scale on the x-axis (scale_x_log10()). Add geom_smooth(method = "lm") per group. Do heavier animals sleep more or less?
2.	Create a faceted histogram (facet_wrap(~ vore)) of brain weight (log-transformed). Which diet groups show the most variable brain sizes?

