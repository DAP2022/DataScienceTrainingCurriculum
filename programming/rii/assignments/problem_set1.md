Please explain your steps. Fully utilize the power of RStudio (Posit) by using Markdown cells AND R chunks (don't just use R chunks with hashed out comments). Use a new rmd file for your assignment and please use a format such as: **Lastname_Firstname_PS1.rmd** so that when I go through and mark/comment, it is straightforward for me to see that it is yours. Thank you!

--------------------------------

## Q1. Using the built-in msleep dataset (available when ggplot2 is loaded)
*We will work through a very similar question in class using the built-in iris dataset. The msleep dataset is included in the ggplot2 package so you will need to load that package in order to access the data set. This will be demonstrated during class*  
- Load the dataset.
- Use at least four inspection functions to characterize it and describe at least three attributes (explain what you choose and why). How is this dataset structurally similar to the Bumpus dataset from R I? How is it different? 
- Using base R slicing and subset(), extract all mammals that are: carnivores, sleep more than 12 hours total per day, and have a known body weight. How many animals meet all three criteria?
-  Use tapply() to calculate mean total sleep time by vore (diet category). Which diet group sleeps the most? Does this surprise you? Offer a biological hypothesis in a Markdown chunk.
-  *You will repeat this anlaysis using dplyr in Module 2*

## Q2. Use the HairEyeColor built-in dataset for basic R to create a mosaic plot. 
- This will be a similar process to what we did in class. Ask and answer, using a graph, a question based on this table.

## Q3:Using the Bumpus dataset:
- Recreate the three visualizations from R I Module 4 (histogram, grouped boxplot, mosaic plot) exactly. These are your baseline.
- Now load ggplot2. Without being taught it yet, use the ggplot2 cheat sheet (find online or in your syllabus) to attempt ONE of the three plots in ggplot2. What was the most confusing aspect of the ggplot2 syntax compared to base R?
-	Save all four plots (three base R + one ggplot2 attempt) to a single PDF. This file will be referenced directly in Module 3 for a quality comparison.
