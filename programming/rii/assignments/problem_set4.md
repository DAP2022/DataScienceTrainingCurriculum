## Question 1: 
Most animals are bilaterally symmetric, and among those that are there are very few systematic differences where the left side is larger or small than the right side. In part, this basic symmetry seems to be common because it is difficult to evolve asymmetry, but also for most things a symmetric condition seems to be most functional. In some cases, however, asymmetry may be lead to higher fitness. One such case is among snail-eating snakes. Snails are themselves asymmetrical (because they tend to coil to the right, rather than to the left), and for snakes who eat snails, it turns out to be more useful to have more teeth on the right side of the head, because the snakes grip the snail most effectively on the right to remove them from their shells. Given this, is asymmetry common among snail-eating snakes?
The data file "R2_AsymmetricalSnakes.csv" contains data on the asymmetry score (right side tooth count minus left side tooth count) for twelve species of snakes that eat snails. Follow the general visual procedure outlined in Module_4AB and answer the above question using the qqnorm and qqline functions. Use a formal test to see if the data set is normally distributed. Could you run a t-test on this data? Explain why or why not.
## Question 2:
It is discovered that the data discussed in the recitation were all male mooses (let's not discuss how this was ascertained). Female mooses from the same region, the north region, were all weighed: 301, 320, 382, 401, 349, 318, 342 and 369. Do northern female mooses weight less than their male counterparts? (include ALL four hypothesis testing steps and code with answer).
## Question 3: 
The data file "R2_Sleep contains information on 10 individuals who took two different sleep aids. Each row represents a different individual, measured in each of the two ways. Do both measurements give the same result? (include ALL four hypothesis testing steps and code with answer)
## Question 4: 
If we wanted to pick up a difference of 1 between Drug A and Drug B and we wanted a power level of 0.90, what sample size would we need?
## Question 5:
Produce a Kaplan-Meier curve for the built-in Leukemia data set ('leukemia'). This dataset is similar to the lung dataset, but instead of male/female column, there is a column, x, that is "Maintained" or "Nonmaintained". Under the Status columns, the Censored individuals are given 1 and dead individuals are assigned the number 2.
Begin by producing a ggplot histogram that distinguishes between censored and uncensored data.
Create a survival object and peek at the columns.
Use ggplot2 to draw an attractive KM survival curve with the median indicated on it.
Use basic R to draw the survival curves for maintained and non-maintained individuals.
