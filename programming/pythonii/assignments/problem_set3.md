Day 3 questions: 

We did these in class, so please include MANY comments explaining the details of your solution. 

## Question 1: 
#HAND IN THE CONVERSION TO HIGHER ORDER WITH ANONYMOUS functions. We'll work on this in class
dna_list=["TAGC","ACGTATCGC","ATG","ACGGCTAG"]
percent_A_T=[]
for dna in dna_list:
    print(dna.count("A"))
    print(dna.count("T"))
    len(dna)     
    percent_A_T.append((dna.count("A")+ dna.count("T"))/len(dna))
print(percent_A_T)

## Question 2: 
translate this into a for loop 
# An example of the use of map function: 
squares = list(map(lambda x: x * x, [0, 1, 2, 3, 4]))
#if you fail to use list() - you will only get a pointer
#square_no_List=map(lambda x: x * x, [0, 1, 2, 3, 4])
print(squares)

## Question 3.
Build a platypus class. It should inherit from the mammalian superclass and, because platypuses have some specialized traits that not all mammals have, it will also override some attributes and methods. Perhaps you can use a polymorphic method to differentiate between most mammals and platypuses. You will likely find it useful to follow the outline of the cars/electric cars cells, except (of course) replacing mammals/platypuses. 
https://en.wikipedia.org/wiki/PlatypusLinks to an external site.
https://en.wikipedia.org/wiki/MammalLinks to an external site.
In lecture, I mentioned: 
Inheritance?  <-- could inherit from a mammal superclass, but they lay eggs, sweat milk, venomous spikes 
Attributes? Maybe: total_fecundity, venomous spikes. 
Methods? Maybe: laying_eggs
You can be as creative as you like. 


You can be as creative as you like. 
