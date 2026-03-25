To answer questions in Module 4, write out the four steps of hypothesis testing. Recall the steps are:

1. Stating the Ho/Ha
2. Stating and running the appropriate test and listing any assumptions mentioned so far
3. Stating the alpha and how the p-value compared to this alpha
4. Concluding – do you reject or fail to reject your null hypothesis.

These steps should be included in your markdown chunks not your R programming chunks. Always include interpretation for your answers.

---------

## Question 1: 
ROC and AUC: Repeat the example that was worked in your Module 4 Notebook, but this time create **one graph that includes all of: gos6, WFNS, Age, s100b, and NDKA**. Calculate the AUC for these factors. Based on the AUC value, which of these factors are good classifiers for outcome after aSAH?


## Question 2:
Produce a Kaplan-Meier curve for the built-in Leukemia data set ('leukemia'). This dataset is similar to the lung dataset, but instead of male/female column, there is a column, x, that is "Maintained" or "Nonmaintained". Under the Status columns, the Censored individuals are given 1 and dead individuals are assigned the number 2.
Begin by producing a ggplot histogram that distinguishes between censored and uncensored data.
Create a survival object and peek at the columns.
Use ggplot2 to draw an attractive KM survival curve with the median indicated on it.
Use basic R to draw the survival curves for maintained and non-maintained individuals.
