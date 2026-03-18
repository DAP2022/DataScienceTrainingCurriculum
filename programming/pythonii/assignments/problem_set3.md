# Module 3 Questions

What this assignment tests: 
    1. **Functional Programming**: map, filter, lambda and their relationship to for loops
    2. **Object Oriented Programming**: class, constructor, inheritance, polymorphism
    3. **Paradigm Fluency**: being able to translate the same logic between procedural and OOP and functional styles 

-----------

## Question 1: AT Content: from for loop to functional style
Below is a procedural solution that caulculates the AT content of a list of DNA sequences:  
```
dna_list=["TAGC","ACGTATCGC","ATG","ACGGCTAG"]
percent_A_T=[]
for dna in dna_list:
    print(dna.count("A"))
    print(dna.count("T"))
    len(dna)     
    percent_A_T.append((dna.count("A")+ dna.count("T"))/len(dna))
print(percent_A_T)
```
1. Rewrite this as a list comprehension (it should all fit on one line)
2. Rewrite using map() and a lambda function
3. Explain in 2-3 sentences: which version is most readable to you? Which one would you prefer to find in someone else's codebase? 

---------
## Question 2: map to a for loop
Translate this functional code back into an explicit for loop:
```
#An example of the use of map function: 
squares = list(map(lambda x: x * x, [0, 1, 2, 3, 4]))
print(squares)
```
Confirm that your for loop produces identical output. 

----------
## Question 3.
Build a platypus class that demonstrates: **inheritance**, **attribute overriding**, and **polymorphism**. It should inherit from the mammalian superclass and, because platypuses have some specialized traits that not all mammals have, it will also override some attributes and methods. You can use a polymorphic method to differentiate between most mammals and platypuses. You will likely find it useful to follow the outline of the cars/electric cars cells, except (of course) replacing mammals/platypuses. 
- https://en.wikipedia.org/wiki/PlatypusLinks to an external site.
- https://en.wikipedia.org/wiki/MammalLinks to an external site.

1. Create a Mammal superclass with at least three attributes and two methods
2. Create a Playpus subclass that inherits from Mammal. Platypuses (and Echnida) are weird mammals since they lay eggs instead of giving birth to live young so that will be a difference that you might use to override?
3. Create at least one instance of the Mammal and at least one instance of the Platypus. 


You can be as creative as you like. 

