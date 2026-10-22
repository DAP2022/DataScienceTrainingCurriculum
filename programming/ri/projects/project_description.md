# Capstone report for 1-credit UMaine course participants

* In addition to the regular assignment questions, credit-seeking participants will also complete five additional questions that correspond to each of the five modules of the course.
* **Dataset: JAXMouse_GeneExpression_Simulated.csv**. This simulated dataset resembles RNA-seq-style mouse tissue gene expression data and is inspired by publicly available gene expression datasets. You will use the same dataset throughout Introduction to R I and Introduction to R II.

The capstone is designed to build on skills you develop during the course. Each module builds on earlier work, and you will gradually produce a cleaned dataset, summary tables, visualizations, and a final report.

**A note about hints:** Some questions include suggested functions or intermediate steps. These hints mostly came from the first cohort from UMaine to take the course, and I am very grateful to them. These hints are intended to help guide your thinking, particularly when a problem requires combining several concepts. You are welcome to develop alternative solutions using techniques covered in the course.

For questions that ask you to interpret results, provide a brief explanation in a Markdown chunk. You do not need to write lengthy responses; a few thoughtful sentences are generally sufficient. 

**Module 1: Using the JAXMouse_GeneExpression_Simulated.csv dataset:**
_**Goal:**_ Import a data set, explore its structure, understand data types, and perform basic calculations. 
### Question 1: Importing and inspecting the data
- Read the dataset into R using **read.csv()**.
- Assign it to a variable called **jaxmouse**.
- Use at least four inspection functions (e.g., head(), str(), summary(), dim(), nrow(), ncol(), names()) to characterize the data.
- In a _Markdown chunk:_ Briefly describe the dataset. What information does it contain? Why might factors be useful for analyzing biological data?
### Question 2: Comparing expression among tissues
- Use unique() to identify the tissue types in the dataset.
- Use tapply() to calculate the mean Expression for each Tissue.
- Identify which tissue has the highest and lowest mean expression.
- _In a Markdown chunk:_ Do the tissues appear to differ in average expression? Can we conclude from these means alone that the differences are statistically significant?

**Project milestone: Save your dataframe as JAXMouse_clean.csv using write.csv().**
Hint: Use row.names = FALSE to avoid saving an extra row-number column. Remember that CSV files do not preserve R factor classes. You can convert categorical columns back into factors when you read the file again.

**Module 2: Using the JAXMouse_GeneExpression_Simulated.csv dataset:**
_**Goal: **_ Write a function and use sapply() to summarize expression for several genes.
### Question 1: Writing a gene-summary function
You have already used functions such as mean(), median(), sd(). Now you will combine them into your own function investigating gene expression! Exciting, no? 
- Use unique(jaxmouse$Gene) to identify the different genes represented in the dataset.
- Choose one gene and use Boolean slicing to create a dataframe containing only observations for that gene.
- Calculate the mean and standard deviation of its Expression values using mean() and sd(). Remember to exclude missing values using na.rm = TRUE.
- Write a function called summarize_gene() that takes a gene name as input and returns a named vector containing the mean and standard deviation of expression for that gene.
- **Test your function on three different genes.** (remember that there is a difference between defining a function and actually calling it!) Hint: First get your calculations working for one specific gene. Then move the code into a function and replace the gene name with the function's input argument.
### Question 2: Applying the function to several genes
- Use unique() to create a vector containing the gene names.
- Select the first five genes using [1:5].
- Use sapply() to apply your summarize_gene() function to those five genes.
- Store the result in an object and inspect it using print() and class().
- _In a Markdown chunk:_ What kind of object did sapply() return? Which of the five genes has the highest mean expression? Which has the greatest standard deviation? Hint: You used sapply() in the regular Module 2 assignment. The difference here is that your function returns two summary statistics rather than one number.

**Project milestone: Keep your function and gene-summary results in your Quarto notebook. You will revisit gene-level variation in R II.**

**Module 3: Using the JAXMouse_GeneExpression_Simulated.csv dataset:**
_Goal:_ Use Boolean slicing to identify observations that failed quality control, investigate missing values, and prepare a cleaned dataset.
### Question 1: Identifying observations that failed quality control
The QC_pass column identifies whether each observation passed or failed quality control.
- Use table(jaxmouse$QC_pass) to examine how many observations passed and failed QC.
- Use unique() or str() to check how the TRUE and FALSE values are stored.
- Using Boolean slicing, create two dataframes:

qc_pass_df: observations that passed QC.

qc_fail_df: observations that failed QC.

- Use nrow() to count the observations in each dataframe.
- Verify that these two counts add up to the total number of rows in the original dataset.
- Use table() to count the failed observations in each tissue. Which tissue has the greatest number of failed observations? Hint: You can apply table() directly to the Tissue column of qc_fail_df.
- _In a Markdown chunk:_ How many observations failed QC? Why might it be important to remove failed observations before conducting further analyses?

### Question 2: Identifying missing values
We will now work only with observations that passed QC.
- Use anyNA() to check whether qc_pass_df$Expression contains missing values.
- Use sum(is.na(...)) to count how many Expression values are missing.
- Using Boolean slicing, create a new dataframe that retains only observations with non-missing Expression values.
- Use nrow() to compare the number of observations before and after removing missing Expression values.
- Verify that your cleaned Expression column no longer contains missing values.
- _In a Markdown chunk:_ How many observations were removed because of missing Expression values? Why might missing data cause problems for statistical analyses?

### Question 3: Investigating Brain tissue
Now that your dataset has been cleaned, investigate one particular subset.
- Using Boolean slicing, select observations from Brain tissue in the Control group. Hint: You will need to combine two logical conditions using & (AND).
- Use tapply() to calculate mean expression for each gene within this subset.
- Use sort() or which.max() to identify the gene with the highest mean expression.
- _In a Markdown chunk:_ Which gene has the highest mean expression in Brain tissue under the Control condition? What additional information would you need before interpreting its biological importance?

**Project milestone: Save your cleaned dataframe (QC-passing observations with no missing Expression values) as: JAXMouse_QCpass.csv**. You will use this file for all remaining analyses in Introduction to R I and Introduction to R II.
Note: For this assignment, we are treating each row as a gene-expression observation. Several observations may belong to the same biological sample, so the number of rows should not automatically be interpreted as the number of independent samples.

**Module 4: Using JAXMouse_QCpass.csv:**
_Goal: _Create basic visualizations using base R and describe patterns in the data.
- Use **JAXMouse_QCpass.csv** (created in Module 3) for this module.
### Question 1: Comparing expression among tissues
- Import your cleaned dataset.
- Create a boxplot comparing Expression among the three Tissue types using base R. Hint: You can use the formula interface: boxplot(Expression ~ Tissue, data = ...)
- Display all three tissue types on the same plot. Add a descriptive title, axis labels, and different colors for the tissues.
- _In a Markdown chunk:_ Which tissue has the highest median expression? Do the tissues differ in how variable their expression values are?

### Question 2: Examining the distribution of expression
- Use Boolean slicing to select only Brain tissue observations.
- Create a histogram of their Expression values using hist(). Add a meaningful title and axis labels.
- _In a Markdown chunk:_ Describe the shape of the distribution. Does it appear approximately symmetric, skewed, or multimodal? Does it resemble a normal distribution? Hint: Think back to the histograms you created using the Bumpus dataset in the regular assignment.

### Question 3: Comparing tissues and treatments
In Module 1, you calculated mean expression for each tissue. Now investigate whether the pattern appears to depend on treatment.
- Use table() to count how many observations belong to each combination of Tissue and Treatment.
- Use tapply() to calculate mean expression for each Tissue × Treatment combination. Hint: You can provide two grouping variables to tapply() using list(Tissue, Treatment).
- Display the resulting table. Identify which combination has the highest mean expression.
- _In a Markdown chunk:_ Does the difference between Control and Treated observations appear similar across all three tissues?

**Project milestone: Save your boxplot and histogram in a PDF named JAXMouse_baseR_plots.pdf**, using pdf() and dev.off(). In R II, you will revisit the tissue boxplot using ggplot2 and compare the results.

**Module 5: Using JAXMouse_QCpass.csv:**
_Goal:_ Summarize data, recognize how confounding variables affect conclusions, and integrate findings into a scientific report.
### Question 1: Describing expression by treatment
- Use tapply() to calculate mean Expression for the Control and Treated groups.
- Repeat the calculation using median() and sd().
- Compare the means and standard deviations of the two groups.
- _In a Markdown chunk:_ Which treatment group has the higher average expression? Does one group show greater variability?

### Question 2: Investigating Simpson's paradox
In the regular Module 5 assignment, you investigated Simpson's paradox using a simulated clinical trial. The JAXMouse dataset was also designed to illustrate how a confounding variable can change the interpretation of a comparison. In this dataset, the relevant variable is BatchID.

#### Part A: Ignoring batch
- Use tapply() to calculate mean Expression for Control and Treated observations across the complete cleaned dataset.
- Which group has the higher mean?

#### Part B: Examining the batches separately
- Use Boolean slicing to create a dataframe containing only observations from Batch1.
- Use tapply() to calculate mean Expression for Control and Treated observations within Batch1.
- Repeat the analysis for Batch2.
- Record your results in the following table:

|Group | Mean Control | Mean Treated | Higher Mean |
| -------- | --------- | ----------| -------- |
|All Batches|   |  |   |
|Batch 1    |   |  |   |
|Batch 2   |    |  |   |

  #### Part C: Interpreting the results
  - Compare the overall results with those from the separate batches. Does the apparent relationship between treatment and expression change?
  - Use table() to examine how many Control and Treated observations are represented in each batch.
  - _In a Markdown chunk:_ Explain how the batch composition might influence the overall comparison. Why can ignoring a confounding variable lead to misleading conclusions in biological research? Hint: Think back to the simulated clinical trial you analyzed in the regular Module 5 assignment.

### Question 3: Reflecting on the dataset
Write a short Markdown paragraph (approximately 150–250 words) addressing the following:
- What did you learn about differences in expression among tissues or treatment groups?
- What data quality issues did you encounter, and how did you address them?
- What did your investigation of batch effects teach you about interpreting biological data?
- What is one biological question you would like to investigate further?
You do not need to perform any additional analyses for this question. Focus on interpreting what you have already discovered.

**Project milestone: Compile your five module answers into a single Quarto or R Markdown report titled: JAXMouse_RI_Analysis_LastnameFirstInitial.html**

You may copy code and Markdown explanations from your completed module assignments into a single document. You do not need to use Quarto include directives. Your report should contain your analyses, relevant outputs, figures, and brief scientific interpretations. This report forms the Introduction to R I component of your JAXMouse capstone project. You will extend the analysis in Introduction to R II.

