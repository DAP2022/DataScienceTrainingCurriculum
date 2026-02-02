# Module 1 Assignment:

Hand in a .qmd file saved as “FirstInitialLastname_Day1.qmd” that has BOTH
markdown explanations and coding chunks (with hashed out comments).

## Question 1:
Use an R Markdown chunk (not a coding chunk) to introduce yourself. This doesn't have to be long, but should contain at least one list and one header so you become familiar with how to use Markdown (and how to use the internet/cheatsheets to help you!). As a prompt, you might answer a subset of the following (or anything other similar question): Why do you want to learn R? What is your background? What are your Favourite food or Hobbies? Do you have pets? If so, why are they THE best? Gimme me an enumerated list of the five things that (a) make you happiest, OR (b) top five people you would invite to a dinner party, OR (c) top five books or films that you would recommend.

Let’s say that in our experimental analyses, we are working with three different sets of cells: normal, cells knocked out for geneA (this means they are missing geneA), and cells overexpressing geneA. We have three replicates for each of the three cell types (normal, none, over-expressed). 
Create a vector named samplegroup with nine elements: 3 control (“CTL”) values, 3 knock-out (“KO”) values, and 3 over-expressing (“OE”) values
Turn samplegroup into a factor data structure. 

## Question 2:
Turn the following table into a matrix (You can just use the Weight and Height columns for your matrix):

|Species| Sex | Weight(lbs) |Height(cm)|
|:-------:|:---:|:---:|:---:|
|Gorilla gorilla|M|400|180|
|Gorilla gorilla| F|175|140|
|Pan troglodytes|M|120|150|
|Pan troglodytes|F|85|150|
|Homo sapiens|M|180|178|
|Homo sapiens|F|140|165|
|Orangutan|M|160|137|
|Orangutan|F|82|115|
|Pan paniscus|M|86|78|
|Pan paniscus|F|68|73|

 
# Question 3:
Using the Bumpus_data.csv:
- Read in the Bumpus data set.
- Pick one of the remaining columns and conduct analysis on it using tapply
  (which, recall, is for numeric continuous variables).
  You can use built in functions like sd() or mean() or some other built-in
   function that sparks joy (you can google lists of built-in base R functions,
   but you can also go here: https://www.javatpoint.com/r-built-in-functions).
- Use the R Markdown chunks to explain your analysis (Why did you pick this
 function?
- What is the data type of the column? Was the output what you expected?)
