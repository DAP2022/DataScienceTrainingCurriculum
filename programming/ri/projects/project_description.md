# Capstone report for 1-credit UMaine course participants

* In addition to the regular assignment questions, credit-seeking participants will also complete five additional questions that correspond to each of the five modules of the course.
* **Dataset: JAXMouse_GeneExpression_Simulated.csv**. This simulated dataset resembles RNA-seq-style mouse tissue gene expression data and is inspired by publicly available gene expression datasets. You will use the same dataset throughout Introduction to R I and Introduction to R II.

The capstone is designed to build on skills you develop during the course. Each module builds on earlier work, and you will gradually produce a cleaned dataset, summary tables, visualizations, and a final report.

**A note about hints:** Some questions include suggested functions or intermediate steps. These hints mostly came from the first cohort from UMaine to take the course, and I am very grateful to them. These hints are intended to help guide your thinking, particularly when a problem requires combining several concepts. You are welcome to develop alternative solutions using techniques covered in the course.

For questions that ask you to interpret results, provide a brief explanation in a Markdown chunk. You do not need to write lengthy responses; a few thoughtful sentences are generally sufficient. 

**Module 1: Using the JAXMouse_GeneExpression_Simulated.csv dataset:**
_**Goal:**_ Import a data set, explore its structure, understand data types, and perform basic calculations. 

1.	Read the dataset into R using **read.csv()**. Assign it to a variable called **jaxmouse**. Use at least four inspection functions (e.g., head(), str(), summary(), dim(), nrow(), ncol(), names()) to characterize the data. In a Markdown chunk, describe what each function revealed.
In a _Markdown chunk:_ What are the dimensions of this dataset (that is: how big is it)? What data types are present?
2.	Identify at least three columns that represent categorical information. Convert these to factors using factor() and, perhaps, level. Verify your conversions using str() and class() on these columns.
In a _Markdown chunk:_  What is the difference between a character column and a factor? Why might factors be useful when analysing biological data?
3.	Use unique() to identify the tissue types represented in the dataset. Use tapply() to compute the mean Expression value for each Tissue type. Remember that tapply() requires three main arguments: the values to summarize, the groups, and the function to apply. Identify which tissue has the highest and lowest average expression.
In a _Markdown chunk:_ Interpret the result. This will be revisited formally in RII Module 4 when we conduct a formal statistical test.
4.	UMaine project milestone: save this dataframe as **"JAXMouse_clean.csv"** using write.csv(). *Note: If you are interested, you could save this with the formatting/cleaning that you did (that is: you could save it while preserving Factors etc) using saveRDS(name_manipulated_DF, "Path_to_save.RDS") and then reading it back into R with the readRDS("Path_to_save.rds") command.* 

**Module 2: Using the JAXMouse_GeneExpression_Simulated.csv dataset:**
_**Goal: **_ Write simple functions and use them to summarize gene expression.

1.	You have already used functions such as mean(), median(), sd(). Now you will combine them into your own functions! Exciting, no?
   * Choose one gene from the dataset using unique(jaxmouse$Gene). Using Boolean slicing, create a dataframe containing only observations for that gene. Calculate the mean, median, and standard deviation of its Expression values, excluding missing values. Write a function called **summarize_gene** that takes a gene name as input, subsets the JAXMouse dataset to that gene, and returns a named vector containing the mean, median, and standard deviation of the Expression values for that gene across all samples. Test your function on at least three different genes. Hint: First get the calculations working for one gene outside a function. Then move that code into your function and replace the specific gene name with an input argument.
2.	Rather than calling your function separately for every gene, you can use sapply()! Use sapply() to apply your summarize_gene function to the first **5** unique genes in the dataset. Hint: you may want to use unique() here.  Store the result and inspect its structure.
In a _Markdown chunk:_ What class of object does sapply return in this case?
3.	We will write a function that checks whether a numeric vector contains any such observations.
- Choose one gene and calculate the mean and standard deviation of its expression values.
- For each expression value, calculate its absolute distance from the mean using abs().
- Use a logical comparison to identify values more than three standard deviations from the mean.
- Use any() to determine whether at least one value meets this criterion.
- Combine these steps into a function called flag_outlier() that accepts a numeric vector and returns a single TRUE or FALSE.
- Test your function on one or two genes.
- Use split() to group the Expression values by Gene. Apply flag_outlier() to these groups using sapply().
- Use sum() to count how many genes were flagged as containing at least one potential outlier.
Hint: The argument to split() should be the numeric values you want to analyze, grouped by the gene names.
_In a Markdown chunk:_ How many genes were flagged? Does an observation more than three standard deviations from its mean necessarily indicate an error? 
4.	UMaine project milestone: Create a dataframe containing one row per gene, with the following columns: Gene, Mean_Expression, SD_Expression, Has_Outlier. You have already calculated most of the information needed for this table in the previous questions. Hint: You can use data.frame() to combine your gene names, summary statistics, and outlier flags. Save the table as **JAXMouse_gene_summary.csv.**

**Module 3: Using the JAXMouse_GeneExpression_Simulated.csv dataset:**
_Goal:_ Filter observations, identify missing values, and create a cleaned dataset for subsequent analysis.

1.	There are samples in this dataset flagged as having failed Quality Control. The QC_pass column is a Boolean Logic with TRUE and FALSE.
- First, use table(jaxmouse$QC_pass) to determine how many observations passed and failed QC. This will help you assess your function below. 
- Using Boolean slicing with [rows,columns], create two new data frames: one containing only QC-passing samples (variables should be named qc_pass_df), and one containing only failed samples (variable should be named qc_fail_df). Determine how many samples failed QC.
-  using nrow() confirm that these qc_pass_df and qc_fail_df add up to the total number of rows in the original dataset. 
-  Using tapply() with a logical vector that identifies failed QC observations and jaxmouse$Tissue, count failed the failed observations within each tissue. Which tissue type had the highest QC number of failures? 
2.	Using only the QC-passing samples:
- check whether any qc_pass_df$Expression values are missing. You will use **anyNA()** to do this.
- Write a single line of code that **counts **the total number of NAs in qc_pass_df$Expression (hint: **sum(is.na(...))**).
- Use tapply() and is.na() to count the missing expression values for each gene. Which genes contain missing observations?
- Using Boolean slicing, create a new dataframe that retains only QC_passing observations with non-missing Expression values. Use nrow() and anyNA() to verify that your expression data have been cleaned.
  _In a Markdown chunk:_ explain why it is important to consider missing data before conducting statistical analysis. 
3.	Now that we have cleaned the dataset, we want to examine a specific subset: Slice out all Brain tissue samples from the Control group only (Remember that & means AND).
 - Compute the mean expression per gene in this subset using tapply(). Which gene has the highest mean expression in brain control samples?
 - Do the same thing but for sd. Which has the most variable expression (highest SD)?
 - Use max() or sort() to identify the gene with the highest mean expression and the gene with the highest standard deviation (there might be more than 1 if they tissue expressions are tied). 
4.	UMaine project milestone: Save the final clean, QC-filtered dataset (no failed QC, no missing Expression) as **"JAXMouse_QCpass.csv".** This is the dataset that will be used for all visualization and statistical analysis in Modules 4, 5, and R II.

**Module 4: Using JAXMouse_QCpass.csv:**
_Goal: _Create basic visualizations using base R and describe patterns in the data.
1.	For each of the three Tissue types, create a boxplot of Expression values (using base R). Display all three tissue types on the SAME plot (use the formula interface: boxplot(Expression ~ Tissue, ...)). Color each tissue differently. Add a descriptive title, axis label, and different colors for the three tissues. Do the three tissues appear to have different expression distributions?
2.	Create a histogram of Expression values for Brain tissue only (use Boolean slicing to select observations from Brain tissue). Does the distribution appear normal? In a Markdown chunk, explain why normality matters. Note: you will test this assumption formally in R II Module 4 so a general understanding is sufficient for now!
3.	So far, you have examined tissues separately. Now you will examine the combination of two categorical variables. Use table() to determine how many observations belong to each Tissue x Treatment combination. Using tapply(), compute the mean and standard deviation of Expression for each combination of Tissue and Treatment (a 3x2 table). Display the results. Which Tissue x Treatment combination has the highest mean expression? Repeat the calculation using sd(). Which has the greatest variability?
4.	UMaine project milestone: Save your Module 4 base R plots to a PDF file using pdf() and dev.off(). Name it "JAXMouse_baseR_plots.pdf". In R II Module 3, you will recreate these same plots using ggplot2 for a side-by-side quality comparison.

**Module 5: Using JAXMouse_QCpass.csv:**
_Goal:_ Summarize data, recognize how confounding variables affect conclusions, and integrate findings into a scientific report.
1.	Use tapply() to compute descriptive statistics (mean, median, SD, IQR) for Expression values grouped by Tissue and by Treatment separately. Present these as a formatted table using data.frame(). Your table should have one row per tissue.
2.	This dataset was designed to contain a Simpson's Paradox. BatchID is a confounding variable. Compare the mean Expression of Control vs. Treated samples: (a) overall (ignoring batch), (b) within Batch1 only, and (c) within Batch2 only. Do the conclusions change depending on whether you account for batch? Explain what this tells you about the danger of ignoring confounders in biological data.
3.	Write a summary paragraph (in a Markdown chunk, not R code) describing what you have learned about this dataset across Modules 1–5. What are its strengths and limitations? What biological questions remain unanswered? What would you do next? (This narrative will be extended in R II.)
4.	UMaine project milestone: Produce a single, well-formatted Quarto/RMarkdown report that compiles all five Module UG credit answers into one document titled "JAXMouse_RI_Analysis_LastnameFirstInitial.html". *You can either copy-and-paste into this document from your 5 PS OR you can use include in a Markdown chunk. Both of these options will have some troubleshooting*. This is the R I component of your semester project.







