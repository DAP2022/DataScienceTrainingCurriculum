# Capstone report for 1-credit UMaine course participants

* In addition to the regular assignment questions, credit-seeking participants will also complete five additional questions that correspond to each of the five modules of the course.
* **Datasets:
1. **JAXMouse_GeneExpression_Simulated.csv**. This single dataset threads through all 10 modules across both courses (5 in RI, 5 in RII). It is a simulated but realistic RNA-seq-style dataset inspired by publicly available mouse tissue gene expression data from GEO.
2. **JAXMouse_QCpass.csv**. This was created in Module 3 of Intro to RI. **_You can also find it in the datasets folder on GitHub if you didn't manage to create it._**
3. **JAXMouse_gene_test_results.csv**. An instructor-provided file containing gene-level results from statistical comparisons between Control and Treated observations.
* Throughout this course, you will build on your earlier work by learning to manipulate data with the tidyverse, create more sophisticated visualizations, perform statistical tests, and fit simple statistical models.
* Some questions include suggested functions or intermediate steps. These are intended to help guide your thinking, particularly when a problem requires combining several concepts. You may develop alternative solutions using techniques covered in the course.
* Provide brief explanations in Markdown chunks when requested. Focus on interpreting your results rather than simply describing the R commands.
  
## Module 1: Which Genes are most Variable?
- Using JAXMouse_QCpass.csv (this was created in Module 3 of Intro to RI)
- _Goal: Use grouped calculations to investigate differences in gene expression among genes._
### Question 1: Summarizing gene expression
- Import JAXMouse_QCpass.csv and inspect its structure.
- Using aggregate() or tapply(), calculate the mean Expression for each gene.
- Repeat the calculation to obtain the standard deviation of expression for each gene.
- Identify the five genes with the highest mean expression and the five genes with the highest standard deviation. You can use sort() or order() to help.
- Are any genes present in both lists?

### Question 2: Visualizing mean expression and variability
- Create a dataframe containing one row per gene with its name, mean expression, and standard deviation.
- Use base R plot() to create a scatterplot with mean expression on the x-axis and standard deviation on the y-axis.
- Label the five most variable genes using text(). Add an informative title and axis labels.
- In a Markdown chunk: Does variation in gene expression tend to increase with mean expression? Are highly expressed genes necessarily the most variable genes? Suggest one reason why expression might differ among observations.

**Project milestone:** Save your plot as JAXMouse_mean_variance_baseR.pdf using pdf() and dev.off().

## Module 2: Identifying Genes for Further Investigation
- Using JAXMouse_QCpass.csv
- _Goal: Use the tidyverse to identify genes that differ most in average expression between Control and Treated observations._
### Question 1: Summarizing expression by treatment
- Load the dplyr package and import JAXMouse_QCpass.csv.
- Use group_by() to group the data by Gene and Treatment.Use summarise() to calculate mean expression for each Gene × Treatment combination. Inspect the resulting table. Does every gene have a mean for both Control and Treated observations?

### Question 2: Finding candidate genes
To compare Control and Treated expression for each gene, it will be helpful to have one row per gene, with separate columns for mean Control and mean Treated expression. The pivot_wider() function from the tidyr package can accomplish this. You may use the following code to get started:
```{r}
library(dplyr)
library(tidyr)

gene_means <- jaxmouse |>
  group_by(Gene, Treatment) |>
  summarise(
    Mean_Expression = mean(Expression, na.rm = TRUE),
    .groups = "drop"
  )

gene_wide <- gene_means |>
  pivot_wider(
    names_from = Treatment,
    values_from = Mean_Expression
  )
```
- Run the code above, modifying the dataframe name if necessary. Inspect gene_wide using head().
- Create a new column containing the difference between the Treated and Control means: Mean_Treated - Mean_Control (Hint: The example above will initially produce columns named Control and Treated. You can use those names directly in your calculation.)
- Use abs() to calculate the absolute difference between the two means. Use arrange() and desc() to order the genes from largest to smallest absolute difference.Identify the ten genes with the largest differences.
- In a Markdown chunk: What does a large difference between the treatment-group means suggest? Does it necessarily mean the difference is statistically significant? Explain briefly.

**Project milestone: Save your ten candidate genes as JAXMouse_top10_DE_candidates.csv.** Note: These are candidate genes for further investigation, not genes that have yet been demonstrated to be differentially expressed.

## Module 3: Visualizing Gene Expression with ggplot2
- Using JAXMouse_QCpass.csv:
- _Goal: Use ggplot2 to create and interpret a more informative figure than the one you produced using base R._
### Question 1: Comparing tissues and treatments
- Import JAXMouse_QCpass.csv and load ggplot2.
- Create a boxplot using geom_boxplot() with Tissue on the x-axis and Expression on the y-axis. Use facet_wrap(~ Treatment) to display Control and Treated observations in separate panels. Color the boxes by Tissue using the fill aesthetic. Add a descriptive title, axis labels, and a theme. If the figure remains readable, try adding individual observations using geom_jitter() with a small point size and low transparency (alpha).

### Question 2: Interpreting the visualization
In a Markdown chunk, answer the following:
- Which tissue appears to have the highest median expression?
- Does the relationship between Treatment and Expression appear similar across all three tissues?
- What additional information does the faceted ggplot2 figure communicate compared with your earlier base R boxplot?

**Project milestone: Save your figure as JAXMouse_ggplot_boxplot.png using ggsave().**

## Module 4: Hypothesis Testing and Multiple Comparisons
- _Goal: Understand how statistical evidence differs from the magnitude of an observed difference, why testing many genes increases the risk of false positives, and how to communicate these results with a volcano plot._
- Using JAXMouse_QCpass.csv and your **JAXMouse_gene_test_results.csv** (download from GitHub in datasets for RII):

### Question 1: Testing one gene
- **Choose one gene** from your list of 10 candidate genes identified in Module 2.
- Use filter() to create a dataframe containing only observations for that gene. Use group_by() and summarise() to calculate the mean, standard deviation, and number of expression observations in the Control and Treated groups.
- Create a boxplot comparing expression between the two treatment groups (Control versus Treatment).
- Use t.test() to compare the expression values between Control and Treated groups. For this exercise, use the default Welch two-sample t-test. Examine the output and identify: The estimated mean expression for each group. The test statistic. The p-value. The confidence interval for the difference between group means.
_ In a Markdown chunk:_ Complete the four steps in Hypothesis Testing:
- State the null and alternative hypotheses.
- Identify the appropirate statistical test and **its assumptions**
- Is there evidence of a difference in expression between the two groups at a significance level of 0.05?
- Explain your conclusion in two or three sentences.

### Question 2: What changes when we test many genes?
In Question 1, you performed a single hypothesis test. However, genomic studies often test hundreds or thousands of genes. For this question, use the file **JAXMouse_gene_test_results.csv** in your datasets. This table contains one row per gene, including mean Control expression, mean Treated expression, and the raw p-value from a treatment comparison. 
- Import the table into R and inspect it using head() and str(). Use nrow() to determine how many genes were tested.
- Use a logical comparison to identify genes with raw p-values below 0.05. Use sum() to count how many genes meet this criterion.
- Use p.adjust() with method = "bonferroni" to calculate adjusted p-values for all genes in the table. Add these adjusted p-values as a new column. Count how many genes have adjusted p-values below 0.05. Compare the number of significant genes before and after correction by filling in the following table:

| Measure     | Number of Genes |
| ----------- | ----------- |
| Total Genes Tested     |        |
| Raw p-values below 0.05   |        |
| Bonferroni_adjusted p-values below 0.05|     |


- _In a Markdown chunk:_ Why does testing many genes increase the risk of false positives? What happens to the number of statistically significant genes when you apply the Bonferroni correction?
Hint: If you conduct 100 independent hypothesis tests and all null hypotheses are true, how many p-values below 0.05 would you expect on average? Why is multiple testing correction essential when testing many genes simultaneously? What would you expect if we tested the top 20 genes with alpha=0.05? (This is a foundational concept in genomics: bulk RNA-seq studies test thousands of genes at once.)

### Question 3: Creating a volcano plot
A volcano plot is commonly used to visualize gene expression results. It combines information about the magnitude of a difference between groups and the statistical evidence for that difference. You will create a volcano plot using the instructor-provided gene-level results and the Bonferroni-adjusted p-values you calculated in Question 2.
##### Part A: Preparing your data. 
- Identify the columns containing mean expression for the Control and Treated groups (Mean_Control, Mean_Treated, raw_p) in your results dataframe.
- For this exercise, assuming the expression means are on a positive, untransformed scale appropriate for ratios, calculate the log2 fold change using: log2(Mean_Treated / Mean_Control).** Add this column to your dataframe.**
- Calculate the negative base-10 logarithm of each raw p-value using: -log10(raw_p). **Add this column to your dataframe.**
- Create a new logical column identifying genes with Bonferroni-adjusted p-values below 0.05. Hint: Your dataframe should now contain one row per gene, including a log2 fold change, a transformed p-value, and an indicator of statistical significance.
#### Part B: Creating the plot. 
- Use ggplot() and geom_point() to create a scatterplot with: x-axis: log2 fold change, y-axis: -log10(raw p-value). Color: whether the gene remains significant after Bonferroni correction. Add a horizontal reference line corresponding to a raw p-value of 0.05 using geom_hline(). Add a vertical reference line at log2 fold change = 0 using geom_vline(). Add a meaningful title, axis labels, and a clean theme.
- Save the figure as JAXMouse_volcano.png using ggsave().
- _ In a Markdown chunk: Do more genes show higher mean expression in Control or Treated observations? How can you tell from the volcano plot? Identify the genes with the three largest absolute log2 fold changes and the genes with the three smallest raw p-values. Are they the same genes, and are they ranked in the same order? Why might genes with similar fold changes have different p-values? Consider the relationship between the magnitude of a difference, variability, and sample size. Many genes in this dataset show lower mean expression in Treated observations. Does this necessarily mean that treatment caused their expression to decrease? What other factors might contribute to this pattern?
Hint: Recall your investigation of Simpson's paradox and batch effects in Introduction to R I.

Note: The horizontal line represents a raw p-value threshold, while the point colors represent significance after multiple-testing correction. These are deliberately different criteria.

### Question 4: Consider what you have learned from the hypothesis tests, adjusted p-values, and volcano plot.
Answer the following questions in a Markdown chunk.
- Why is a statistically significant result not necessarily a biologically important result?
- Can a gene have a large fold change but a relatively high p-value? What might explain this?
- Can a gene have a small fold change but a very low p-value? What might explain this?
- Why is multiple-testing correction especially important in genomics?
- What additional information would you need before concluding that treatment causes a change in gene expression?
Project milestone: Save your volcano plot and retain your table containing raw and Bonferroni-adjusted p-values. Include both in your final Quarto report.

## Module 5: Does Accounting for Other Variables Change Our Conclusions?
- _Goal: Use multiple linear regression to investigate whether an apparent treatment-associated difference changes when other variables are included in the model. _
- Using JAXMouse_QCpass.csv
### Question 1: Choosing a gene
- Return to the gene-level test results from Module 4.
- Identify the gene with the smallest raw p-value.
- Use filter() to create a dataframe containing only observations for that gene.
- Use str() to check the data types of Expression, Treatment, Tissue, Sex, Age_weeks, and BatchID. Convert categorical predictors to factors where necessary.
- Create a boxplot comparing expression between Control and Treated observations for your selected gene.
### Question 2: Building two regression models: 
You will compare a model that considers Treatment alone with a model that also includes other variables. Use the following two model formulas. You do not need to develop the formulas independently.

Model 1: Treatment only
```{r}
model1 <- lm(
  Expression ~ Treatment,
  data = gene_df
)

# Model 2: Including other predictors

model2 <- lm(
  Expression ~ Treatment + Tissue + Sex + Age_weeks + BatchID,
  data = gene_df
)
```
- Replace gene_df with the name of the dataframe containing your selected gene, if necessary.
- Run Model 1 and use summary(model1) to examine the results.
- Identify the estimated coefficient and p-value for Treatment.
- Run Model 2 and use summary(model2) to examine the results.
- Identify the estimated coefficient and p-value for Treatment in Model 2.
- Record the R-squared value for each model.
- Complete the following comparison table:

  | Result    | Treatment Only | Multiple Predictors |
| ----------- | ----------- | ----------- |
| Treatment coefficient     |        |    |
| Treatment p-value  |        |    |
| R-Squared|     |  |

### Question 3: Understanding Model Limits
- Use plot(model2) to display the diagnostic plots for your second model.
- Focus on the residuals-versus-fitted plot and the normal QQ plot.
- Look for unusual patterns or observations that appear inconsistent with the fitted model.
- Use summary(model2) to identify other predictors that appear associated with expression. Remember that categorical predictors may have multiple coefficients representing comparisons with reference groups.
- In a Markdown chunk, answer the following:
    - Did the estimated treatment effect change when you included other predictors?
    - Why might the simple model and the multiple-predictor model give different results?
    - What do the residual plots suggest about the fit of your model?
    - Can you conclude that treatment caused changes in gene expression? Why or why not?

Note: A change in a coefficient or p-value is informative even if neither result is statistically significant. These models provide an introductory illustration of adjusting for other variables, not a complete causal analysis.

Project milestone: Include your model comparison table and interpretation in your final report.
# **FINAL SEMESTER PROJECT DELIVERABLE:** 
Compile your complete analysis from both RI and RII into a single polished Quarto report titled "JAXMouse_FinalReport_LastnameFirstInitial.html". The report should include: 
- (a) an Introduction describing the biological question and dataset;
- (b) all five R I module analyses (data inspection through descriptive statistics);
- (c) all five R II module analyses (tidyverse wrangling, ggplot2 figures, hypothesis tests, ANOVA, regression);
- (d) a Conclusion section synthesizing your findings: does treatment alter gene expression, does this differ by tissue, and what biological story do these data tell?

This final report demonstrates the complete R programming and data analysis workflow: from raw data to reproducible scientific communication, exactly as practiced by computational biologists in research settings. 

