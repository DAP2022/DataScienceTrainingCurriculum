# Module 1 Assignment:

Hand in a .qmd file saved as “FirstInitialLastname_Day1.qmd” that has BOTH
markdown explanations and coding chunks (with hashed out comments).

## Question 1:
Use an R Markdown chunk (not a coding chunk) to introduce yourself. This doesn't have to be long, but should contain at least one list and one header so you become familiar with how to use Markdown (and how to use the internet/cheatsheets to help you!). As a prompt, you might answer a subset of the following (or anything other similar question): Why do you want to learn R? What is your background? What are your Favourite food or Hobbies? Do you have pets? If so, why are they THE best? Gimme me an enumerated list of the five things that (a) make you happiest, OR (b) top five people you would invite to a dinner party (living or dead), OR (c) top five books or films that you would recommend, OR (d) if that is too personal, how about five datasets or scientific questions that you find fascinating. 

## Question 2:
We are designing an experiment with three cell line conditions: normal cells, cells knocked out for geneA (missing the gene), and cells overexpressing geneA. We have three biological replicates for each condition.
1.	Create a vector named samplegroup with nine elements: three "CTL" values, three "KO" values, and three "OE" values. Convert samplegroup into a factor. Print both the vector and the factor and explain in a Markdown chunk what changed and why factors matter for downstream analysis.
2.	Now extend your thinking: the Bumpus dataset (Bumpus_data.csv) records whether house sparrows survived a severe winter storm. Read the dataset in. Identify which columns are, or should be treated as, factors and which are continuous numeric variables. Use str() and summary() to support your answer. Explain in a Markdown chunk: what would go wrong if you accidentally treated a factor column as numeric?
3.	Use tapply() to calculate the mean of one numeric column of your choosing, broken down by the survival factor. Explain your choice of column and interpret the result biologically in a Markdown chunk.


## Question 3:
Turn the following table into a matrix (You can just use the Weight and Height columns for your matrix). Answer in Markdown: why can a matrix only hold Weight and Height, but the data frame can hold all columns?

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

 
