This assignment is testing the following major concepts: 

- **Modules**: Packaging functions into a .py file and importing them
- **Recursion**: Base case+ general case
- **Code Reading**: Understanding and modifying someone else's code!
- **Functional thinking**: eliminating state

### Question 1: Modularize ORFadvisor()

Use the **ORFadvisor()** function that you wrote in the assignments for Module 1 and move it to a separate .py file to create a module. Then: 
- Import your module from a new notebook cell using the same imprt syntax you used for the **re** module in python I.
- Call **ORFadvisor()** from the imported module and confirm that it produces the same output (you might use test cases as well as the DNA string that we have reused throughout the course to do this).
- Add at least one more helper function to the module. For example, a function that takes a sequence and removes the introns to return only the coding sequence is the kind of problem that you have already solved and you could transform your solution into a function!

## Question 2: MCMC mutation simulation - read, extend, explain
*Note: This is a summative question about understanding code, tweaking it modestly, and explaining both the code and your improvement(s). You will recycle other people's code A LOT in the wild and so being able to read and extend code you didn't create yourself is really important!* 

Use the MCMC program discussed in Module 2B of Python II as a base for this question and remember that there is a diagram of what it is doing here: [MCMC](https://github.com/DAP2022/DataScienceTrainingCurriculum/blob/main/programming/pythonii/course_content_jupyter_notebooks/images/MCMC_Example.jpeg) 

--------
I have written a terribly inefficient program that takes an original 4 nucleotide string and mutates it according to certain rules over a specified number of steps (approximately 1,000,000). At certain step numbers (**1,100,1000, 10000**) the program prints out what the 4 nucleotides have mutated into. Do the following: 

1. **Replace the four hard-coded times points, (1,100,1000,10000), with a list the user provides as a function argument**. *Do not use input() for this*; pass the list when calling the function. This is motivated by a 'real-life' situation: You often want to be able to 'dip' into a simulation at certain time points and sample what the state of the 4 nucleotide string is at that point. In order to accomplish that, you will need to add in a counter that tracks the replication cycle and prints out both the cycle number and what the mutated four nucleotide sequence is at that time point. 
2. **Add a mutation log**: this is a feature that keeps track of when a mutation event happened, where in the four sequences it happened and what the mutation was. This only needs to have a simple print statement that identifies these things to the user (maybe at the end of the program?)
3. **Pick one of the following to do and explain it**: 
•    Better encapsulation of the function by breaking it up into smaller functions that are called from within the main function. Compare the time that your program takes with better 'encapsulation' versus the original. Explain any difference in time.  
•    Replace the while loop with for loop(s) since while loops tend to be inefficient. Compare the time that your program takes between the while and for loops. If there is or is not improvement in time, suggest a reason. 
•     Allow user to specify as large of a nucleotide sequence as they want – instead of just 4 nucleotides, users could specify 8 or 1000 or whatever length that they want. 
•    You may have another idea to make this function more optimal - just include it in your comments/explanation so I know what it is. 

## Question 3: Implement recursion

Solve the Fibonacci sequence using recursion (see Module_2A). Your function must have: 
1. A clearly named base case (when does it stop?)
2. A clearly named recursive case (how does it move toward the base?)
Use pythontutor.com to step through your function for fib(5) and include 1-2 sentences about what you observed in the stack call. 

## Question 4: Eliminate state (Functional thinking)

1. rewrite the following to make it "stateless"*: 
```
x=0
#x has state because we are setting it to be 0 and it is being modified depending on 
#where it is in the program. 
print(x)
for i in range(10):
    print(x, "becomes..." )
    x=x+i
    print(x, "Go through the loop again and the value of x has changed!")
print(x)
```
* stateless is a bit nuanced, but in this case think of it as "the output of a function or for loop should depend ONLY on the arguments, and not on the value of any other variable that is outside of the function or for loop". 

Assignment 3 will continue with higher level function conversions. 

