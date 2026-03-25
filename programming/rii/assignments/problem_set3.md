Remember: 
- name your file with the following standard: **LastnameFirstInitial_RII_Module3.qmd**
- To answer questions in Module 4, write out the four steps of hypothesis testing. Recall the steps are:

1. Stating the Ho/Ha
2. Stating and running the appropriate test and listing any assumptions mentioned so far
3. Stating the alpha and how the p-value compared to this alpha
4. Concluding – do you reject or fail to reject your null hypothesis.

These steps should be included in your markdown chunks not your R programming chunks. Always include interpretation for your answers.

-----------

## Question 1: 
Focus on only one trait in the Bumpus data set (you can choose whichever numeric trait appeals to you): 
- **is there any indication of stabilizing selection on your chosen trait among the house sparrows?** To rephrase the previous question, more precisely:**Do the survivors of the storm have less variance than the non-surviving** You don't need to conduct a hypothesis test just provide graphical (hint: probably a boxplot) evidence and summary statistic evidence (mean, median etc).
- Is there is a difference in the variance of the trait between male and female sparrow? Again, you don't need to conduct a formal test just provide graphical (boxplot) evidence with the males and female values of the trait separated and summary statistic evidence (mean, median etc).
- Using the age categorical variable **test** whether adult male and juvenile (young) male birds were equally likely to have survived the storm. In this data set, adult/youth information is only provided for the male birds; a=adult and y = young/juvenile. This question is like the hypothesis question we worked through in module 4 except that it is important to recognize that, for this question, n = total male survival count (where n=trials) and is not total survival (which would include females). Provide the answer using both the **binom.test()** and the **prop.test()** function. Which of these two tests had a smaller p-value? Explain why that is the case.


## Question 2:
We explored multiple ways to answer the following question so use **any two methods** you want to get the answer: If you flipped a coin 1000 times, what is the probability of having 84 or fewer heads? How do your two answers compare (for instance, are they exactly the same? Are they different? If so, why are they different?)


## Question 3: 
Most animals are bilaterally symmetric, and among those that are there are very few systematic differences where the left side is larger or small than the right side. In part, this basic symmetry seems to be common because it is difficult to evolve asymmetry, but also for most things a symmetric condition seems to be most functional. In some cases, however, asymmetry may be lead to higher fitness. One such case is among snail-eating snakes. Snails are themselves asymmetrical (because they tend to coil to the right, rather than to the left), and for snakes who eat snails, it turns out to be more useful to have more teeth on the right side of the head, because the snakes grip the snail most effectively on the right to remove them from their shells. Given this, is asymmetry common among snail-eating snakes?
The data file **"R2_AsymmetricalSnakes.csv"** contains data on the asymmetry score (right side tooth count minus left side tooth count) for twelve species of snakes that eat snails. **Follow the general visual procedure outlined** in Module_4AB and answer the above question using the **qqnorm** and** qqline functions**. Use a formal test to see if the data set is normally distributed. Could you run a t-test on this data? Explain why or why not.

## Question 4:
It is discovered that the data discussed in the recitation were all male mooses (let's not discuss how this was ascertained). Female mooses from the same region, the north region, were all weighed: 301, 320, 382, 401, 349, 318, 342 and 369. Do northern female mooses weight less than their male counterparts? (include ALL four hypothesis testing steps and code with answer).

## Question 5: 
The data file "R2_Sleep contains information on 10 individuals who took two different sleep aids. Each row represents a different individual, measured in each of the two ways. Do both measurements give the same result? (include ALL four hypothesis testing steps and code with answer). 
- What type of t-test is most appropriate here, and why?
- What sample size would be needed to detect a difference of 0.25 hours with 90% power?
