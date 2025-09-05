I don't know how far we will get into Module 5, so this assignment is tentative. I will confirm during class. These questions mimic the analysis in the module5AB notebook so you might want to complete all of them if you are interested in correlation/regression/ANOVA in R since there is one question per each of these analyses. I have included the datasets in the module. 
## Question 1:
The European cuckoo does not look after its own eggs, but instead lays them in the nests of birds of other species (note: this seems like an excellent strategy in my opinion). We have seen previously that cuckoos sometimes have evolved to lay eggs that are colored similarly to the host birds' eggs. Is the same true of size -- do cuckoos lay eggs of different sizes in nests of different hosts? The data file "cuckooeggs.csv" contains data on the lengths of cuckoo eggs laid in a variety of other species' nests.
1. Test for a difference between the host species in the size of the cuckoo eggs. Remember: You need to include all four steps when conducting a test (including testing and investigating the assumptions of the test you wish to use).
2. Using a Tukey-Kramer test, identify which pairs of host species are significantly different from each other? If your result in part a failed to reject the null hypothesis, still conduct a Tukey-Kramer test and comment on its appropriateness and conclusions (are the conclusions consistent with the conclusion in part a?).
## Question 2:
Animals that are infected with a pathogen often have disturbed circadian rhythms. (A circadian rhythm is a daily cycle in a behavior or physiological trait that persists in the absence of time cues.) Shirasu-Hiza et al. (2007) wanted to know whether it was possible that the circadian timing mechanism itself could have an effect on disease. They used three groups of fruit flies: one "normal", one with a mutation in the timing gene tim01 (heterozygous = 1 copy of allele), and one group that had the tim01 mutant in a homozygous state (2 copies). They exposed these flies to a dangerous bacteria, Streptococcus pneumoniae, and measured how long the flies lived afterwards, in days. The date file "circadian mutant health.csv" shows some of their data.
- Plot a boxplot that includes each of the three groups (not separate boxplots, all three groups should be on the same boxplot). Do these data match the assumptions of an ANOVA?
- Do an appropriate test to ask whether lifespan differs between the three groups of flies. (Hint: use a nonparametric test in this case – don't worry about transformations since you have already worked through the transformations in the notebook and they are seldom worth the time....).
## Question 3: 
Larger animals tend to have larger brains. But is the increase in brain size proportional to the increase in body size? A set of measurements on mammal body and brain size was collated by Allison and Cicchetti (1976), and these data are to be found in the data set “mammals.csv.” The file contains columns giving the species name, the body mass (in kg) and brain size (in g) of 62 different mammal species
- Plot brain size against body size.Is the relationship linear?
- Find a transformation (for either or both variables) that makes the relationship between these two variables linear.
- Is there statistical evidence that brain size is correlated with body size?
- Can you use a parametric test or do you need to use the parametric version of the test? Why? Check the assumptions of the test. Run both the parametric and the nonparametric tests and compare their results. Do you have any explanation for any discrepancies?
- What line best predicts (transformed) brain size from (transformed) body size. Superimpose this line onto your scatterplot.
- Make a residual plot.Which species has the highest brain size for their body size? Which species has the smallest brain relative to that predicted by its body size? You will want to superimpose the names of the animals from the downloaded file onto the graph of the residuals. You can do this with the function >text(). To see how this works, an example is given below:
```
> plot(test_mamamal.resid, col='purple', pch=19,cex=1,lty=”solid”,lwd=2)
> text(test_mam.resid,labels=name,srt=60, cex=0.3,pos=3)
```
- Are humans significantly different from the brain size predicted by our body size? To break this (general) question down into component: Conduct the appropriate test based on the assumptions that are met. Are there other outliers present? If so, give the names of two other mammals that are quite different.

- Is there a clear correlation between brain size and body size?
- Are there outliers present in this data set? Can you identify them
