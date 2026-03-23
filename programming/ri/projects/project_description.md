# Capstone report for 1-credit UMaine course participants

* In addition to the regular assignment questions, credit-seeking participants will also complete five additional questions that correspond to each of the five modules of the course.
* **Dataset: JAXMouse_GeneExpression_Simulated.csv**. This single dataset threads through all 10 modules across both courses (5 in RI, 5 in RII). It is a simulated but realistic RNA-seq-style dataset inspired by publicly available mouse tissue gene expression data from GEO.

**Module 1: Using the JAXMouse_GeneExpression_Simulated.csv dataset:**
1.	Read the dataset into R using read.csv(). Use at least four inspection functions (e.g., head(), str(), summary(), dim(), nrow(), ncol(), names()) to characterize the data. In a Markdown chunk, describe what each function revealed. What are the dimensions of this dataset? What data types are present?
2.	Identify which columns should be factors and convert them. What is the difference between a character column and a factor? Why does it matter in biological data?
3.	Use tapply() to compute the mean Expression value for each Tissue type. Interpret the result: does any tissue appear to have systematically higher or lower expression? This will be revisited formally in RII Module 4.
4.	UMaine project milestone: Save a cleaned version of the dataset (factors converted, column names verified) as **"JAXMouse_clean.csv"** using write.csv(). This file will be the input for all subsequent UG credit questions.

**Module 2: Using your JAXMouse_clean.csv dataset (saved in Module 1):**
1.	Write a function called summarize_gene that takes a gene name (character string) as input, subsets the JAXMouse dataset to that gene, and returns a named vector containing the mean, median, and standard deviation of the Expression values for that gene across all samples. Test your function on at least three different genes.
2.	Use sapply() or lapply() to apply your summarize_gene function to the first 10 unique genes in the dataset. Store the result and inspect its structure. What class of object does sapply return in this case?
3.	Write a function called flag_outlier that takes a numeric vector and returns TRUE if any value is more than 3 standard deviations from the mean (a common QC criterion in genomics), and FALSE otherwise. Apply this function using sapply across all genes. How many genes have at least one outlier sample?
4.	UMaine project milestone: Produce a summary table (data frame) with one row per gene containing: gene name, mean expression, SD, and whether it is flagged as an outlier. Save this as **"JAXMouse_gene_summary.csv".**

**Module 3: Using JAXMouse_clean.csv:**
1.	There are samples in this dataset flagged as QC_pass == FALSE. Using Boolean slicing (not a package function), create two new data frames: one containing only QC-passing samples, and one containing only failed samples. How many samples failed QC? What Tissue type had the highest QC failure rate? Report this with tapply().
2.	Using only the QC-passing samples, check whether any Expression values are missing. Write a single line of code that counts the total number of NAs in the dataset. Then write code to identify which genes have any missing values. Remove rows with missing expression values and document your decision in a Markdown chunk.
3.	Slice out all Brain tissue samples from the Control group only. Compute the mean expression per gene in this subset using tapply(). Which gene has the highest mean expression in brain control samples? Which has the most variable expression (highest SD)?
4.	UMaine project milestone: Save the final clean, QC-filtered dataset (no failed QC, no missing Expression) as **"JAXMouse_QCpass.csv".** This is the dataset that will be used for all visualization and statistical analysis in Modules 4, 5, and R II.

**Module 4: Using JAXMouse_QCpass.csv:**
1.	For each of the three Tissue types, create a boxplot of Expression values (using base R). Display all three tissue types on the SAME plot (use the formula interface: boxplot(Expression ~ Tissue, ...)). Color each tissue differently. Do the three tissues appear to have different expression distributions?
2.	Create a histogram of Expression values for Brain tissue only. Does the distribution appear normal? In a Markdown chunk, explain why normality matters. Note: you will test this assumption formally in R II Module 4 so a general understanding is sufficient for now!
3.	Using tapply(), compute the mean and standard deviation of Expression for each combination of Tissue and Treatment (a 3x2 table). Display the results. Which Tissue x Treatment combination has the highest mean expression? Which has the greatest variability?
4.	UMaine project milestone: Save your Module 4 base R plots to a PDF file using pdf() and dev.off(). Name it "JAXMouse_baseR_plots.pdf". In R II Module 3, you will recreate these same plots using ggplot2 for a side-by-side quality comparison.

**Module 5: Using JAXMouse_QCpass.csv:**
1.	Compute descriptive statistics (mean, median, SD, IQR) for Expression values grouped by Tissue and by Treatment separately. Present these as a formatted table using data.frame().
2.	This dataset was designed to contain a Simpson's Paradox. BatchID is a confounding variable. Compare the mean Expression of Control vs. Treated samples: (a) overall (ignoring batch), (b) within Batch1 only, and (c) within Batch2 only. Do the conclusions change depending on whether you account for batch? Explain what this tells you about the danger of ignoring confounders in biological data.
3.	Write a summary paragraph (in a Markdown chunk, not R code) describing what you have learned about this dataset across Modules 1–5. What are its strengths and limitations? What biological questions remain unanswered? What would you do next? (This narrative will be extended in R II.)
4.	UMaine project milestone: Produce a single, well-formatted Quarto/RMarkdown report that compiles all five Module UG credit answers into one document titled "JAXMouse_RI_Analysis_LastnameFirstInitial.html". This is the R I component of your semester project.







