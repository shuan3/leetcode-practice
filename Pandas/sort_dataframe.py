import pandas as pd
from typing import List
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    condition="animals.weight>100"
    df=animals[animals.weight>100].sort_values(by=["weight"], ascending=False)
    return pd.DataFrame(df['name'])


import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:

    return animals[animals['weight']>100].sort_values(['weight'],ascending=False)[['name']]






# get # rows and # columns

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0],len(players.column)]
    


#display 3 rows of data
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

#select columns
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students.student_id==101][['name','age']]


import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[ students["student_id"] == 101, ["name", "age"] ]
    




#join and rename columns

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    combine = customers.merge(orders, how='left', right_on = 'customerId', left_on = 'id')
    combine = combine[combine['customerId'].isna()]
    combine = combine.rename(columns={'name':'Customers'})
    return combine[['Customers']]