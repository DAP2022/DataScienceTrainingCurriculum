# Biostatistics II: Module 4AB Questions

1. The foraging gene, for, has been found to underlie variation in foraging behavior in several insect species. Researchers examined if the gene might influence behavioral differences in the honeybee. Worker bees perform tasks in the hive such as brood care when they are young and switch to foraging for nectar and pollen as they age. The authors compared for gene expression in nurse and foraging workers bees in three bee colonies. 

|Worker type|		Colony |	for gene expression|
|:---:|:---:|:---:|
|Nurse | 1 | 0.99 |
|Forager |	1 |	1.93 |
|Nurse |	2 |	1.00 |
|Forager |	2 |	2.36 |
|Nurse	|	3	|	0.24 |
|Forager |	3 |	1.96 |

A. Write out the full null hypothesis and the alternate hypothesis

B. Interpret the given table with hypothesis testing.

|Source of Variation|	Sum of Squares |	df| Mean Squares | F| P|
|:---:|:---:|:---:|:---:|:---:|:---:|
| Colony| 0.34 | 2|0.17 | | |
| Worker Type| 2.69 | 1 | 2.69 | 35.53 | 0.027 |
| Residual | 0.15| 2| 0.076| | |

C. Is worker type a random effect or a fixed effect?

D. Explain the purpose of a blocking variable in experimental design?

2. There are two strains of mouse and three diets. Using the following table, explain any main effects, and any interactions.

 |Source of Variation|	Sum of Squares |	df| Mean Squares | F| P|
|:---:|:---:|:---:|:---:|:---:|:---:|
| Diet| 30.5 | 2|15.25 | 5.12 |0.008|
| Genotype| 12.3 | 1 | 12.3 | 4.13| 0.045 |
| Diet*Genotype| 8.6 | 2 | 4.3 | 1.44| 0.246 |
| Residual | 59.7| 20| 2.99| | |


3. 3. We want to assess whether Diet affects gene expression, controlling for the influence of body weight. 

 |Source of Variation|	Sum of Squares |	df| Mean Squares | F| P|
|:---:|:---:|:---:|:---:|:---:|:---:|
| Body Weight| 50.2 | 1|50.2 | 12.8 |0.001|
| Diet| 20.6 | 2 | 10.3 | 2.63| 0.09 |
| Residual | 78.0| 19| 4.11| | |

A. What is the covariate in this case? 

B. The first round of fitting has already occurred. Can you write out the F equations for this second round and interpret the results of this table on gene expression? 


