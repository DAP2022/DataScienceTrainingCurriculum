## Question 1: 

Use the following to explore the maternal mortality dataframe (included in the Module 4 datasets): 

1. use groupby in a command. This is an artificial question (there are better methods to answer it for this data set), but use groupby to get the count of countries reporting maternal mortality for the following years (or substitute in other years, if they are particularly interesting to you): "1800", "1850", "1910","1925","1950","2000","2013". 

2. Plot the data. You can do what we did in class and plot countries and a few selected years. You can use the matplotlib cheatsheets (https://matplotlib.org/cheatsheets/_images/cheatsheets-1.png
https://matplotlib.org/cheatsheets/_images/cheatsheets-2.pngLinks to an external site.) to make your plots slightly more fancy. You might find an interesting pattern!

 

## Question 2: 

This is an excellent website for SQL commands: https://www.sqlitetutorial.net/

Using the same database ("JAX2024_Desert_data.db"), PICK ONE (of the two given below) and construct the following SQL queries: 

I didn't present this as well organized as it could have been, so please remember:
1. Put your 'stack' of libraries in a cell:
``` 
import numpy as np
import pandas as pd
import sqlite3 as sql
```
2. Create a connection object: 
connection_desert=sql.connect("JAX2024_Desert_data.db")
3. The connection object is the second argument of the query (I have highlighted the other important pieces of the query):
```
dfA = pd.read_sql_query("SELECT species_id,hindfoot_length FROM Desert_ecol_info WHERE hindfoot_length >= 30;", connection_desert)
```
1. Only include the top 40 largest individual rodents. The data should include species_id, year and weight and the individuals should be sorted in descending order (with any 'ties' broken based on hindfoot_length). NOTE: this command will look similar to dFI in the examples we covered in class. 

2. Extract only the following information to the screen (a print statement is fine): species="PE", sex and where the animal was trapped. Remove any NULL elements (remember to remove null elements in this database use NOT ''. (<-those are two single quotes). 

 
