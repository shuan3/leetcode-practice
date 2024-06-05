from typing import List

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    schema=['student_id','age']
    return pd.DataFrame(data=student_data,columns=schema)
    





#if input data is json
import pandas as pd
 
# initialize data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df)




# Python code demonstrate creating
# Pandas Dataframe from Dicts of series.
 
import pandas as pd
 
# Initialize data to Dicts of series.
d = {'one': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd']),
     'two': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd'])}
 
# creates Dataframe.
df = pd.DataFrame(d)
 
# print the data.



# Python program to demonstrate creating
# pandas Dataframe from lists using zip.
 
import pandas as pd
 
# List1
Name = ['tom', 'krish', 'nick', 'juli']
 
# List2
Age = [25, 30, 26, 22]
 
# get the list of tuples from two lists.
# and merge them by using zip().
list_of_tuples = list(zip(Name, Age))
 
# Assign data to tuples.
list_of_tuples
 
 
# Converting lists of tuples into
# pandas Dataframe.
df = pd.DataFrame(list_of_tuples,
                  columns=['Name', 'Age'])
 
# Print data.
print(df)