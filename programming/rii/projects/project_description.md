# Capstone report for 1-credit UMaine course participants

* In addition to the regular assignment questions, credit-seeking participants will also complete five additional questions that correspond to each of the five modules of the course.
* **Dataset: JAXMouse_GeneExpression_Simulated.csv**. This single dataset threads through all 10 modules across both courses (5 in RI, 5 in RII). It is a simulated but realistic RNA-seq-style dataset inspired by publicly available mouse tissue gene expression data from GEO.
  
## Module 1: Using JAXMouse_QCpass.csv (this was created in Module 3 of Intro to RI):
1.	Review your R I Module 1 tapply() result (mean Expression by Tissue). Repeat this analysis now using base R aggregate() function as well. Do both approaches give the same result? Which do you find more readable and why?
2.	Identify the top 5 most highly expressed genes (highest mean expression across all samples). Identify the 5 most variably expressed genes (highest SD). Are any genes in both lists? What might this mean biologically?
3.	Using base R, create a scatterplot of mean expression (x-axis) vs. SD of expression (y-axis) for each gene. Label the five most variable genes on the plot using text(). This type of "mean-variance" plot is foundational in RNA-seq analysis. Save to your existing **"JAXMouse_baseR_plots.pdf"** by appending a new page.
4.	Undergraduate project milestone: Write a brief Markdown paragraph describing what the mean-variance plot reveals. In R II Module 3, you will recreate this as a polished ggplot2 figure and compare the two versions side by side.
5. Write a brief Markdown paragraph describing what the mean-variance plot reveals. In R II Module 3 (below), you will recreate this as a polished ggplot2 figure and compare the two versions side by side.

## Module 2: Using JAXMouse_QCpass.csv
1.	Is the JAXMouse dataset tidy? Each row should represent one observation of one variable. Evaluate this formally against the three rules of tidy data in a Markdown chunk. (Hint: consider what constitutes a single "observation" in this experiment.)
2.	Use dplyr (group_by + summarize) to compute mean, median, and SD of Expression for each combination of Tissue and Treatment. Arrange the output by descending mean expression. Which Tissue x Treatment combination has the highest mean expression? How does this compare to your base R tapply() result from R I Module 4?
3.	Use filter() and select() to create a clean tibble containing only Brain tissue samples, retaining only the columns: SampleID, Gene, Expression, Treatment, Sex. Pipe this directly into a ggplot2 boxplot of Expression by Treatment. Add a meaningful title, axis labels, and theme.
4.	Using dplyr, identify the top 10 most differentially expressed genes (largest absolute difference in mean expression between Control and Treated) across all tissues. Save this list as **"JAXMouse_top10_DE_candidates.csv"**. These genes will be the focus of the formal statistical tests in Module 4.

## Module 3: Using JAXMouse_QCpass.csv:
1.	Recreate the base R boxplot from RI, Module 4, Q1 (Expression by Tissue) using ggplot2. Use geom_boxplot() colored by Tissue, with geom_jitter() overlaid, and facet_wrap(~ Treatment) to show Control vs. Treated side by side. Compare the two versions in a Markdown critique.
2.	Recreate the mean-variance scatterplot from R II, Module 1, Q3 using ggplot2. Use geom_point(), color by a logical variable indicating whether the gene is among the top 10 DE candidates (from Module 2), and use ggrepel or geom_text() to label those top 10 genes. This is a publication-style MA-like plot.
3.	Create a faceted ggplot2 violin plot (geom_violin() + geom_boxplot() overlaid) showing Expression distributions for each Tissue, faceted by Treatment. Add proper labels and a clean theme (e.g., theme_bw()). In a Markdown chunk, describe what the violin plot reveals that a boxplot alone cannot.
4.	Save your **three** polished ggplot2 figures from this module using ggsave(). Name them **"JAXMouse_ggplot_boxplot.png", "JAXMouse_MAplot.png"**, and **"JAXMouse_violin.png"**. These figures will be incorporated into your final semester project report.

## Module 4: Using JAXMouse_QCpass.csv and your **JAXMouse_top10_DE_candidates.csv**:
1.	For each of your top 10 DE candidate genes, test whether the Expression values are normally distributed using a Shapiro-Wilk test (shapiro.test()). Create a QQ plot for each gene (you may facet these in ggplot2). What proportion of genes have normally distributed expression? This determines whether you will use parametric or non-parametric tests in Q2.
2.	For each of your top 10 DE candidate genes, conduct the appropriate two-sample test (t.test() if normal, wilcox.test() if not) comparing Control vs. Treated expression. Include **all four hypothesis testing steps** for at least TWO of the genes in full; for the remaining genes, report only the test statistic and p-value in a summary table.
3.	Apply a Bonferroni correction (p.adjust(method = "bonferroni")) to your 10 p-values. How many genes remain significant after correction? Why is multiple testing correction essential when testing many genes simultaneously? (This is a foundational concept in genomics: bulk RNA-seq studies test thousands of genes at once.)
4.	Produce a volcano plot: a scatterplot where x = log2(fold change: mean Treated / mean Control) and y = -log10(raw p-value), for all genes in the dataset. Color points red if they are among your top 10 DE candidates. Label those points with gene names. Save as "JAXMouse_volcano.png". This is one of the most iconic plots in genomics.

## Module 5: Using JAXMouse_QCpass.csv:
1.	Using one-way ANOVA (or Kruskal-Wallis if assumptions are violated), test whether Expression differs across the three Tissue types for each of your top 10 DE candidate genes. For genes where ANOVA is significant, apply TukeyHSD() to identify which tissue pairs differ. Summarize results in a table.
2.	Test whether Age_weeks is correlated with Expression levels across all samples (using Pearson and Spearman correlation). Do this for each of the three tissue types separately. Is there a tissue where age appears to predict expression? Display with a scatterplot + regression line using ggplot2 geom_smooth(method = "lm").
3.	For the gene with the strongest evidence of a Treatment effect (lowest p-value from Module 4), fit a linear model: Expression ~ Treatment + Tissue + Sex + Age_weeks. Examine the model summary. Which predictors are significant? Calculate and plot the residuals. Are any samples obvious outliers? Label them by SampleID.

# **FINAL SEMESTER PROJECT DELIVERABLE:** 
Compile your complete analysis from both RI and RII into a single polished Quarto report titled "JAXMouse_FinalReport_LastnameFirstInitial.html". The report should include: (a) an Introduction describing the biological question and dataset; (b) all five R I module analyses (data inspection through descriptive statistics); (c) all five R II module analyses (tidyverse wrangling, ggplot2 figures, hypothesis tests, ANOVA, regression); (d) a Conclusion section synthesizing your findings — does treatment alter gene expression, does this differ by tissue, and what biological story do these data tell?
This final report demonstrates the complete R programming and data analysis workflow: from raw data to reproducible scientific communication — exactly as practiced by computational biologists in research settings. 

