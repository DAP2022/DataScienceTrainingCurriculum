To answer question 3, write out the four steps of hypothesis testing. Recall the steps are:

1. Stating the Ho/Ha
2. Stating and running the appropriate test and listing any assumptions mentioned so far
3. Stating the alpha and how the p-value compared to this alpha
4. Concluding – do you reject or fail to reject your null hypothesis.

These steps should be included in your markdown chunks not your R programming chunks. Include interpretation for your answers.

## Question 1: 
Focus on only one trait in the Bumpus data set (you can choose whichever numeric trait appeals to you): 
- **is there any indication of stabilizing selection on your chosen trait among the house sparrows?** To rephrase the previous question, more precisely: Do the survivors of the storm have less variance than the non-surviving? You don't need to conduct a test just provide graphical (hint: probably a boxplot) evidence and summary statistic evidence (mean, median etc).
- Is there is a difference in the variance of the trait between male and female sparrow? You don't need to conduct a formal test just provide graphical (boxplot) evidence with the males and female values of the trait separated and summary statistic evidence (mean, median etc).
- Using the age categorical variable test whether adult male and juvenile (young) male birds were equally likely to have survived the storm. In this data set, adult/youth information is only provided for the male birds; a=adult and y = young/juvenile. This question is like the hypothesis question we worked through in module 3 except that it is important to recognize that, for this question, n = total male survival count (where n=trials) and is not total survival (which would include females). Provide the answer using both the binom.test() and the prop.test() function. Which of these two tests had a smaller p-value? Explain why that is the case.
## Question 2:
We explored multiple ways to answer the following question so use any two methods you want to get the answer: If you flipped a coin 1000 times, what is the probability of having 84 or fewer heads? How do your two answers compare (for instance, are they exactly the same? Are they different? If so, why are they different?)
## Question 3: 
ROC and AUC: Repeat the example that was worked in your rmd file, but this time create one graph that includes gos6, WFNS, Age, s100b, and NDKA. Calculate the AUC for these factors. Based on the AUC value, which of these factors are good classifiers for outcome after aSAH?
